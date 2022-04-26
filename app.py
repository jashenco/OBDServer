from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
import json

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

class JsonModel(object):
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class CarStatistic(db.Model, JsonModel):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=False, nullable=False)
    value = db.Column(db.String(100), unique=False)
    date = db.Column(db.DateTime, unique=False)

    def __repr__(self):
        return f'[{self.id}, {self.key}, {self.value}, {self.date}]'

@app.route("/")
def home():
    return "OBD App. Test 1."

@app.route("/stats", methods=['GET', 'POST'])
def addstat():
    if request.method == 'POST':
        content = request.json

        key = content['key']
        value = content['value']
        date = datetime.datetime.now()

        newCarStatistic = CarStatistic(key=key, value=value, date=date)

        db.session.add(newCarStatistic)
        db.session.commit()

        return "data received"

    elif request.method == 'GET':
        return json.dumps([s.as_dict() for s in CarStatistic.query.all()], default=str)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')