import pandas as pd
from flask import Blueprint, jsonify, request
from ..api.sender import APISender

uploads_bp = Blueprint('uploads', __name__)


@uploads_bp.route('/uploads/<path:path>', methods=['GET', 'POST'])
def uploads(path):
    if path == "broker":
        """ broker file is uploaded"""
        data_service_api: APISender = APISender()
        f = request.files['file']
        if f.filename.endswith('csv'):
            data_frame = pd.read_csv(f, names=['broker_code', 'broker_name'])
            print("Printing List")
            brokers_data = data_frame.values.tolist()
            for broker in brokers_data[1:]:
                data: dict = {
                    "broker_code": broker[0],
                    "broker_name": broker[1]
                }
                print(data)
                data_service_api.send_broker(broker=data)
            # TODO sends data to data-service
            return jsonify({'status': True, 'message': 'successfully uploaded'}), 200
        else:
            return jsonify({'status': False, 'message': 'please upload csv file'}), 500
    elif path == "stock":
        """ stock file is being uploaded"""
        f = request.files['file']
        if f.filename.endswith('csv'):
            data_frame = pd.read_csv(f, names=['broker_code', 'broker_name'])
            print("Printing List")
            print(data_frame.DataFrame.values.tolist())
            # TODO sends data to data-service
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
