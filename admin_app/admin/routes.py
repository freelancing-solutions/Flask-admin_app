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


@admin_bp.route('/settings/<path:path>', methods=["GET", "POST"])
def settings(path):
    if path == "api":
        return render_template("api/settings.html")
    elif path == "scrapper":
        return render_template("scrapper/settings.html")


@admin_bp.route('/schedules/<path:path>', methods=["GET", "POST"])
def schedules(path):
    if path == "api":
        return render_template("api/schedules.html")
    elif path == "scrapper":
        return render_template("scrapper/schedules.html")


@admin_bp.route('/logs/<path:path>', methods=["GET"])
def logs(path):
    if path == "api":
        return render_template("api/logs.html")
    elif path == "scrapper":
        return render_template("scrapper/logs.html")

