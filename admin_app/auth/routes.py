from flask import Blueprint, render_template
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login')
# @route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
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
# @route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def register() -> tuple:
    return render_template('register.html'), 200


@auth_bp.route('/logout')
# @route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def logout() -> tuple:
    return render_template('logout.html'), 200

