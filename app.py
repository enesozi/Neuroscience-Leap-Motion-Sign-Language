from lib_leap import Leap
from train_test_api import Model
from flask import Flask, render_template, request
from hand_data import get_hand_position
import numpy as np
import time
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

controller = Leap.Controller()
Model = Model()

gesture = ""

instances = []


def orderedDict_to_Array(data_as_dict):
	list = []
	for k, v in data_as_dict.items():
		list.append(v)

	return np.array(list)




# Main page
@app.route('/')
def index():
    return render_template('JSONViewer.html')


@app.route('/receiver', methods=['GET'])
def worker():
    # Just for triggering the connection of hmtl and lm device
    request.args.get('foo')
    # Predicting
    data = get_hand_position(controller, blocking=True)
    prediction = Model.predict(data)
    print(prediction)
    # without sleep there is no delay, but it stops after a few seconds (see console of browser)
    #time.sleep(0.5)
    return prediction[0]

if __name__ == '__main__':
	http_server = WSGIServer(('', 5000), app)
	http_server.serve_forever()