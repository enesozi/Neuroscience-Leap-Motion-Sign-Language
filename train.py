from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from joblib import dump,load

# Read file
data = pd.read_csv('train_data_last.csv')
print data.head()

# Split test-train
X_train, X_test, y_train, y_test = train_test_split(data.iloc[:,:-1], data.label, test_size=0.2, random_state=42)

# Train data with two models.
clf = RandomForestClassifier(n_estimators=15, max_depth=3, random_state=0)
clf.fit(X_train,y_train)

svc = SVC(gamma='auto')
svc.fit(X_train,y_train)

# Create reports(confusion matrix etc.)
# TODOS

# Saves models to files
joblib_file1 = "models/random_forest.pkl"
dump(clf, joblib_file1)

joblib_file2 = "models/svc.pkl"
dump(svc, joblib_file2)

# Load a model from the file
# joblib_model = load(joblib_file)