from flask import Flask, request, send_file
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getRisk')
def get_location_risk():  # put application's code here
    latitude = None
    longitude = None
    if "lat" in request.args.keys():
        latitude = request.args["lat"]
    if "long" in request.args.keys():
        longitude = request.args["long"]
    if latitude is not None and longitude is not None and os.path.exists(f"./static/{latitude}_{longitude}.json"):
        return send_file(f"./static/{latitude}_{longitude}.json")
    return {"save_spot": "unknown", "advise": "retry later"}


@app.route('/getSaveSpot')
def get_next_save_spot():
    latitude = None
    longitude = None
    if "lat" in request.args.keys():
        latitude = request.args["lat"]
    if "long" in request.args.keys():
        longitude = request.args["long"]
    if latitude is not None and longitude is not None and os.path.exists(f"./static/save_spot_{latitude}_{longitude}.json"):
        return send_file(f"./static/save_spot_{latitude}_{longitude}.json")
    return {"latitude": 0.0, "longitude": 0.0}


@app.route('/getStatus')
def get_status():
    name = None
    if "name" in request.args.keys():
        name = request.args["name"]
    if name is not None and os.path.exists(f"./static/status_{name}.json"):
        return send_file(f"./static/status_{name}.json")
    return {"latitude": 0.0, "longitude": 0.0}


if __name__ == '__main__':
    app.run()
