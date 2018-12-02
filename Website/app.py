import Leap
import os, sys, inspect, thread, time, platform
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from time import sleep
from threading import Thread, Event
app = Flask(__name__)

controller = Leap.Controller()

socketio = SocketIO(app)
thread = Thread()
thread_stop_event = Event()

connection = "False"; 
state = "Not connected";
gesture= "";


class UpdateThread(Thread):
    def __init__(self):
        self.delay = 1
        super(UpdateThread, self).__init__()

    def update(self):
        print("updating values...")
        

        '''while not thread_stop_event.isSet():
            
            connection = "False"
            state = "Not connected"
            gesture = "None"
            number = "11"
            print("Try to send...")
            socketio.emit('newnumber', {'number': number}, namespace='/test')
            sleep(self.delay)
        '''

    def run(self):
        self.update()




class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"


    def on_frame(self, controller):
        frame = controller.frame()
        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
          frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))
    

def run_controller():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)




# Main page
@app.route('/')
def index():
    return render_template('index.html', connection=connection, state=state, gesture=gesture)


@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    run_controller()

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = UpdateThread()
        thread.start()


@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)



