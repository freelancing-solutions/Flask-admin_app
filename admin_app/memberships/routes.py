import json
import typing
from flask import Blueprint, request, render_template, jsonify, flash
from admin_app.main import api_sender, api_fetcher

memberships_bp = Blueprint('memberships', __name__)


@memberships_bp.route('/membership-plans', methods=["GET", "POST"])
def membership_plans() -> tuple:
    if request.method == "GET":
        response, status = api_fetcher.get_all_membership_plans()
        try:
            response_json: dict = response.get_json()
            message: str = response_json['message']
            state: bool = response_json['status']
            if state:
                membership_plans_list: typing.List[dict] = response_json['payload']
            else:
                membership_plans_list: typing.List[dict] = []
        except Exception as e:
            message: str = str(e)
            membership_plans_list: typing.List[dict] = []
        flash(message=message)
        return render_template('memberships/membership_plans.html', membership_plans=membership_plans_list), status


@memberships_bp.route('/create-membership-plan', methods=['GET', 'POST'])
def create_membership_plan() -> tuple:
    import asyncio
    if request.method == "GET":
        return render_template('memberships/create_plans.html'), 200
    elif request.method == "POST":
        return asyncio.new_event_loop().run_until_complete(api_sender.send_membership_plans(
            membership_plan=request.get_json()))
