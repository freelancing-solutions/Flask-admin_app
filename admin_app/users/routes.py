from flask import Blueprint, render_template, url_for
users_bp = Blueprint('users', __name__)


@users_bp.route('/users/<path:path>', methods=["GET", "POST"])
def users(path: str) -> tuple:
    if path == "users":
        return render_template('users/users.html')
    elif path == "messages":
        return render_template('users/messages.html')
    elif path == "subscriptions":
        return render_template('users/subscriptions.html')
