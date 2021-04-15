import requests
from flask import jsonify


class APIFetcher:
    base_uri: str = "https://data-service.pinoydesk.com/"
    all_stocks_data_endpoint: str = "api/v1/stocks/all/stocks"
    all_brokers_data_endpoint: str = "api/v1/stocks/all/brokers"
    exchange_data_endpoint: str = "api/v1/exchange/get-all-exchanges"
    messages_data_endpoint: str = "api/v1/messages/all"
    tickets_data_endpoint: str = "api/v1/tickets/all"
    affiliate_data_endpoint: str = "api/v1/affiliates/all"
    user_data_endpoint: str = "api/v1/user"
    membership_data_endpoint: str = "api/v1/memberships"
    api_data_endpoint: str = "api/v1/api/all"
    scrapper_data_endpoint: str = "api/v1/scrapper/all"
    get_exchange_endpoint: str = "/api/v1/exchange/get-exchange"
    get_broker_endpoint: str = "/api/v1/stocks/item/broker"
    get_stock_endpoint: str = "/api/v1/stocks/item/stock"

    def __init__(self):
        pass

    def _build_url(self, endpoint: str) -> str:
        if endpoint == "stock":
            return self.base_uri + self.all_stocks_data_endpoint
        elif endpoint == "get-stock":
            return self.base_uri + self.get_stock_endpoint
        elif endpoint == "broker":
            return self.base_uri + self.all_brokers_data_endpoint
        elif endpoint == "get-broker":
            return self.base_uri + self.get_broker_endpoint
        elif endpoint == "exchange":
            return self.base_uri + self.exchange_data_endpoint
        elif endpoint == "get-exchange":
            return self.base_uri + self.get_exchange_endpoint
        elif endpoint == "messages":
            return self.base_uri + self.messages_data_endpoint
        elif endpoint == "tickets":
            return self.base_uri + self.tickets_data_endpoint
        elif endpoint == "affiliate":
            return self.base_uri + self.affiliate_data_endpoint
        elif endpoint == "user":
            return self.base_uri + self.user_data_endpoint
        elif endpoint == "membership":
            return self.base_uri + self.membership_data_endpoint
        elif endpoint == "api":
            return self.base_uri + self.api_data_endpoint
        elif endpoint == "scrapper":
            return self.base_uri + self.scrapper_data_endpoint
        else:
            return ""

    @staticmethod
    def _requester(url: str, data: dict = None) -> tuple:
        try:
            if data:
                response = requests.post(url=url, json=data)
            else:
                response = requests.post(url=url)
            response_data = response.json()
            if response.ok:
                return jsonify({'status': True, 'message': response_data['message'], 'payload': response_data['payload']}), 200
            return jsonify({'status': False, 'message': response_data['message']}), 500
        except ConnectionError as e:
            return jsonify({'status': False, 'message': e}), 200

    def fetch_exchanges(self) -> tuple:
        url = self._build_url(endpoint='exchange')
        return self._requester(url=url)

    def fetch_brokers(self) -> tuple:
        return self._requester(url=self._build_url(endpoint='broker'))

    def fetch_stocks(self) -> tuple:
        return self._requester(url=self._build_url(endpoint='stock'))

    def fetch_exchange(self, exchange_id: str) -> tuple:
        return self._requester(url=self._build_url(endpoint='get-exchange'), data={'exchange_id': exchange_id})

    def fetch_broker(self, broker_id: str) -> tuple:
        return self._requester(url=self._build_url(endpoint='get-broker'), data={'broker_id': broker_id})

    def fetch_stock(self, stock_id: str) -> tuple:
        return self._requester(url=self._build_url(endpoint='get-stock'), data={'stock_id': stock_id})

