import requests
from flask import jsonify, current_app
from flask_caching import Cache
from requests import ReadTimeout, TooManyRedirects
from requests.exceptions import ConnectionError, ConnectTimeout, SSLError, HTTPError

# noinspection PyAttributeOutsideInit
class APISender:
    """
        send data to data-service
    """
    # 6 Hours
    long_cache_timeout: int = 60 * 60 * 6
    # short cache Timeout 10 minutes
    short_cache_timeout: int = 60 * 10
    cache: Cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})

    def __init__(self):
        self.base_uri: str = ""
        self.send_stock_data_endpoint: str = ""
        self.send_broker_data_endpoint: str = ""
        self.send_add_exchange_data_endpoint: str = ""
        self.send_messages_data_endpoint: str = ""
        self.send_tickets_data_endpoint: str = ""
        self.send_affiliate_data_endpoint: str = ""
        self.send_user_data_endpoint: str = ""
        self.send_membership_data_endpoint: str = ""
        self.send_membership_plan_endpoint: str = ""
        self.send_api_data_endpoint: str = ""
        self.send_scrapper_data_endpoint: str = ""
        self.send_scrapper_scrapping_settings: str = ""
        self.send_buy_volume_endpoint: str = ""
        self.send_sell_volume_endpoint: str = ""
        self.send_net_volume_endpoint: str = ""
        self.headers = {}

    def init_app(self, app):
        with app.app_context():
            self.base_uri = app.config.get("BASE_URI")
            self.send_stock_data_endpoint = app.config.get("SEND_STOCK_DATA_ENDPOINT")
            self.send_broker_data_endpoint = app.config.get("SEND_BROKER_DATA_ENDPOINT")
            self.send_scrapper_scrapping_settings = app.config.get("SEND_SCRAPPER_SETTINGS")
            self.send_add_exchange_data_endpoint = app.config.get("SEND_ADD_EXCHANGE_DATA_ENDPOINT")
            self.send_messages_data_endpoint = app.config.get("SEND_MESSAGES_DATA_ENDPOINT")
            self.send_tickets_data_endpoint = app.config.get("SEND_TICKETS_DATA_ENDPOINT")
            self.send_affiliate_data_endpoint = app.config.get("SEND_AFFILIATE_DATA_ENDPOINT")
            self.send_user_data_endpoint = app.config.get("SEND_USER_DATA_ENDPOINT")
            self.send_membership_data_endpoint = app.config.get("SEND_MEMBERSHIP_DATA_ENDPOINT")
            self.send_membership_plan_endpoint = app.config.get("SEND_MEMBERSHIP_PLAN_ENDPOINT")
            self.send_api_data_endpoint = app.config.get("SEND_API_DATA_ENDPOINT")
            self.send_scrapper_data_endpoint = app.config.get("SEND_SCRAPPER_DATA_ENDPOINT")
            self.send_buy_volume_endpoint: str = app.config.get("SEND_BUY_VOLUME_ENDPOINT")
            self.send_sell_volume_endpoint: str = app.config.get("SEND_SELL_VOLUME_ENDPOINT")
            self.send_net_volume_endpoint: str = app.config.get("SEND_NET_VOLUME_ENDPOINT")

            # initializing cache
            x_project_name: str = app.config.get('PROJECT') + ".admin"
            self.headers: dict = {'user-agent': 'admin-app',
                                  'X-PROJECT-NAME': x_project_name,
                                  'Content-type': 'application/json',
                                  'mode': 'cors',
                                  'x-auth-token': app.config.get('SECRET')}

            print(self.headers)
            self.cache.init_app(app, config={'CACHE_TYPE': 'simple'})

        return self

    # @cache.memoize(timeout=long_cache_timeout)
    def _build_url(self, endpoint: str) -> str:
        if endpoint == "stock":
            return self.base_uri + self.send_stock_data_endpoint
        elif endpoint == "broker":
            return self.base_uri + self.send_broker_data_endpoint
        elif endpoint == "exchange":
            return self.base_uri + self.send_add_exchange_data_endpoint
        elif endpoint == "messages":
            return self.base_uri + self.send_messages_data_endpoint
        elif endpoint == "tickets":
            return self.base_uri + self.send_tickets_data_endpoint
        elif endpoint == "affiliate":
            return self.base_uri + self.send_affiliate_data_endpoint
        elif endpoint == "user":
            return self.base_uri + self.send_user_data_endpoint
        elif endpoint == "membership":
            return self.base_uri + self.send_membership_data_endpoint
        elif endpoint == "membership-plan":
            return self.base_uri + self.send_membership_plan_endpoint
        elif endpoint == "api":
            return self.base_uri + self.send_api_data_endpoint
        elif endpoint == "scrapper":
            return self.base_uri + self.send_scrapper_data_endpoint
        elif endpoint == "scrapping-settings":
            return self.base_uri + self.send_scrapper_scrapping_settings
        elif endpoint == "buy-volume":
            return self.base_uri + self.send_buy_volume_endpoint
        elif endpoint == "sell-volume":
            return self.base_uri + self.send_sell_volume_endpoint
        elif endpoint == "net-volume":
            return self.base_uri + self.send_net_volume_endpoint
        else:
            return ""

    def _requester(self, url: str, data: dict) -> tuple:
        try:
            response = requests.post(url=url, json=data, headers=self.headers)
            response.raise_for_status()
            response_data: dict = response.json()
            return jsonify(response_data), 200

        except ConnectTimeout:
            return jsonify({'status': False, 'message': 'A time-out occurred while connecting to data-service'}), 500
        except ReadTimeout:
            return jsonify({'status': False, 'message': 'Error Reading Response, check data-service'}), 500
        except TooManyRedirects:
            return jsonify({'status': False, 'message': 'Too Many Redirects Probable Cause is DNS Settings'}), 500
        except SSLError:
            return jsonify({'status': False, 'message': 'Unable to connect using SSL'}), 500
        except ConnectionError:
            return jsonify({'status': False, 'message': 'Error connecting to data-service'}), 500
        except HTTPError:
            return jsonify({'status': False, 'message': 'Well Something Snapped'}), 500

    def send_stock(self, stock: dict) -> tuple:
        """
            send stock data
        :param stock:
        :return:
        """
        print("Stock Data Received : {}".format(stock))
        url: str = self._build_url(endpoint="stock")
        response = self._requester(url=url, data=stock)
        return response

    def send_broker(self, broker: dict) -> tuple:
        """
            send broker data
        :param broker:
        :return:
        """
        print("broker data : {}".format(broker))

        url: str = self._build_url(endpoint="broker")
        response = self._requester(url=url, data=broker)
        return response

    def send_buy_volume(self, buy_volume: dict) -> tuple:
        print("buy volume data: {}".format(buy_volume))
        url: str = self._build_url(endpoint="buy-volume")
        response = self._requester(url=url, data=buy_volume)
        return response

    def send_sell_volume(self, sell_volume: dict) -> tuple:
        print("Sell volume data: {}".format(sell_volume))
        url: str = self._build_url(endpoint="sell-volume")
        response = self._requester(url=url, data=sell_volume)
        return response

    def send_net_volume(self, net_volume: dict) -> tuple:
        print("net volume data: {}".format(net_volume))
        url: str = self._build_url(endpoint="net-volume")
        response = self._requester(url=url, data=net_volume)
        return response

    def send_exchange(self, exchange: dict) -> tuple:
        """
            send exchange data
        :param exchange:
        :return:
        """
        url: str = self._build_url(endpoint="exchange")
        return self._requester(url=url, data=exchange)

    def send_messages(self, messages: dict) -> tuple:
        """
            send messages
        :param messages:
        :return:
        """
        url: str = self._build_url(endpoint="messages")
        return self._requester(url=url, data=messages)

    def send_tickets(self, ticket: dict) -> tuple:
        """
            send ticket data
        :param ticket:
        :return:
        """
        url: str = self._build_url(endpoint="tickets")
        return self._requester(url=url, data=ticket)

    def send_affiliate(self, affiliate_data: dict) -> tuple:
        """
            send affiliate data
        :param affiliate_data:
        :return:
        """
        url: str = self._build_url(endpoint="affiliate")
        return self._requester(url=url, data=affiliate_data)

    def send_user(self, user: dict) -> tuple:
        """
            send user data
        :param user:
        :return:
        """
        url: str = self._build_url(endpoint="user")
        return self._requester(url=url, data=user)

    def send_memberships(self, memberships: dict) -> tuple:
        """
            send subscriptions data
        :param memberships:
        :param subscriptions:
        :return:
        """
        url: str = self._build_url(endpoint="memberships")
        return self._requester(url=url, data=memberships)

    def send_membership_plans(self, membership_plan: dict) -> tuple:
        url: str = self._build_url(endpoint='membership-plan')
        return self._requester(url=url, data=membership_plan)

    def send_api(self, api: dict) -> tuple:
        """
            send api data
        :param api:
        :return:
        """
        url: str = self._build_url(endpoint="memberships")
        return self._requester(url=url, data=api)

    def send_scrapper(self, scrapper: dict) -> tuple:
        """
            send scrapping service
        :param scrapper:
        :return:
        """
        url: str = self._build_url(endpoint="scrapper")
        print("Scrapper URL : {}".format(url))
        return self._requester(url=url, data=scrapper)

    def send_scrapping_settings(self, settings_data: dict) -> tuple:

        url: str = self._build_url(endpoint="scrapping-settings")
        return self._requester(url=url, data=settings_data)