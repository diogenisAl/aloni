import flask
from flask import request, jsonify
import json


app = flask.Flask(__name__)
# app.config["DEBUG"] = True

#  Open data.json file
f = open('data/members_data.json', "r")

#  Load data from json file to data variable.
animals = json.load(f)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Student Archive</h1>
<p>Under construction...</p>'''

# A route to return all of the available entries in our catalog.
@app.route('/api/members/all', methods=['GET'])
def api_all():
    return jsonify(animals)

@app.route('/api/members', methods=['GET'])
def api_id():
    # Check if an English Name was provided as part of the URL.
    # If English Name is provided, assign it to a variable.
    # If no English Name is provided, display an error in the browser.
    # URL example: http://127.0.0.1:5000/api/animals?english_name=Dog

    #if 'id' in request.args:
    #    id = int(request.args['id'])

    if 'english_name' in request.args:
        english_name = str(request.args['english_name'])
    else:

        return "Error: No english_name field provided. Please specify an english_name."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for animal in animals:
#        if animal['id'] == id:
        if animal['english_name'] == english_name:
            results.append(animal)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


# Run the app
if __name__ == '__main__':
    app.run()