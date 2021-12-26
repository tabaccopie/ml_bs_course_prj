# USAGE
# Start the server:
# 	python run_server.py
# Submit a request via cURL:
# 	curl -X POST -F image=@dog.jpg 'http://localhost:8180/predict'
# Submita a request via Python:
#	python simple_request.py

# import the necessary packages
import numpy as np
import dill
import pandas as pd
dill._dill._reverse_typemap['ClassType'] = type
#import cloudpickle
import flask
import os

# initialize our Flask application and the model
app = flask.Flask(__name__)
model = None

def load_model(model_path):
	# load the pre-trained model
	global model
	with open(model_path, 'rb') as f:
		model = dill.load(f)

modelpath = "/app/app/models/pipeline.dill"
load_model(modelpath)

@app.route("/", methods=["GET"])
def general():
	return "Welcome to fraudelent prediction process"

@app.route("/predict", methods=["POST"])
def predict():
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}

	# ensure an image was properly uploaded to our endpoint
	if flask.request.method == "POST":
		ssc_p, hsc_p, degree_p = "", "", ""
		request_json = flask.request.get_json()
		if request_json["ssc_p"]:
			ssc_p = request_json['ssc_p']
		if request_json["hsc_p"]:
			hsc_p = request_json['hsc_p']
		if request_json["degree_p"]:
			degree_p = request_json['degree_p']

		preds = model.predict(pd.DataFrame({"ssc_p": [ssc_p],
												  "hsc_p": [hsc_p],
												  "degree_p": [degree_p]}))
		data["predictions"] = round(preds[:1][0][0], 2)
		#data["ssc_p"] = ssc_p
		# indicate that the request was a success
		data["success"] = True

	# return the data dictionary as a JSON response
	return flask.jsonify(data)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading the model and Flask starting server..."
		"please wait until server has fully started"))
	port = int(os.environ.get('PORT', 8180))
	app.run(host='0.0.0.0', debug=True, port=port)
