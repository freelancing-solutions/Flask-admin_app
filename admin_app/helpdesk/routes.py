from flask import Blueprint, render_template, url_for
helpdesk_bp = Blueprint('helpdesk', __name__)


@helpdesk_bp.route('/helpdesk/<path:path>', methods=['POST', 'GET'])
def helpdesk(path):
    if path == "messages":
        return render_template('helpdesk/messages.html')
    elif path == "tickets":
        return render_template('helpdesk/tickets.html')