from functools import lru_cache
from flask import Blueprint, render_template
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login')
@lru_cache(maxsize=16)
def login() -> tuple :
    return render_template('login.html'), 200


@auth_bp.route('/recover', methods=['POST'])
def recover():
    """
        recover password
    :return:
    """
    pass


@auth_bp.route('/register')
@lru_cache(maxsize=16)
def register() -> tuple:
    return render_template('register.html'), 200


@auth_bp.route('/logout')
@lru_cache(maxsize=16)
def logout() -> tuple:
    return render_template('logout.html'), 200

