from flask import Blueprint, render_template, url_for, current_app
from admin_app.config import only_cache_get
from admin_app.main import route_cache, cache_timeout

users_bp = Blueprint('users', __name__)


@users_bp.route('/users/<path:path>', methods=["GET", "POST"])
# @route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def users(path: str) -> tuple:
    if path == "users":
        return render_template('users/users.html')
    elif path == "messages":
        return render_template('users/messages.html')
    elif path == "subscriptions":
        return render_template('users/subscriptions.html')
