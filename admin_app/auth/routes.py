from flask import Blueprint, render_template, url_for, current_app
from admin_app.config import only_cache_get
from admin_app.main import route_cache, cache_timeout

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login')
# @route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def login():
    return render_template('login.html')


@auth_bp.route('/recover', methods=['POST'])
def recover():
    """
        recover password
    :return:
    """
    pass


@auth_bp.route('/register')
# @route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def register():
    return render_template('register.html')


@auth_bp.route('/logout')
# @route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def logout():
    return render_template('logout.html')

