# encoding:utf-8
# author:wwg
from app import create_app,db
from flask_script import Manager, Shell,Server
from app.models import FunctionModelsDb
from flask_migrate import Migrate,MigrateCommand
app = create_app()
manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True))
# migrate=Migrate(app,db)
# def make_shell_context():
#     return dict(app=app, db=db, FunctionModels=FunctionModels, CaseInformation=CaseInformation)
# manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
