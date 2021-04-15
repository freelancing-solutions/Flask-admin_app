import pandas as pd
from flask import Blueprint, jsonify, request
from ..api.sender import APISender

uploads_bp = Blueprint('uploads', __name__)


@uploads_bp.route('/uploads/<path:path>', methods=['GET', 'POST'])
def uploads(path: str) -> tuple:
    data_service_api: APISender = APISender()
    if path == "broker":
        """ broker file is uploaded"""
        f = request.files['file']
        if f.filename.endswith('csv'):
            data_frame = pd.read_csv(f, names=['broker_id', 'broker_code', 'broker_name'])
            brokers_data = data_frame.values.tolist()
            for broker in brokers_data[1:]:
                data: dict = {
                    "broker_id": broker[0],
                    "broker_code": broker[1],
                    "broker_name": broker[2]
                }
                data_service_api.send_broker(broker=data)

            return jsonify({'status': True, 'message': 'successfully uploaded'}), 200
        else:
            return jsonify({'status': False, 'message': 'please upload csv file'}), 500
    elif path == "stock":
        """ stock file is being uploaded"""
        f = request.files['file']
        if f.filename.endswith('csv'):
            data_frame = pd.read_csv(f, names=['stock_id', 'stock_code', 'stock_name', 'symbol'])
            stock_list: list = data_frame.DataFrame.values.tolist()
            for stock in stock_list:
                data: dict = {
                    'stock_id': stock[0],
                    'stock_code': stock[1],
                    'stock_name': stock[2],
                    'symbol': stock[3]
                }
                data_service_api.send_stock(stock=data)
            return jsonify({'status': True, 'message': 'successfully uploaded'}), 200
        else:
            return jsonify({'status': False, 'message': 'please upload csv file'}), 500
    elif path == "user":
        """ user image is being uploaded"""
        f = request.files['file']
        json_data = request.get_json()

        if f.filename.endswith('png') or f.filename.endswith('jpg') or f.filename.endswith('jpeg'):
            image_data = f.read()
            #TODO-  send the image to user database, json_data will contain the information
            # for the user being updated
        return jsonify({'status': True, 'message': 'successfully uploaded'}), 200
    elif path == "tickets":
        """ files related to support tickets are being uploaded"""
        f = request.files['file']
        if f.filename.endswith('png') or f.filename.endswith('jpg') or f.filename.endswith('jpeg') or f.filename.endswith('pdf'):
            file_data = f.read()
            #TODO - sends the filedata to data-service

        return jsonify({'status': True, 'message': 'successfully uploaded'}), 200
    elif path == "messages":
        """ files """
        pass
