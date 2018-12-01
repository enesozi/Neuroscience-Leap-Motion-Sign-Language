from Database.db_mongo import DB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.externals import joblib

db = DB()
data = db.get_train_data()
print data

# Train data with two models.


# Create reports(confusion matrix etc.)


# Saves models to files
# joblib_file = "joblib_model.pkl"
# joblib.dump(model, joblib_file)

# Load a model from the file
# joblib_model = joblib.load(joblib_file)

