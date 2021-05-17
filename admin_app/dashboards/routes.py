from flask import Blueprint, render_template, request
from admin_app.config import only_cache_get
from admin_app.main import api_fetcher, route_cache, cache_timeout
dash_bp = Blueprint('dashboard', __name__)


@dash_bp.route('/dashboard/<path:path>', methods=['GET', 'POST'])
@route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def dashboard(path: str) -> tuple:
    if request.method == "GET":
        if path == "exchanges":
            return render_template("dashboard/exchanges.html"), 200
        elif path == "brokers":
            return render_template("dashboard/brokers.html"), 200

        elif path == "stocks":
            return render_template("dashboard/stocks.html"), 200

        elif path == "statistics":
            return render_template("dashboard/statistics.html"), 200
    else:
        if path == "exchanges":
            return api_fetcher.fetch_exchanges()
        elif path == "brokers":
            return api_fetcher.fetch_brokers()
        elif path == "stocks":
            return api_fetcher.fetch_stocks()
