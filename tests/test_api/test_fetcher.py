import typing
from admin_app.api.fetcher import APIFetcher
from tests import test_app


def test_fetch_stock():
    api_fetcher: APIFetcher = APIFetcher()
    api_fetcher.init_app(app=test_app())
    response, status = api_fetcher.fetch_stock(stock_id="ABC")
    json_data: dict = response.get_json()
    message = json_data.get('message')
    assert message is not None, "fetch_stock not responding correctly"
    assert json_data['status'], message


def test_fetch_broker():
    api_fetcher: APIFetcher = APIFetcher()
    api_fetcher.init_app(app=test_app())
    response, status = api_fetcher.fetch_broker(broker_id="ABC")
    json_data: dict = response.get_json()
    message: typing.Union[None, str] = json_data.get('message')
    assert message is not None, "fetch_broker not responding correctly"
    assert json_data['status'], message


def test_fetch_buy_volume():
    api_fetcher: APIFetcher = APIFetcher()
    api_fetcher.init_app(app=test_app())
    response, status = api_fetcher.fetch_buy_volume()


def test_fetch_sell_volume():
    pass


def test_fetch_net_volume():
    pass
