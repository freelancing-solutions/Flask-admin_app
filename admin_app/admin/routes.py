from flask import Blueprint, render_template, url_for, request, current_app
from admin_app.config import only_cache_get
from admin_app.main import api_fetcher, api_sender, cache_timeout
from admin_app.main import route_cache

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/', methods=["GET", "POST"])
@route_cache.cached(timeout=cache_timeout)
def home() -> tuple:
    return render_template('index.html'), 200


# noinspection DuplicatedCode
@admin_bp.route('/data/<path:path>', methods=["GET", "POST"])
@route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def data(path: str) -> tuple:
    import asyncio
    if request.method == "GET":
        if path == "exchange":
            return render_template("forms/exchange.html"), 200
        elif path == "broker":
            return render_template("forms/broker.html"), 200
        elif path == "stock":
            return render_template("forms/stock.html"), 200
        elif path == "scrapped":
            return render_template("forms/manual.html"), 200
    else:
        json_data: dict = request.get_json()
        loop = asyncio.new_event_loop()
        if path == "exchange":
            return loop.run_until_complete(api_sender.send_exchange(exchange=json_data))
        elif path == "broker":
            return loop.run_until_complete(api_sender.send_broker(broker=json_data))
        elif path == "stock":
            return loop.run_until_complete(api_sender.send_stock(stock=json_data))


# noinspection DuplicatedCode
@admin_bp.route('/data/<path:resource>/edit/<path:uid>', methods=["GET", "POST"])
@route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def data_edit(resource: str, uid: str) -> tuple:
    import asyncio
    if request.method == "GET":
        if resource == "exchange":
            response = api_fetcher.fetch_exchange(exchange_id=uid)
            response_code: int = int(response[1])
            if response_code == 200:
                exchange_data: dict = response[0].get_json().get('payload')
                return render_template("forms/edit-exchange.html", exchange_data=exchange_data), 200
            else:
                # let error handlers handle this problem
                pass
        elif resource == "broker":
            response = api_fetcher.fetch_broker(broker_id=uid)
            response_code: int = int(response[1])
            if response_code == 200:
                broker_data: dict = response[0].get_json().get('payload')
                return render_template("forms/edit-broker.html", broker_data=broker_data), 200
        elif resource == "stock":
            response = api_fetcher.fetch_stock(stock_id=uid)
            response_code: int = int(response[1])
            if response_code == 200:
                stock_data: dict = response[0].get_json().get('payload')
                return render_template("forms/edit-stock.html", stock_data=stock_data), 200
    else:

        json_data: dict = request.get_json()

        loop = asyncio.new_event_loop()
        if resource == "exchange":
            return loop.run_until_complete(api_sender.send_exchange(exchange=json_data))
        elif resource == "broker":
            return loop.run_until_complete(api_sender.send_broker(broker=json_data))
        elif resource == "stock":
            return loop.run_until_complete(api_sender.send_stock(stock=json_data))


@admin_bp.route('/data/<path:resource>/view/<path:uid>', methods=["GET", "POST"])
@route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def data_view(resource: str, uid: str) -> tuple:
    if request.method == "GET":
        if resource == "exchange":
            response = api_fetcher.fetch_exchange(exchange_id=uid)
            response_code: int = int(response[1])
            if response_code == 200:
                exchange_data: dict = response[0].get_json().get('payload')
                return render_template("forms/view/exchange-view.html", exchange_data=exchange_data), 200
        elif resource == "broker":
            response = api_fetcher.fetch_broker(broker_id=uid)
            response_code: int = int(response[1])
            if response_code == 200:
                broker_data: dict = response[0].get_json().get('payload')
                return render_template("forms/view/broker-view.html", broker_data=broker_data), 200

        elif resource == "stock":
            response = api_fetcher.fetch_stock(stock_id=uid)
            response_code: int = int(response[1])
            if response_code == 200:
                stock_data: dict = response[0].get_json().get('payload')
                return render_template("forms/view/stocks-view.html", stock_data=stock_data), 200


@admin_bp.route('/settings/<path:path>', methods=["GET", "POST"])
@route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def settings(path):
    if request.method == "GET":
        if path == "api":
            return render_template("api/settings.html"), 200
        elif path == "scrapper":
            return render_template("scrapper/settings.html"), 200

    elif request.method == "POST":
        if path == "scrapper":
            settings_data: dict = request.get_json()
            return api_sender.send_scrapping_settings(settings_data=settings_data)


@admin_bp.route('/schedules/<path:path>', methods=["GET", "POST"])
@route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def schedules(path):
    if path == "api":
        return render_template("api/schedules.html"), 200
    elif path == "scrapper":
        return render_template("scrapper/schedules.html"), 200


@admin_bp.route('/logs/<path:path>', methods=["GET"])
@route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def logs(path):
    if path == "api":
        return render_template("api/logs.html"), 200
    elif path == "scrapper":
        return render_template("scrapper/logs.html"), 200
