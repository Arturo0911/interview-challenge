
from app import *
from flask import jsonify
from app.models import (
    PythonChallenge
)
from app.Schema import (
    challenge_schema,
    challenge_schemas
)

# Error requests section
@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "Message": "You haven't authorize to access this url"
        })

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "Message": "Sorry, that method isn't allowed"
        })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "Message": f"Url Not found"
        })






@app.route("/", methods=["GET"])
def index():
    data = PythonChallenge.query.all()
    elements = challenge_schemas.dump(data)
    print(elements)
    return jsonify(elements)


@app.route("/get_currency/<location>/", methods=["GET"])
def query_currency(location: str):
    pass