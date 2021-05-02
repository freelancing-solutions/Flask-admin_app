import typing
from flask import Blueprint, jsonify, request, current_app, render_template
from admin_app.main import api_sender, api_fetcher

memberships_bp = Blueprint('memberships', __name__)

@memberships_bp.route('/membership-plans', methods=["GET", "POST"])
def membership_plans() -> tuple:
    if request.method == "GET":
        # TODO fetch membership plans from data-store
        response = api_fetcher.get_all_membership_plans()
        try:
            status, payload, message = response
            membership_plans_list: typing.List[dict] = payload
        except Exception:
            status, message = response
            membership_plans_list: typing.List[dict] = []

        return render_template('memberships/membership_plans.html',  membership_plans=membership_plans_list)


@memberships_bp.route('/create-membership_plan', methods=['GET', 'POST'])
def create_membership_plan() -> tuple:
    if request.method == "GET":
        return render_template('memberships/create_plans.html')
    elif request.method == "POST":
        membership_plan_data: dict = request.get_json()
        return api_sender.send_membership_plans(membership_plan=membership_plan_data)