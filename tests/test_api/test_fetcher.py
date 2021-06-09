from flask import current_app
from admin_app.api.fetcher import APIFetcher
from tests import test_app


def test_fetch_stock():
    api_fetcher: APIFetcher = APIFetcher()
    api_fetcher.init_app(app=test_app())
    response, status = api_fetcher.fetch_stock(stock_id="ABC")
    json_data: dict = response.get_json()
    print(json_data)
    assert False, ""


def test_fetch_broker():
    pass


def test_fetch_buy_volume():
    pass


def test_fetch_sell_volume():
    pass


def test_fetch_net_volume():
    pass
