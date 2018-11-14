from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, String, text
from sqlalchemy.sql import select

class DB:
	NUMBER_OF_ATTRIBUTES = 60
	def __init__(self,db_name):
		self.__engine = create_engine('sqlite:///%s.sqlite'%db_name)
		metadata = MetaData(self.__engine)
		columns = [Column('attribute_%d'%(i+1), String()) for i in range(DB.NUMBER_OF_ATTRIBUTES)] + [Column('label', String(length=1))]
		self.__train_data = Table('train_table', metadata, *columns)
		metadata.create_all(self.__engine,checkfirst=True)
		self.__conn = self.__engine.connect()


	@property
	def conn(self):
		return self.__conn

	def get_train_data(self):
		return self.__conn.execute(select([self.__train_data]))

	def insert_train_data(self,attributes,label='A'):
		if len(attributes) != DB.NUMBER_OF_ATTRIBUTES:
			raise ValueError('Expected ' + str(DB.NUMBER_OF_ATTRIBUTES) + ' features, got ' + str(len(attributes)))

		inserted = self.__train_data.insert().values(label=label, **attributes)
		self.__conn.execution_options(autocommit=True).execute(inserted)

	def truncate_db(self):
		meta = MetaData(bind=self.__engine, reflect=True)
		trans = self.__conn.begin()
		for table in meta.sorted_tables:
			self.__conn.execute(table.delete())
		trans.commit()


# if __name__ == "__main__":
# 	db = DB('leapd')
# 	attributes = dict(zip(['attribute_%d'%(i+1) for i in range(DB.NUMBER_OF_ATTRIBUTES)],
# 		[1.5555 for _ in range(DB.NUMBER_OF_ATTRIBUTES)]))
# 	db.truncate_db()
# 	db.insert_train_data(attributes)
# 	for r in db.get_train_data():
# 		print r
	