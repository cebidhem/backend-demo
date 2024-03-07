# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.database import db, Name
from backend.config import POSTGRES
import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

# Create the tables within the Flask application context
with app.app_context():
    db.init_app(app)
    db.create_all()


@app.route('/names', methods=['POST'])
def store_name():
    name = request.json.get('name')
    if name:
        new_name = Name(name=name)
        db.session.add(new_name)
        db.session.commit()
        return jsonify({'message': 'Name stored successfully'}), 201
    else:
        return jsonify({'error': 'Name not provided'}), 400


@app.route('/names', methods=['GET'])
def get_names():
    names = Name.query.all()
    return jsonify({'names': [name.name for name in names]})


@app.route('/live', methods=['GET'])
def is_live():
    return {"message": True}, 200


@app.route('/ready', methods=['GET'])
def is_ready():
    Name.query.all()
    return {"message": True}, 200


if __name__ == '__main__':
    app.run(host=os.environ.get('BINDING', 'localhost'), debug=os.environ.get('DEBUG', False))
