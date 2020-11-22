from flask import *
from flask_cors import CORS
import manager

app = Flask('WorkerSVM')
CORS(app)

driver = manager.driver()

#------accesos--------------------------

@app.route('/fit', methods = ['POST'])
def fit():
	data = request.get_json() 
	print ('\nTraning: ', data)
	resp = driver.fit(data)
	return jsonify({'score': resp})


@app.route('/predict', methods = ['POST'])
def predict():
	data = request.get_json() 
	print ('\nPredicting: ', data)
	resp = driver.predict(data)
	return jsonify({'is_user': resp})


#----------------------------------------

@app.route('/')
def home():
	with open('eyes.html', 'r') as aber:
		page = aber.read()
	return page


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/kill', methods=['GET'])
def kill():
	print('killing app')
	shutdown_server()

#-----------------------------------------

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)