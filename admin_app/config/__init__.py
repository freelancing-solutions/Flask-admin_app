import os
from decouple import config
from flask import request


# noinspection PyUnusedLocal
def only_cache_get(*args, **kwargs):
    return False if request.method == "GET" else True


# noinspection PyUnusedLocal
def only_cache_post(*args, **kwargs):
    return False if request.method == "POST" else True


class Config:
    """
        CONFIGURATION SETTINGS FOR ADMIN CONSOLE
    """

    def __init__(self):
        pass

    BASE_URI: str = config('base_uri') or os.getenv('base_uri')
    ALL_STOCKS_DATA_ENDPOINT: str = os.getenv('all_stocks_data_endpoint') or config('all_stocks_data_endpoint')
    ALL_BROKERS_DATA_ENDPOINT: str = os.getenv('all_brokers_data_endpoint') or config('all_brokers_data_endpoint')
    EXCHANGE_DATA_ENDPOINT: str = os.getenv('exchange_data_endpoint') or config('exchange_data_endpoint')
    MESSAGES_DATA_ENDPOINT: str = os.getenv('messages_data_endpoint') or config('messages_data_endpoint')
    TICKETS_DATA_ENDPOINT: str = os.getenv('tickets_data_endpoint') or config('tickets_data_endpoint')
    AFFILIATE_DATA_ENDPOINT: str = os.getenv('affiliate_data_endpoint') or config('affiliate_data_endpoint')
    USER_DATA_ENDPOINT: str = os.getenv('user_data_endpoint') or config('user_data_endpoint')
    MEMBERSHIP_DATA_ENDPOINT: str = os.getenv('membership_data_endpoint') or config('membership_data_endpoint')
    GET_MEMBERSHIP_PLANS_ENDPOINT: str = os.getenv('get_membership_plans_endpoint') or config('get_membership_plans_endpoint')
    API_DATA_ENDPOINT: str = os.getenv('api_data_endpoint') or config('api_data_endpoint')
    SCRAPPER_DATA_ENDPOINT: str = os.getenv('scrapper_data_endpoint') or config('scrapper_data_endpoint')

    GET_EXCHANGE_DATA_ENDPOINT: str = os.getenv('get_exchange_endpoint') or config('get_exchange_endpoint')
    GET_BROKER_ENDPOINT: str = os.getenv('get_broker_endpoint') or config('get_broker_endpoint')
    GET_STOCK_ENDPOINT: str = os.getenv('get_stock_endpoint') or config('get_stock_endpoint')

    # sender settings
    SEND_STOCK_DATA_ENDPOINT: str = os.getenv('send_stock_data_endpoint') or config('send_stock_data_endpoint')
    SEND_BROKER_DATA_ENDPOINT: str = os.getenv('send_broker_data_endpoint') or config('send_broker_data_endpoint')
    SEND_ADD_EXCHANGE_DATA_ENDPOINT = os.getenv('send_add_exchange_data_endpoint') or config('send_add_exchange_data_endpoint')
    SEND_SCRAPPER_SETTINGS = os.getenv('send_scrapping_settings') or config('send_scrapping_settings')
    SEND_MESSAGES_DATA_ENDPOINT: str = os.getenv('send_messages_data_endpoint') or config('send_messages_data_endpoint')
    SEND_TICKETS_DATA_ENDPOINT: str = os.getenv('send_tickets_data_endpoint') or config('send_tickets_data_endpoint')
    SEND_AFFILIATE_DATA_ENDPOINT: str = os.getenv('send_affiliate_data_endpoint') or config('send_affiliate_data_endpoint')
    SEND_USER_DATA_ENDPOINT: str = os.getenv('send_user_data_endpoint') or config('send_user_data_endpoint')
    SEND_MEMBERSHIP_DATA_ENDPOINT: str = os.getenv('send_membership_data_endpoint') or config('send_membership_data_endpoint')
    SEND_MEMBERSHIP_PLAN_ENDPOINT: str = os.getenv('send_membership_plan_endpoint') or config('send_membership_plan_endpoint')
    SEND_API_DATA_ENDPOINT: str = os.getenv('send_api_data_endpoint') or config('send_api_data_endpoint')
    SEND_SCRAPPER_DATA_ENDPOINT: str = os.getenv('send_scrapper_data_endpoint') or config('send_scrapper_data_endpoint')
    SEND_BUY_VOLUME_ENDPOINT: str = os.getenv("send_buy_volume_endpoint") or config("send_buy_volume_endpoint")
    SEND_SELL_VOLUME_ENDPOINT: str = os.getenv("send_sell_volume_endpoint") or config("send_sell_volume_endpoint")
    SEND_NET_VOLUME_ENDPOINT: str = os.getenv("send_net_volume_endpoint") or config("send_net_volume_endpoint")

    SECRET: str = os.getenv('secret') or config('secret')
    PROJECT: str = os.getenv('project') or config('project')

    CACHE_DEFAULT_TIMEOUT: int = os.getenv('cache_default_timeout') or config('cache_default_timeout')
    CACHE_TYPE: str = os.getenv('cache_type') or config('cache_type')
