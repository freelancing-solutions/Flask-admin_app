from flask import Flask
from admin_app.config import Config


def create_admin_app(config_class=Config):
    admin_app = Flask(__name__)
    admin_app.config.from_object(config_class)

    return admin_app
