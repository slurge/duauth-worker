from flask import *
from flask_cors import CORS


app = Flask('flaksModule')

@app.route('/fit', methods = ['POST'])
def fit():
	print('aber')
	si = request.get_json() #Conseguir los datos del fingerprint y cadencia
	print ('\nTraning: ', si[])
	#aqui iria el modelo de entrenamiento de datos

	return jsonify(resp)

@app.route('/predict', methods = ['POST'])
def predict():
	si = request.get_json() 

	print ('\nPredicting: ', si)
	#Modelo de prediccion SVM con SVC
	return jsonify(resp)

@app.route('/')
def home():
	return 'Hola mundo!'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/kill', methods=['GET'])
def kill():
	print('killing app')
	shutdown_server()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)