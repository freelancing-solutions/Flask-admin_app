import os
from decouple import config


class Config:
    base_uri = os.getenv('base_uri') or config('base_uri')
    all_stocks_data_endpoint = os.getenv('all_stocks_data_endpoint') or config('all_stocks_data_endpoint')
    all_brokers_data_endpoint = os.getenv('all_brokers_data_endpoint') or config('all_brokers_data_endpoint')
    exchange_data_endpoint = os.getenv('exchange_data_endpoint') or config('exchange_data_endpoint')
    messages_data_endpoint = os.getenv('messages_data_endpoint') or config('messages_data_endpoint')
    tickets_data_endpoint = os.getenv('tickets_data_endpoint') or config('tickets_data_endpoint')
    affiliate_data_endpoint = os.getenv('affiliate_data_endpoint') or config('affiliate_data_endpoint')
    user_data_endpoint = os.getenv('user_data_endpoint') or config('user_data_endpoint')
    membership_data_endpoint = os.getenv('membership_data_endpoint') or config('membership_data_endpoint')
    api_data_endpoint = os.getenv('api_data_endpoint') or config('api_data_endpoint')
    scrapper_data_endpoint = os.getenv('scrapper_data_endpoint') or config('scrapper_data_endpoint')
    get_exchange_endpoint = os.getenv('get_exchange_endpoint') or config('get_exchange_endpoint')
    get_broker_endpoint = os.getenv('get_broker_endpoint') or config('get_broker_endpoint')
    get_stock_endpoint = os.getenv('get_stock_endpoint') or config('get_stock_endpoint')

    stock_data_endpoint = os.getenv('stock_data_endpoint') or config('stock_data_endpoint')
    broker_data_endpoint = os.getenv('broker_data_endpoint') or config('broker_data_endpoint')
    add_exchange_data_endpoint = os.getenv('add_exchange_data_endpoint') or config('add_exchange_data_endpoint')
    # TODO - Finish this and resolve conflicts
