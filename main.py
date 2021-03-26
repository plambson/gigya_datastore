from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Payload
import json

app = Flask(__name__)
app.secret_key = '1234qwer'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payload.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)


@app.route('/retrieve', methods=['GET'])
def retrieve():
    gigya_id = request.args.get('gigya_id')
    payload = db.session.query(Payload.payload).filter(Payload.gigya_id == gigya_id).first()[0]
    return payload


@app.route('/insert', methods=['POST'])
def insert():
    gigya_id = request.form.get('gigya_id')
    payload = request.form.get('payload')
    row = Payload(gigya_id, payload)
    db.session.add(row)
    db.session.commit()
    return '{}'.format(row.id)


@app.route('/retrieve_ids', methods=['GET'])
def retrieve_ids():
    ids = [x.gigya_id for x in db.session.query(Payload.gigya_id)]
    return json.dumps(ids)


@app.route('/retrieve_all', methods=['GET'])
def retrieve_all():
    all = [[x.gigya_id, x.payload] for x in db.session.query(Payload).all()]
    return json.dumps(all)


if __name__ == "__main__":
    app.run()
