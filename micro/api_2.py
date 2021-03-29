from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@http://localhost/arb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.route('/cp/<id>', methods=['GET'])
def get_cp(id):
  task = cp.query.get(id)
  return cp.jsonify(task)


if __name__ == "__main__":
    app.run(debug=True)