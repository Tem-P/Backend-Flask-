import os
import unittest
import sys

#from flask_migrate import Migrate, MigrateCommand
#from flask_script import Manager

from app.main import create_app#, db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.app_context().push()

#manager = Manager(app)

#migrate = Migrate(app, db)

#manager.add_command('db', MigrateCommand)

#@manager.command
def run():
    app.run()

#@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


def main():
    args = sys.argv
    usage = 'manage.py run \n'+\
            'manage.py test'
    if len(args)<2:
        print(usage)
        return
    if args[1]=='run':
        run()
    elif args[1]=='test':
        test()
    else:
        print(usage)

if __name__ == '__main__':
    main()