from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from joblib import dump, load
from time import time


class Model(object):

    def __init__(self, model_name='random_forest', mode=0):
        self.model_name = model_name
        self.model_file = "modelsv2/%s.joblib" % self.model_name
        self.clf = None
        if mode == 1:
            self.clf = load(self.model_file)

    def train(self, test_size=.2, train_file='train_data_latest.csv'):
        # Read file
        data = pd.read_csv(train_file)

        # Split test-train
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            data.iloc[:, :-1], data.label, stratify=data.label, test_size=test_size, random_state=42)

        if self.model_name == 'random_forest':
            self.clf = RandomForestClassifier(
                n_estimators=15, max_depth=3, random_state=0)
        elif (self.model_name == 'knn'):
            self.clf = KNeighborsClassifier()
        else:
            self.clf = SVC(gamma='auto')

        self.clf.fit(self.X_train, self.y_train)

        # Saves model to file
        dump(self.clf, self.model_file)

    def predict(self, test_instance):

        features_reordered = np.array([test_instance[key]
                                       for key in sorted(test_instance)])

        return self.clf.predict(features_reordered.reshape(1, -1))

    def evaluate(self, test_size=0.2, train_file='train_data_last.csv'):
        # measure time for training
        t0 = time()
        self.train(random_state=0)
        print('Test split: {0}', test_size)
        print('Number of training samples {0} Number of test samples {1}'
              .format(len(self.y_train), len(self.y_test)))
        train_time = time() - t0

        # measure time for predicting
        t0 = time()
        test_predict = self.clf.predict(self.X_test)
        test_time = time() - t0
        train_predict = self.clf.predict(self.X_train)
        #calculate accuracies
        accuracy_train = accuracy_score(self.y_train, train_predict)
        accuracy_test = accuracy_score(self.y_test, test_predict)
        print('Accuracy test: {0}'.format(accuracy_test))
        print('Confusion matrix for test data:')
        print(confusion_matrix(self.y_test, test_predict))

        return train_time, test_time, accuracy_train, accuracy_test
