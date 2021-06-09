from functools import lru_cache
import requests
from flask import jsonify
from flask_caching import Cache
from requests import ReadTimeout, TooManyRedirects
from requests.exceptions import ConnectTimeout, SSLError, ConnectionError, HTTPError


# noinspection PyAttributeOutsideInit
class APIFetcher:
    # 6 Hours
    long_cache_timeout: int = 60*60*6
    # short cache Timeout 10 minutes
    short_cache_timeout: int = 60*10
    cache: Cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
    use_cache: bool = True
    headers: dict = {'user-agent': 'admin-app',
                     'project': '',
                     'Content-type': 'application/json',
                     'mode': 'cors',
                     'token': ''}
    _url_look_up: dict = {}

    def __int__(self):
        pass


    # noinspection DuplicatedCode
    def init_app(self, app):
        # TODO - initialize caching here for fetching data
        with app.app_context():
            self._url_look_up: dict = {
                "base-url": app.config.get('BASE_URI'),
                "stock": app.config.get('ALL_STOCKS_DATA_ENDPOINT'),
                "get-stock": app.config.get('GET_STOCK_ENDPOINT'),
                "broker": app.config.get('ALL_BROKERS_DATA_ENDPOINT'),
                "get-broker": app.config.get('GET_BROKER_ENDPOINT'),
                "exchange": app.config.get('EXCHANGE_DATA_ENDPOINT'),
                "get-exchange": app.config.get('GET_EXCHANGE_DATA_ENDPOINT'),
                "messages": app.config.get('MESSAGES_DATA_ENDPOINT'),
                "tickets": app.config.get('TICKETS_DATA_ENDPOINT'),
                "affiliates": app.config.get('AFFILIATE_DATA_ENDPOINT'),
                "user": app.config.get('USER_DATA_ENDPOINT'),
                "membership": app.config.get('MEMBERSHIP_DATA_ENDPOINT'),
                "membership-plans": app.config.get('GET_MEMBERSHIP_PLANS_ENDPOINT'),
                "api": app.config.get('API_DATA_ENDPOINT'),
                "scrapper": app.config.get('SCRAPPER_DATA_ENDPOINT')
            }

            self.headers.setdefault('project', app.config.get('PROJECT'))
            self.headers.setdefault('token', app.config.get('SECRET'))

            x_project_name: str = app.config.get('PROJECT') + ".admin"
            self.headers: dict = {'user-agent': 'admin-app',
                                  'X-PROJECT-NAME': x_project_name,
                                  'Content-type': 'application/json',
                                  'mode': 'cors',
                                  'x-auth-token': app.config.get('SECRET')}
            # initializing cache
            self.cache.init_app(app, config={'CACHE_TYPE': 'simple'})
        return self

    @lru_cache(maxsize=1024)
    def _build_url(self, endpoint: str) -> str:
        return "{}{}".format(self._url_look_up['base-url'], self._url_look_up[endpoint])

    @cache.memoize(timeout=short_cache_timeout)
    def _requester(self, url: str, data: dict = None) -> tuple:
        try:
            if data:
                response = requests.post(url=url, json=data, headers=self.headers)
            else:
                response = requests.post(url=url, headers=self.headers)
            response.raise_for_status()
            response_data: dict = response.json()
            return jsonify({'status': True, 'message': response_data['message'],
                            'payload': response_data['payload']}), 200

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

    def get_all_membership_plans(self) -> tuple:
        return self._requester(url=self._build_url(endpoint='membership-plans'), data=None)
