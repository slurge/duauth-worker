from sklearn.svm import SVC  ##########
from pathlib import Path 	         #
import pandas as pd    			  ##	
import numpy as np                ####
import makedata                       #
import pickle                         #
import SVM                ###      ###
import csv                  #######


class driver:

	def new_dataset(self, name):
		with open('data/'+name+'.csv', 'w') as f:
			writer = csv.writer(f)
			n  = [str(i + 1) for i in range(20)]
			headers = n + [
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
			writer.writerow(headers)


	def fit(self, data):
		#si no existe dataset: crear nuevo
		if not self.dataset_exists(data['site']):
			self.new_dataset(data['site'])
		#crear vector con data
		vec = makedata.make(data['cadence'], data['agent'])
		vec.append(data['user'])
		#escribir vector a csv
		self.write_vec(vec, data['site'])
		#leer csv con pandas
		df = self.load_dataset(data['site'])
		#si num de datos > 10:
		if len(df) > 10:
			x = np.asanyarray(df.drop(columns=['target_user']))
			y = np.asanyarray(df[['target_user']])
			#entrenar
			model = SVM.SVM()
			score = model.fit(x, y.ravel())
			#guardar modelo
			self.save_pickle(data['user'], model)
			#regresar score
			return score
		return -1
		
	def predict(self, data):
		#si modelo no existe, regresar error
		if not self.model_exists(data['user']):
			return 'error: no existe ese usuario'
		#crear vector
		vec = np.asanyarray(makedata.make(data['cadence'], data['agent']))
		#cargar model
		model = self.load_pickle(data['user'])
		#clasificar
		return model.predict(vec, data['user'])
		#return resultado
		


	def load_dataset(self, dataset_name):
		return pd.read_csv('data/'+dataset_name+'.csv')

	def write_vec(self, vec, dataset):
		with open('data/'+dataset+'.csv', 'a', newline='') as f:
			writer = csv.writer(f)
			writer.writerow(vec)

	def save_pickle(self, name, model):
		with open('models/'+str(name)+'.bin', 'wb') as f:
			f.write(pickle.dumps(model))

	def load_pickle(self, name):
		with open('models/'+str(name)+'.bin', 'rb') as f:
			return pickle.loads(f.read())



	def model_exists(self, model):
		return self.file_exists('models/'+str(model)+'.bin')

	def dataset_exists(self, dataset):
		return self.file_exists('data/'+str(dataset)+'.csv')

	def file_exists(self, filename):
		return Path(filename).is_file()
		


if __name__ == '__main__':
	print('si')
