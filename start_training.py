from lib_leap import Leap
import time
from trainer_gui import TrainGUI
from hand_data import get_hand_position
from Database.config import NUM_SAMPLES, SAMPLE_DELAY, NUM_FEATURES


def train():
    train_gui = TrainGUI()
    controller = Leap.Controller()

    for t in range(NUM_SAMPLES):
        sample = get_hand_position(controller, True)
        while len(sample) != NUM_FEATURES:
            print "Please place only right hand in view"
            sample = get_hand_position(controller, True)
        print(sample)
        train_gui.run(sample)
        print "Please, wait.."
        time.sleep(SAMPLE_DELAY)
        print "Now, you can try.."


if __name__ == "__main__":
    train()
