from flask import Flask, jsonify, Response
from main import *

app = Flask(__name__)
player_car = None
success_response = Response("success", status=200)

@app.route('/boost', methods=['POST'])
def trigger_boost():
    boost(veh=player_car)
    return success_response


@app.route('/break', methods=['POST'])
def trigger_break():
    parking_break(veh=player_car)
    return success_response


@app.route('/kaputt', methods=['POST'])
def trigger_kaputt():
    break_breakgroups(veh=player_car)
    return success_response


@app.route('/explode', methods=['POST'])
def trigger_explode():
    explode(veh=player_car)
    return success_response


@app.route('/reset', methods=['POST'])
def trigger_reset():
    reset(veh=player_car, bng=bng)
    return success_response


if __name__ == '__main__':
    bng.open(launch=False)
    player_car = get_player_vehicle(bng)
    app.run(port=5000)

