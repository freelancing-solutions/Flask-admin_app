from flask import Flask
from admin_app.config import Config


def create_admin_app(config_class=Config):
    admin_app = Flask(__name__, template_folder='templates', static_folder='static')
    admin_app.config.from_object(config_class)

    # routes
    from ..admin.routes import admin_bp
    from ..auth.routes import auth_bp
    from ..dashboards.routes import dash_bp
    from ..users.routes import users_bp
    from ..helpdesk.routes import helpdesk_bp
    from ..uploads.routes import uploads_bp

    # blue prints
    admin_app.register_blueprint(admin_bp)
    admin_app.register_blueprint(auth_bp)
    admin_app.register_blueprint(dash_bp)
    admin_app.register_blueprint(users_bp)
    admin_app.register_blueprint(helpdesk_bp)
    admin_app.register_blueprint(uploads_bp)

    return admin_app
