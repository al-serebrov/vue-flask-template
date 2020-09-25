import os

from autoria.api import RiaAPI, RiaAverageCarPrice
from flask import Flask, jsonify, request
from flask_cors import CORS
from copy import deepcopy

app = Flask(__name__)
# unsafe, all origins have access, should be limited to frontend
CORS(app)
ria_api = RiaAPI()
api_key = os.environ.get('API_KEY')


# a simple page that says hello
@app.route('/')
def hello():
    return "Hello World!"


@app.route('/categories')
def categories():
    return jsonify(ria_api.get_categories())


@app.route('/categories/<category_id>/bodystyles')
def bodystyles(category_id):
    return jsonify(ria_api.get_bodystyles(category_id))


@app.route('/categories/<category_id>/marks')
def marks(category_id):
    return jsonify(ria_api.get_marks(category_id))


@app.route('/categories/<category_id>/gearboxes')
def gearboxes(category_id):
    return jsonify(ria_api.get_gearboxes(category_id))


@app.route('/categories/<category_id>/driverTypes')
def driver_types(category_id):
    return jsonify(ria_api.get_driver_types(category_id))


@app.route('/categories/<category_id>')
def category_info(category_id):
    return jsonify({
        'bodystyles': ria_api.get_bodystyles(category_id),
        'marks': ria_api.get_marks(category_id),
        'gearboxes': ria_api.get_gearboxes(category_id),
        'driverTypes': ria_api.get_driver_types(category_id),
    })


@app.route('/categories/<category_id>/marks/<mark_id>/models')
def models(category_id, mark_id):
    return jsonify(ria_api.get_models(category_id, mark_id))


@app.route('/states')
def states():
    return jsonify(ria_api.get_states())


@app.route('/states/<state_id>/cities')
def cities(state_id):
    return jsonify(ria_api.get_cities(state_id))


@app.route('/fuels')
def fuels():
    return jsonify(ria_api.get_fuels())


@app.route('/colors')
def colors():
    return jsonify(ria_api.get_colors())


@app.route('/average')
def average():
    args = deepcopy(dict(request.args))
    args['api_key'] = api_key
    ria_average = RiaAverageCarPrice(**args)
    average = ria_average.get_average()
    return jsonify(average)
