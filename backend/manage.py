from cancer.app import create_app
from flask_script import Server, Manager
from flask_migrate import MigrateCommand

manager = Manager(create_app)
manager.add_command("runserver", Server())
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()