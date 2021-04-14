import requests
from flask import jsonify


class APISender:
    """
        send data to data-service
    """
    base_uri: str = "https://data-service.pinoydesk.com/"
    stock_data_endpoint: str = "api/v1/stocks/create/stock"
    broker_data_endpoint: str = "api/v1/stocks/create/broker"
    exchange_data_endpoint: str = "api/v1/exchange/add"
    messages_data_endpoint: str = "api/v1/messages/update"
    tickets_data_endpoint: str = "api/v1/tickets/update"
    affiliate_data_endpoint: str = "api/v1/affiliates/update"
    user_data_endpoint: str = "api/v1/user/update"
    membership_data_endpoint: str = "api/v1/membership/update"
    api_data_endpoint: str = "api/v1/api/add"
    scrapper_data_endpoint: str = "api/v1/scrapper/add"

    def __init__(self):
        pass

    def _build_url(self, endpoint: str) -> str:
        if endpoint == "stock":
            return self.base_uri + self.stock_data_endpoint
        elif endpoint == "broker":
            return self.base_uri + self.broker_data_endpoint
        elif endpoint == "exchange":
            return self.base_uri + self.exchange_data_endpoint
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

    def _requester(self, url: str, data: dict) -> tuple:
        try:
            response = requests.post(url=url, json=data)
            print(response.text)
            if response.ok:
                print("OK")
                return jsonify({'status': True, 'message': 'success'}), 200
            return jsonify({'status': True, 'message': 'success'}), 200
        except ConnectionError as e:
            return jsonify({'status': True, 'message': 'success'}), 200

    def send_stock(self, stock: dict) -> tuple:
        """
            send stock data
        :param stock:
        :return:
        """
        data = {"stock": stock}
        url = self._build_url(endpoint="stock")
        return self._requester(url=url, data=data)

    def send_broker(self, broker: dict) -> tuple:
        """
            send broker data
        :param broker:
        :return:
        """
        data = {"broker": broker}
        url = self._build_url(endpoint="broker")
        return self._requester(url=url, data=data)

    def send_exchange(self, exchange: dict) -> tuple:
        """
            send exchange data
        :param exchange:
        :return:
        """
        data = {"exchange": exchange}
        url = self._build_url(endpoint="exchange")
        return self._requester(url=url, data=data)

    def send_messages(self, messages: dict) -> tuple:
        """
            send messages
        :param messages:
        :return:
        """
        data = jsonify({"messages": messages})
        url = self._build_url(endpoint="messages")
        return self._requester(url=url, data=data)

    def send_tickets(self, ticket: dict) -> tuple:
        """
            send ticket data
        :param ticket:
        :return:
        """
        data = {'ticket': ticket}
        url = self._build_url(endpoint="tickets")
        return self._requester(url=url, data=data)

    def send_affiliate(self, affiliate_data: dict) -> tuple:
        """
            send affiliate data
        :param affiliate_data:
        :return:
        """
        data = {'affiliate': affiliate_data}
        url = self._build_url(endpoint="affiliate")
        return self._requester(url=url, data=data)

    def send_user(self, user: dict) -> tuple:
        """
            send user data
        :param user:
        :return:
        """
        data = {'user': user}
        url = self._build_url(endpoint="user")
        return self._requester(url=url, data=data)

    def send_memberships(self, memberships: dict) -> tuple:
        """
            send subscriptions data
        :param memberships:
        :param subscriptions:
        :return:
        """
        data = {'memberships': memberships}
        url = self._build_url(endpoint="memberships")
        return self._requester(url=url, data=data)

    def send_api(self, api: dict) -> tuple:
        """
            send api data
        :param api:
        :return:
        """
        data = {'api': api}
        url = self._build_url(endpoint="memberships")
        return self._requester(url=url, data=data)

    def send_scrapper(self, scrapper: dict) -> tuple:
        """
            send scrapping service
        :param scrapper:
        :return:
        """
        data = {'scrapper': scrapper}
        url = self._build_url(endpoint="scrapper")
        return self._requester(url=url, data=data)
