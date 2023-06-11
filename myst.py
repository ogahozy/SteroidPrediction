from flask_migrate import Migrate, upgrade
from app import create_app, db #, cli
from app.models import User, Predict, Role

app = create_app()
#cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Predict, 'Role':Role}


def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()

    # create or update user roles
    Role.insert_roles()