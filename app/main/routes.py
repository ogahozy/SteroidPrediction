from crypt import methods
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from flask_babel import _, get_locale
from langdetect import detect, LangDetectException
from app import db
from app.main.forms import  PredictForm
from app.models import User, Predict, Role
from app.decorators import admin_required, Permission
from app.main import bp
import numpy as np
import pickle


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html', title=_('Home'))
                         

@bp.route('/diagnose/<username>', methods=['GET', 'POST'])
@login_required
@admin_required
def diagnose(username):
    user = User.query.filter_by(username=username).first_or_404()
    name = user.name
    username =user.username 
    form = PredictForm()
    if form.validate_on_submit() and current_user.is_administrator:
        bsteroid = int(form.bsteroid.data)
        asteroid  = int(form.asteroid.data)
        conditions = int(form.conditions.data)
        bp= int(form.bp.data)
        to_predict_list = [bsteroid,asteroid,conditions,bp]
        result = ValuePredictor(to_predict_list)
        # perform save to database
        classes = int(result)
        if result== 0:
            prediction ='Not Responding'
        else:
            prediction = 'Responding'
        predict = Predict(name=name,username=username,bsteroid=bsteroid,asteroid=asteroid,conditions=conditions,
                            bp=bp,classes=classes)
        db.session.add(predict)
        db.session.commit()
        return render_template('analyse.html', title=_('Analysis'), prediction=prediction)
    return render_template('diagnose.html', title=_('Analysis'), form=form, user=user) #,

                          
# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 4)
    loaded_model = pickle.load(open("model.sav", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@bp.route('/explore')
@login_required
def explore():
    users = User.query.order_by(User.id)
    return render_template('explore.html', title=_('Explore'),users=users)


@bp.route('/report')
@login_required
def report():
    predict = Predict.query.order_by(Predict.username)
    return render_template('report.html', title=_('Explore'), predict=predict)  


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    predicts = Predict.query.filter_by(username=username)    
    return render_template('user.html', user=user, predicts=predicts)