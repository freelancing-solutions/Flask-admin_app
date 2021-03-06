import typing

from flask import Blueprint, render_template
from admin_app.config import only_cache_get
from admin_app.main import route_cache, cache_timeout, api_fetcher

helpdesk_bp = Blueprint('helpdesk', __name__)


@helpdesk_bp.route('/helpdesk/<path:path>', methods=['POST', 'GET'])
@route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def helpdesk(path) -> tuple:
    if path == "resolved":
        response, status = api_fetcher.fetch_resolved_tickets()
        response_data: dict = response.get_json()
        if response_data['status']:
            tickets_list: typing.List['dict'] = response_data['payload']
        else:
            tickets_list: typing.List['dict'] = []
        return render_template('helpdesk/tickets.html', tickets_list=tickets_list), 200
    if path == "unresolved":
        response, status = api_fetcher.fetch_unresolved_tickets()
        response_data: dict = response.get_json()
        if response_data['status']:
            tickets_list: typing.List['dict'] = response_data['payload']
        else:
            tickets_list: typing.List['dict'] = []
        return render_template('helpdesk/tickets.html', tickets_list=tickets_list), 200
    elif path == "tickets":
        response, status = api_fetcher.fetch_support_tickets()
        response_data: dict = response.get_json()
        if response_data['status']:
            tickets_list: typing.List['dict'] = response_data['payload']
        else:
            tickets_list: typing.List['dict'] = []
        return render_template('helpdesk/tickets.html', tickets_list=tickets_list), 200


@helpdesk_bp.route('/help-desk/ticket/<path:ticket_id>', methods=['POST', 'GET'])
def helpdesk_ticket(ticket_id: str) -> tuple:
    response, status = api_fetcher.fetch_ticket(ticket_id=ticket_id)
    response_data: dict = response.get_json()
    if response_data['status']:
        ticket_instance: typing.Union[dict, None] = response_data['payload']
    else:
        ticket_instance: typing.Union[dict, None] = None
    return render_template('helpdesk/ticket.html', ticket=ticket_instance), 200
