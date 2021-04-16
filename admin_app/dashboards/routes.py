from flask import Blueprint, render_template, url_for, request
from admin_app.main import api_fetcher
dash_bp = Blueprint('dashboard', __name__)


@dash_bp.route('/dashboard/<path:path>', methods=['GET', 'POST'])
def dashboard(path):
    if request.method == "GET":
        if path == "exchanges":
            return render_template("dashboard/exchanges.html")
        elif path == "brokers":
            return render_template("dashboard/brokers.html")

        elif path == "stocks":
            return render_template("dashboard/stocks.html")

        elif path == "statistics":
            return render_template("dashboard/statistics.html")
    else:

        if path == "exchanges":
            return api_fetcher.fetch_exchanges()
        elif path == "brokers":
            return api_fetcher.fetch_brokers()
        elif path == "stocks":
            return api_fetcher.fetch_stocks()
