import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
# from app.models import User, Role, Post

from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(app, db, render_as_batch=True)
manager = Manager(app)

def make_shell_context():
    pass
    # return dict(app=app, db=db, User=User, Role=Role, Post=Post)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
