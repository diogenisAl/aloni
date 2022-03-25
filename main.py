import flask
from flask import request, jsonify
import json


app = flask.Flask(__name__)
# app.config["DEBUG"] = True

#  Open .json file
f = open('data/members_data.json', "r")

#  Load data from json file to data variable.
members = json.load(f)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Student Archive</h1>
<p>Under construction...</p>'''

# A route to return all of the available entries in our catalog.
@app.route('/api/members/all', methods=['GET'])
def api_all():
    return jsonify(members)

@app.route('/api/members', methods=['GET'])
def api_id():

    if 'id' in request.args:
        id = str(request.args['id'])
    else:

        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for member in members:
        if member['members_IDs'].find(id) != -1:
            results.append(member)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


# Run the app
if __name__ == '__main__':
    app.run()