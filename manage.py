import os
import unittest
import sys
from app.main import create_app
from app.main.jobqueue import jobqueue

def run():
    app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
    app.app_context().push()
    app.run()
    jobqueue.stop_threads()

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