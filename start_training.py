from lib_leap import Leap
import time
from trainer_gui import TrainGUI
from hand_data import get_hand_position
from Database.config import NUM_SAMPLES, SAMPLE_DELAY, NUM_FEATURES


def train():
    train_gui = TrainGUI()
    controller = Leap.Controller()
    print("Please show your hand")
    for t in range(NUM_SAMPLES):
        print('Getting hand data..')
        sample = get_hand_position(controller, True)
        while len(sample) != NUM_FEATURES:
            print "Please place only right hand in view"
            sample = get_hand_position(controller, True)
        print(sample)
        print "Please submit and try again.."
        train_gui.run(sample)
        time.sleep(SAMPLE_DELAY)


if __name__ == "__main__":
    train()
