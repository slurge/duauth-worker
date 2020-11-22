from sklearn.svm import SVC  ##########
from pathlib import Path 	         #
import pandas as pd    			  ##	
import numpy as np                ####
import makedata                       #
import pickle                         #
import SVM                ###      ###
import csv                  #######


class driver:
	def __init__(self):
		self.loaded_model = SVM.SVM()
		self.set_headers()

		#with open('data/1.csv', 'a', newline='') as f:
		#	writer = csv.writer(f)
		#	writer.writerow(self.headers)


	#-------SVM-------

	def fit(self, data):
		#si existe dataset para sitio, cargar desde csv
		#if self.dataset_exists(data['site']):
		#	self.load_csv(data['site'])

		#crear vector con su Y
		vec = makedata.make(data['cadence'], data['agent'])

		vec.append(data['user'])

		with open('data/1.csv', 'a', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(vec)


		#df = pd.DataFrame(data=[vec], columns=self.headers)
		#print(df)

		#self.loaded_dataset.append(df, ignore_index=True)
		#self.save_csv(data['site'])
		

		#si datos > 100, hacer split y calcular score
		#svm.fit(dataframe)
		#x = np.asanyarray(self.loaded_dataset.drop(columns=['target_user']))
		#y = np.asanyarray(self.loaded_dataset[['target_user']])

		#score = self.loaded_model.fit(x, y) if len(self.loaded_dataset) > 30 else -1
		score = -1

		#guardar pickle
		if score > 0:
			self.save_pickle(data['user'])
		#guardar csv
		return score





	def predict(self, data):
		#si model no existe, error
		if self.model_exists(data['user']):
			self.load_pickle(data['user'])
		else:
			return 'no existe ese modelo'
		#crear vector
		x = np.asanyarray(makedata.make(data['cadence'], data['agent']))
		y = data['user']
		#svm.predict(x,y)
		return self.loaded_model.predict(x, y)
		#return resultado

	#-----------------

	def set_headers(self):
		n  = [str(i + 1) for i in range(20)]
		self.headers = n + [
			'is_pc',
			'is_mobile',
			'is_tablet',
			'is_touch_capable',
			'is_bot',
			'browser',
			'browser_version',
			'os',
			'os_version',
			'device',
			'target_user'
		]

	def new_model(self):
		self.loaded_model = SVM.SVM()

	#------files------

	def save_pickle(self, name):
		with open('models/'+str(name)+'.bin', 'wb') as f:
			f.write(pickle.dumps(self.loaded_model))

	def load_pickle(self, name):
		with open('models/'+name+'.bin', 'rb') as f:
			self.loaded_model = pickle.loads(f.read())

	def save_csv(self, name):
		self.loaded_dataset.to_csv('data/'+str(name)+'.csv')

	def load_csv(self, name):
		self.loaded_dataset = pd.read_csv('data/'+str(name)+'.csv')

	#-----------------

	def model_exists(self, model):
		return self.file_exists('models/'+str(model)+'.bin')

	def dataset_exists(self, dataset):
		return self.file_exists('data/'+str(dataset)+'.csv')

	def file_exists(self, filename):
		return Path(filename).is_file()


if __name__ == '__main__':

	aber = {
		'site' : 0,
		'user' : 0,
		'cadence' : [12,43543,123,2323,456,234,123],
		'agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
	}

	a = driver()
	print(a.fit(aber))
