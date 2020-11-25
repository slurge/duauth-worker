###
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

class SVM:
	def __init__(self):
		self.model = SVC(gamma=2, C=1)	#gamma = tolerancia, C = regularizacion

		
	def fit(self, x, y):
		self.model.fit(x, y)
		return self.model.score(x, y)


	def predict(self, x, y):
		pred = self.model.predict(x.reshape(1, -1))[0]
		res = pred == int(y)
		print(res)
		return res
	
