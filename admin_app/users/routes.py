import typing
from flask import Blueprint, render_template, request, flash, get_flashed_messages
from admin_app.config import only_cache_get
from admin_app.main import route_cache, cache_timeout, api_fetcher
users_bp = Blueprint('users', __name__)


def return_user_by_uid(uid: str, users_list: typing.List[dict]) -> typing.Union[dict, None]:
    for user_data in users_list:
        if user_data.uid == uid:
            return user_data
    return None


def return_plan_by_plan_id(plan_id: str, membership_plans: typing.List[dict]) -> typing.Union[dict, None]:
    for member_data in membership_plans:
        if member_data.plan_id == plan_id:
            return member_data
    return None


@users_bp.route('/users/<path:path>', methods=["GET", "POST"])
@route_cache.cached(timeout=cache_timeout, unless=only_cache_get)
def users(path: str) -> tuple:
    get_flashed_messages()
    if request.method == "GET":
        if path == "users":
            response, status = api_fetcher.fetch_all_users()
            response_data: dict = response.get_json()
            message: str = response_data['message']
            if response_data['status']:
                users_list: typing.List[dict] = response_data['payload']
            else:
                flash(message=message)
                users_list: typing.List[dict] = []
            print(users_list)
            return render_template('users/users.html', users=users_list), 200
        elif path == "messages":
            return render_template('users/messages.html'), 200

        elif path == "subscriptions":
            response, status = api_fetcher.fetch_memberships()
            response_data: dict = response.get_json()
            message: str = response_data['message']
            if response_data['status']:
                members_list: typing.List[dict] = response_data['payload']
            else:
                flash(message=message)
                members_list: typing.List[dict] = []

            response, status = api_fetcher.get_all_membership_plans()
            response_data: dict = response.get_json()
            visual_data: typing.List[dict] = []

            if response_data['status']:
                membership_plans: typing.List[dict] = response_data['payload']
                response, status = api_fetcher.fetch_all_users()
                response_data: dict = response.get_json()
                users_data: typing.List[dict] = response_data['payload']

                for member in members_list:
                    user_data = return_user_by_uid(uid=member.uid, users_list=users_data)
                    plan_data = return_plan_by_plan_id(plan_id=member.plan_id, membership_plans=membership_plans)
                    if user is not None:
                        visual_data.append({
                            'status': member['status'],
                            'date_created': member['date_created'],
                            'plan_start_date': member['plan_start_date'],
                            'payment_method': member['payment_method'],
                            'user': user_data,
                            'plan': plan_data
                        })
            return render_template('users/subscriptions.html', members_list=visual_data), 200


@users_bp.route('/user/<path:uid>', methods=["GET", "POST"])
def user(uid: str) -> tuple:
    get_flashed_messages()
    if request.method == "GET":
        response, status = api_fetcher.fetch_user(uid=uid)
        response_data: dict = response.get_json()
        message: str = response_data['message']

        if response_data['status']:
            user_data: dict = response_data['payload']
            return render_template('users/user.html', user=user_data), 200
        else:
            flash(message=message)
            return render_template('users/user.html'), 500

    elif request.method == "PUT":
        # TODO - update user
        user_data: dict = request.get_json()
        return api_fetcher.update_user(user_data=user_data)
