from config import UNAME, PASSWORD, DBNAME, PORT, COLLECTION, NUMBER_OF_ATTRIBUTES
from pymongo import MongoClient

class DB:

    def __init__(self):
        client = MongoClient(
            'mongodb://{0}:{1}@ds125263.mlab.com:{2}/{3}'.format(UNAME, PASSWORD, PORT, DBNAME))
        self.__train_data_collection = client[DBNAME][COLLECTION]

    def get_train_data(self):
        return [instance for instance in self.__train_data_collection.find()]

    def insert_train_data(self, attributes):
        if len(attributes) != NUMBER_OF_ATTRIBUTES:
            raise ValueError('Expected ' + str(NUMBER_OF_ATTRIBUTES) +
                             ' features, got ' + str(len(attributes)))

        print("Inserted with id: ", self.__train_data_collection.insert(attributes))

    def truncate_db(self):
        x = self.__train_data_collection.delete_many({})
        print(x.deleted_count, " documents deleted.")


# if __name__ == "__main__":
#     db = DB()
#     attributes = dict(zip(['attribute_%d' % (i + 1) for i in range(DB.NUMBER_OF_ATTRIBUTES)],
#                           [1.5555 for _ in range(DB.NUMBER_OF_ATTRIBUTES)]))
#     db.truncate_db()
#     db.insert_train_data(attributes)
#     for r in db.get_train_data():
#         print r
