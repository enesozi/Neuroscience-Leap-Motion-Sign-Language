import os, sys, inspect, thread, time, platform

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))

if(platform.system() == 'Linux'):
    arch_dir = 'LeapSDK/lib/x64' if sys.maxsize > 2**32 else 'LeapSDK/lib/x86'
elif(platform.system() == 'Windows'):
    arch_dir = 'LeapSDKWin' if sys.maxsize > 2**32 else 'LeapSDKWin'
elif(platform.system() == 'Darwin'):
    arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap

class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"


    def on_frame(self, controller):
        frame = controller.frame()
        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % (
          frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))
          
def main():
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

if __name__ == "__main__":
    main()