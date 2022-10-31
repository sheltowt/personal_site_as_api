import json
from flask import Flask, jsonify, request, make_response

basic_api = Flask(__name__)

with open("resume.json") as json_data:
	resume = json.load(json_data)

@basic_api.route('/', methods=['GET'])
def display_resume():
	if request.method == 'GET':
		return make_response(jsonify(resume), 200)

if __name__ == '__main__':
    basic_api.run(debug=False, host='0.0.0.0', port=8080)