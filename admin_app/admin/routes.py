from flask import Blueprint, render_template, url_for
admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@admin_bp.route('/data/<path:path>', methods=["GET", "POST"])
def data(path):
    if path == "exchange":
        return render_template("forms/exchange.html")
    elif path == "broker":
        return render_template("forms/broker.html")
    elif path == "stock":
        return render_template("forms/stock.html")