# Import
from flask import Flask, render_template
app = Flask(__name__)

# Get Controller
controller = Leap.Controller()

# Main page
@app.route('/')
def start():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()



