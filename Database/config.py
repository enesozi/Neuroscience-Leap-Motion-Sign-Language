import os

UNAME = os.environ.get('CNS_UNAME')
PASSWORD = os.environ.get('CNS_PASSWORD')
DBNAME = "utcns"
PORT = 25263
COLLECTION = "train_data"
# with label
NUMBER_OF_ATTRIBUTES = 61
NUM_SAMPLES = 150
SAMPLE_DELAY = 1
NUM_FEATURES = 60