from flask import Blueprint, jsonify, request, current_app, render_template
from admin_app.main import api_sender

memberships_bp = Blueprint('memberships', __name__)

@memberships_bp.route('/membership-plans', methods=["GET", "POST"])
def membership_plans() -> tuple:
    if request.method == "GET":
        membership_plans = []
        return render_template('memberships/membership_plans.html',  membership_plans=membership_plans)
    elif request.method == "POST":
        membership_plan_data: dict = request.get_json()
        return api_sender.send_membership_plans(membership_plan=membership_plan_data)



