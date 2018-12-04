import Leap
from train_test_api import Model
from sklearn.externals import joblib
from sklearn.datasets import load_digits
import os, sys, inspect, thread, time, platform
from flask import Flask, render_template, url_for, copy_current_request_context, request
from hand_data import get_hand_position 
app = Flask(__name__)

controller = Leap.Controller()
model = Model()


connection = "False"; 
state = "Not connected";
gesture= "";


# Main page
@app.route('/')
def index():
    return render_template('JSONViewer.html')


@app.route('/receiver', methods = ['GET'])
def worker():
    # Just for triggering the connection of hmtl and lm device
    request.args.get('foo')
    
    # Predicting
    #data = get_hand_position(controller)
    #print(data)
    #prediction = model.predict(data)

    return "A"


if __name__ == '__main__':
    app.run()



