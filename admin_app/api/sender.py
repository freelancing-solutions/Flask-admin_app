from functools import lru_cache
from aiohttp import ClientConnectorError
from flask import jsonify
from flask_caching import Cache
from requests import ReadTimeout, TooManyRedirects
from requests.exceptions import ConnectionError, ConnectTimeout, SSLError, HTTPError
import aiohttp


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
        self.headers = {}

    def init_app(self, app):
        with app.app_context():
            self.base_uri = app.config.get("BASE_URI")
            self._url_look_up: dict = {
                "stock": app.config.get("SEND_STOCK_DATA_ENDPOINT"),
                "broker": app.config.get("SEND_BROKER_DATA_ENDPOINT"),
                "exchange": app.config.get("SEND_ADD_EXCHANGE_DATA_ENDPOINT"),
                "messages": app.config.get("SEND_MESSAGES_DATA_ENDPOINT"),
                "tickets": app.config.get("SEND_TICKETS_DATA_ENDPOINT"),
                "affiliate": app.config.get("SEND_AFFILIATE_DATA_ENDPOINT"),
                "user": app.config.get("SEND_USER_DATA_ENDPOINT"),
                "membership": app.config.get("SEND_MEMBERSHIP_DATA_ENDPOINT"),
                "membership_plan": app.config.get("SEND_MEMBERSHIP_PLAN_ENDPOINT"),
                "api": app.config.get("SEND_API_DATA_ENDPOINT"),
                "scrapper": app.config.get("SEND_SCRAPPER_DATA_ENDPOINT"),
                "scrapping-settings": app.config.get("SEND_SCRAPPER_SETTINGS"),
                "buy-volume": app.config.get("SEND_BUY_VOLUME_ENDPOINT"),
                "sell-volume": app.config.get("SEND_SELL_VOLUME_ENDPOINT"),
                "net-volume": app.config.get("SEND_NET_VOLUME_ENDPOINT")
            }
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

    @lru_cache(maxsize=1024)
    def _build_url(self, endpoint: str) -> str:
        return "{}{}".format(self.base_uri, self._url_look_up[endpoint])

    async def _requester(self, url: str, data: dict) -> tuple:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, json=data, headers=self.headers) as response:
                    response_data: dict = await response.json()
                    return jsonify(response_data), 200
        except ClientConnectorError:
            return jsonify({'status': False, 'message': 'A time-out occurred while connecting to data-service'}), 500
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

    async def send_stock(self, stock: dict) -> tuple:
        """
            send stock data
        :param stock:
        :return:
        """
        url: str = self._build_url(endpoint="stock")
        return await self._requester(url=url, data=stock)

    async def send_broker(self, broker: dict) -> tuple:
        """
            send broker data
        :param broker:
        :return:
        """
        url: str = self._build_url(endpoint="broker")
        return await self._requester(url=url, data=broker)

    async def send_buy_volume(self, buy_volume: dict) -> tuple:
        url: str = self._build_url(endpoint="buy-volume")
        return await self._requester(url=url, data=buy_volume)

    async def send_sell_volume(self, sell_volume: dict) -> tuple:
        url: str = self._build_url(endpoint="sell-volume")
        return await self._requester(url=url, data=sell_volume)

    async def send_net_volume(self, net_volume: dict) -> tuple:
        url: str = self._build_url(endpoint="net-volume")
        return await self._requester(url=url, data=net_volume)

    async def send_exchange(self, exchange: dict) -> tuple:
        """
            send exchange data
        :param exchange:
        :return:
        """
        url: str = self._build_url(endpoint="exchange")
        return await self._requester(url=url, data=exchange)

    async def send_messages(self, messages: dict) -> tuple:
        """
            send messages
        :param messages:
        :return:
        """
        url: str = self._build_url(endpoint="messages")
        return await self._requester(url=url, data=messages)

    async def send_tickets(self, ticket: dict) -> tuple:
        """
            send ticket data
            :param ticket:
            :return:
        """
        url: str = self._build_url(endpoint="tickets")
        return await self._requester(url=url, data=ticket)

    async def send_affiliate(self, affiliate_data: dict) -> tuple:
        """
            send affiliate data
        :param affiliate_data:
        :return:
        """
        url: str = self._build_url(endpoint="affiliate")
        return await self._requester(url=url, data=affiliate_data)

    async def send_user(self, user: dict) -> tuple:
        """
            send user data
        :param user:
        :return:
        """
        url: str = self._build_url(endpoint="user")
        return await self._requester(url=url, data=user)

    async def send_memberships(self, memberships: dict) -> tuple:
        """
            send subscriptions data
        :param memberships:
        :return:
        """
        url: str = self._build_url(endpoint="memberships")
        return await self._requester(url=url, data=memberships)

    async def send_membership_plans(self, membership_plan: dict) -> tuple:
        url: str = self._build_url(endpoint='membership-plan')
        return await self._requester(url=url, data=membership_plan)

    async def send_api(self, api: dict) -> tuple:
        """
            send api data
        :param api:
        :return:
        """
        url: str = self._build_url(endpoint="memberships")
        return await self._requester(url=url, data=api)

    async def send_scrapper(self, scrapper: dict) -> tuple:
        """
            send scrapping service
        :param scrapper:
        :return:
        """
        url: str = self._build_url(endpoint="scrapper")
        print("Scrapper URL : {}".format(url))
        return await self._requester(url=url, data=scrapper)

    async def send_scrapping_settings(self, settings_data: dict) -> tuple:

        url: str = self._build_url(endpoint="scrapping-settings")
        return await self._requester(url=url, data=settings_data)