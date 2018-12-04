from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from joblib import dump, load


class Model(object):

    def __init__(self, model_name='random_forest'):
        self.model_name = model_name
        self.clf = None
        self.model_file = "models/%s.joblib" % self.model_name

    def train(self, train_file='train_data_last.csv'):
        # Read file
        data = pd.read_csv(train_file)

        # Split test-train
        X_train, _, y_train, _ = train_test_split(
            data.iloc[:, :-1], data.label, test_size=0.2, random_state=42)

        if self.model_name == 'random_forest':
            self.clf = RandomForestClassifier(
                n_estimators=15, max_depth=3, random_state=0)
        else:
            self.clf = SVC(gamma='auto')

        self.clf.fit(X_train, y_train)

        # Saves model to file
        dump(self.clf, self.model_file)

    def predict(self, test_instance):
        if self.clf is None:
            self.clf = load(self.model_file)
        return self.clf.predict(test_instance)
