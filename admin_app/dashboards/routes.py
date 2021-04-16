from flask import Blueprint, render_template, url_for, request, current_app
from admin_app.api.fetcher import APIFetcher
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
        data_service_instance: APIFetcher = APIFetcher(app=current_app)
        if path == "exchanges":
            return data_service_instance.fetch_exchanges()
        elif path == "brokers":
            return data_service_instance.fetch_brokers()
        elif path == "stocks":
            return data_service_instance.fetch_stocks()
