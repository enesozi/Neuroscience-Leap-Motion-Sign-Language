from lib_leap import Leap
from train_test_api import Model
from flask import Flask, render_template, request
from hand_data import get_hand_position
import sys

app = Flask(__name__)

controller = Leap.Controller()
model = Model(model_name='knn', mode=1)

# Main page


@app.route('/')
def index():
    return render_template('JSONViewer.html')


@app.route('/receiver', methods=['GET'])
def worker():
    data = get_hand_position(controller, blocking=True)
    return model.predict(data)[0]

if __name__ == '__main__':
    app.run()
