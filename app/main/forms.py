from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField, TextAreaField, SelectField,\
    SubmitField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Length, Email, Regexp
from flask_babel import _, lazy_gettext as _l
from app.models import User, Role


#class EditProfileForm(FlaskForm):
#    username = StringField(_l('Username'), validators=[DataRequired()])
#    about_me = TextAreaField(_l('About me'),
#                             validators=[Length(min=0, max=140)])
#    submit = SubmitField(_l('Submit'))
#
#    def __init__(self, original_username, *args, **kwargs):
#        super(EditProfileForm, self).__init__(*args, **kwargs)
#        self.original_username = original_username#

#    def validate_username(self, username):
#        if username.data != self.original_username:
#            user = User.query.filter_by(username=self.username.data).first()
#            if user is not None:
#                raise ValidationError(_('Please use a different username.'))


#class EditProfileAdminForm(FlaskForm):
#    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
#                                             Email()])
#    username = StringField('Username', validators=[
#        DataRequired(), Length(1, 64),
#        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
#               'Usernames must have only letters, numbers, dots or '
#               'underscores')])
#    confirmed = BooleanField('Confirmed')
#    role = SelectField('Role', coerce=int)
#    name = StringField('Real name', validators=[Length(0, 64)])
#    location = StringField('Location', validators=[Length(0, 64)])
#    about_me = TextAreaField('About me')
#    submit = SubmitField('Submit')

#    def __init__(self, user, *args, **kwargs):
#        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
#        self.role.choices = [(role.id, role.name)
#                             for role in Role.query.order_by(Role.name).all()]
#        self.user = user
#
#    def validate_email(self, field):
#        if field.data != self.user.email and \
#                User.query.filter_by(email=field.data).first():
#            raise ValidationError('Email already registered.')

#    def validate_username(self, field):
#        if field.data != self.user.username and \
#                User.query.filter_by(username=field.data).first():
#            raise ValidationError('Username already in use.')


#class EmptyForm(FlaskForm):
#    submit = SubmitField('Submit')


class PredictForm(FlaskForm):
    bsteroid = StringField(_l('Before Steroid'), validators=[DataRequired()])
    asteroid = StringField(_l('After Steroid'), validators=[DataRequired()])
    conditions = StringField(_l('is it normal or high?'), validators=[DataRequired()])
    bp = StringField(_l('Do you have bp ?'), validators=[DataRequired()])
    submit = SubmitField(_l('Predict Patience IOP'))

