import os

from flask import Flask

from demoEventSite import home, about, contact, directions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True, root_path=os.path.dirname(os.path.abspath(__file__)),
                static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
                static_url_path='/static')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'demoEventSite.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(home.bp)
    app.register_blueprint(about.bp)
    app.register_blueprint(contact.bp)
    app.register_blueprint(directions.bp)

    return app
