from lib_leap import Leap
from train_test_api import Model
from flask import Flask, render_template, request
from hand_data import get_hand_position

app = Flask(__name__)

controller = Leap.Controller()
Model = Model()

gesture = ""

instances = []



# Main page
@app.route('/')
def index():
    return render_template('JSONViewer.html')


@app.route('/receiver', methods=['GET'])
def worker():
    # Just for triggering the connection of hmtl and lm device
    request.args.get('foo')
    # Predicting
    #data = get_hand_position(controller)
    # print(data)
    #prediction = model.predict(data)

    return "A"



if __name__ == '__main__':
    app.run()
