import pandas as pd
from flask import Blueprint, jsonify, request, current_app
from admin_app.main import api_sender

uploads_bp = Blueprint('uploads', __name__)
raw_dataframe = ["id", "stock_id", "broker_id", "stock_code", "stock_name", "broker_code",
                 "date", "buy_volume", "buy_value", "buy_ave_price", "buy_market_val_percent",
                 "buy_trade_count", "sell_volume", "sell_value", "sell_ave_price", "sell_market_val_percent",
                 "sell_trade_count", "net_volume", "net_value", "total_volume", "total_value"]


def compile_scrapped_data(stock) -> dict:
    data: dict = {
        "id": stock[0],
        "stock_id": stock[1],
        "broker_id": stock[2],
        "stock_code": stock[3],
        "stock_name": stock[4],
        "broker_code": stock[5],
        "date": stock[6],
        "buy_volume": stock[7],
        "buy_value": stock[8],
        "buy_ave_price": stock[9],
        "buy_market_val_percent": stock[10],
        "buy_trade_count": stock[11],
        "sell_volume": stock[12],
        "sell_value": stock[13],
        "sell_ave_price": stock[14],
        "sell_market_val_percent": stock[15],
        "sell_trade_count": stock[16],
        "net_volume": stock[17],
        "net_value": stock[18],
        "total_volume": stock[19],
        "total_value": stock[20]
    }

    return data


@uploads_bp.route('/uploads/<path:path>', methods=['GET', 'POST'])
def uploads(path: str) -> tuple:
    if path == "scrapped":
        f = request.files['file']
        data_frame = pd.read_csv(f, names=raw_dataframe)
        stock_data = data_frame.values.tolist()
        for stock in stock_data[1:]:
            try:
                data = compile_scrapped_data(stock=stock)
                api_sender.send_scrapper(scrapper=data)
            except Exception:
                pass

        return jsonify({'status': False, 'message': 'successfully sent scrapped data'}), 200

    elif path == "broker":
        """ broker file is uploaded"""
        f = request.files['file']
        if f.filename.endswith('csv'):
            data_frame = pd.read_csv(f, names=['broker_id', 'broker_code', 'broker_name'])
            brokers_data = data_frame.values.tolist()
            print("broker data : {}".format(brokers_data))
            for broker in brokers_data[1:]:
                try:
                    data: dict = {
                        "broker_id": broker[0],
                        "broker_code": broker[1],
                        "broker_name": broker[2]
                    }
                    api_sender.send_broker(broker=data)
                except IndexError:
                    jsonify({'status': False, 'message': 'please check your csv file format'}), 500
            return jsonify({'status': True, 'message': 'successfully uploaded'}), 200
        else:
            return jsonify({'status': False, 'message': 'please upload csv file'}), 500
    elif path == "stock":
        """ stock file is being uploaded"""
        f = request.files['file']
        if f.filename.endswith('csv'):
            data_frame = pd.read_csv(f, names=['stock_id', 'stock_code', 'stock_name', 'symbol'])
            stock_list: list = data_frame.values.tolist()
            for stock in stock_list[1:]:
                try:
                    data: dict = {
                        'stock_id': stock[0],
                        'stock_code': stock[1],
                        'stock_name': stock[2],
                        'symbol': stock[3]
                    }
                    api_sender.send_stock(stock=data)
                except IndexError:
                    jsonify({'status': False, 'message': 'please check your csv file format'}), 500
            return jsonify({'status': True, 'message': 'successfully uploaded'}), 200
        else:
            return jsonify({'status': False, 'message': 'please upload csv file'}), 500
    elif path == "user":
        """ user image is being uploaded"""
        f = request.files['file']
        json_data = request.get_json()

        if f.filename.endswith('png') or f.filename.endswith('jpg') or f.filename.endswith('jpeg'):
            image_data = f.read()
            # TODO-  send the image to user database, json_data will contain the information
            # for the user being updated
        return jsonify({'status': True, 'message': 'successfully uploaded'}), 200
    elif path == "tickets":
        """ files related to support tickets are being uploaded"""
        f = request.files['file']
        if f.filename.endswith('png') or f.filename.endswith('jpg') or f.filename.endswith(
                'jpeg') or f.filename.endswith('pdf'):
            file_data = f.read()
            # TODO - sends the filedata to data-service

        return jsonify({'status': True, 'message': 'successfully uploaded'}), 200
    elif path == "messages":
        """ files """
        pass
