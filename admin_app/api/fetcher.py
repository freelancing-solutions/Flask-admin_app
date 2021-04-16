import requests
from flask import jsonify


# noinspection PyAttributeOutsideInit
class APIFetcher:
    def __int__(self):
        self.base_uri: str = ""
        self.all_stocks_data_endpoint: str = ""
        self.all_brokers_data_endpoint: str = ""
        self.exchange_data_endpoint: str = ""
        self.messages_data_endpoint: str = ""
        self.tickets_data_endpoint: str = ""
        self.affiliate_data_endpoint: str = ""
        self.user_data_endpoint: str = ""
        self.membership_data_endpoint: str = ""
        self.api_data_endpoint: str = ""
        self.scrapper_data_endpoint: str = ""
        self.get_exchange_endpoint: str = ""
        self.get_broker_endpoint: str = ""
        self.get_stock_endpoint: str = ""

    def init_app(self, app):
        with app.app_context():
            self.base_uri = app.config.get('BASE_URI')
            self.all_stocks_data_endpoint = app.config.get('ALL_STOCKS_DATA_ENDPOINT')
            self.all_brokers_data_endpoint = app.config.get('ALL_BROKERS_DATA_ENDPOINT')
            self.exchange_data_endpoint = app.config.get('EXCHANGE_DATA_ENDPOINT')
            self.messages_data_endpoint = app.config.get('MESSAGES_DATA_ENDPOINT')
            self.tickets_data_endpoint = app.config.get('TICKETS_DATA_ENDPOINT')
            self.affiliate_data_endpoint = app.config.get('AFFILIATE_DATA_ENDPOINT')
            self.user_data_endpoint = app.config.get('USER_DATA_ENDPOINT')
            self.membership_data_endpoint = app.config.get('MEMBERSHIP_DATA_ENDPOINT')
            self.api_data_endpoint = app.config.get('API_DATA_ENDPOINT')
            self.scrapper_data_endpoint = app.config.get('SCRAPPER_DATA_ENDPOINT')
            self.get_exchange_endpoint = app.config.get('GET_EXCHANGE_DATA_ENDPOINT')
            self.get_broker_endpoint = app.config.get('GET_BROKER_ENDPOINT')
            self.get_stock_endpoint = app.config.get('GET_STOCK_ENDPOINT')
        return self

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
            response_data: dict = response.json()
            if response.ok:
                return jsonify({'status': True, 'message': response_data['message'], 'payload': response_data['payload']}), 200
            return jsonify({'status': False, 'message': response_data['message']}), 500
        except ConnectionError as e:
            return jsonify({'status': False, 'message': e}), 200

    def fetch_exchanges(self) -> tuple:
        url: str = self._build_url(endpoint='exchange')
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

