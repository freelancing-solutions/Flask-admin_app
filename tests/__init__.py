from flask import current_app
from admin_app.main import create_admin_app
from admin_app.config import Config


def test_app():
    if not current_app:
        app = create_admin_app(config_class=Config)
        app.app_context().push()
    else:
        app = current_app

    app.testing = True
    return app
