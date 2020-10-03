import datetime
import os

from flask import Flask, jsonify, request

from flask_cors import CORS

try:
    from .models import db, Messages
except ImportError:
    from models import db, Messages

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()
# unsafe, all origins have access, should be limited to frontend
CORS(app, resources={r"/*": {"origins": "*"}}, max_age=3600)


@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello World!'})


@app.route('/messages', methods=['GET'])
def get_messages():
    messages = [{
        'id': m.id,
        'message': m.msg,
        'created_at': m.created_at,
        'last_modified_at': m.last_modified_at
    } for m in Messages.query.all()]
    return jsonify(messages)


@app.route('/messages', methods=['POST'])
def add_message():
    data = request.get_json(force=True)
    message = Messages(msg=data.get('message'))
    db.session.add(message)
    db.session.commit()
    return jsonify({'status': 'Success'})


@app.route('/messages/<message_id>', methods=['DELETE'])
def delete_message(message_id):
    try:
        Messages.query.filter_by(id=message_id).delete()
        db.session.commit()
        return jsonify({'status': 'Success'})
    except Exception as e:
        return jsonify({'status': 'Failure'})


@app.route('/messages/<message_id>', methods=['UPDATE'])
def update_message(message_id):
    try:
        message = Messages.query.filter_by(id=message_id).first()
        message.msg = request.get_json(force=True).get('message')
        message.last_modified_at = datetime.datetime.utcnow()
        db.session.add(message)
        db.session.commit()
        return jsonify({'status': 'Success'})
    except Exception as e:
        return jsonify({'status': 'Failure'})
