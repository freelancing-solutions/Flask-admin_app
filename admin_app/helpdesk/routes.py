from flask import Blueprint, render_template, url_for, current_app

from admin_app.config import only_cache_get
from admin_app.main import route_cache, cache_timeout

helpdesk_bp = Blueprint('helpdesk', __name__)


@helpdesk_bp.route('/helpdesk/<path:path>', methods=['POST', 'GET'])
@route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def helpdesk(path):
    if path == "messages":
        return render_template('helpdesk/messages.html')
    elif path == "tickets":
        return render_template('helpdesk/tickets.html')