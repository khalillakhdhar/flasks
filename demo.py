from flask import Flask, request, jsonify

app = Flask(__name__) # accés aux méthode du protocole http
# Route d'accueil (GET)
@app.route('/') # annotation
def home():
 return "Bienvenue dans notre application Flask !"
@app.route('/lecture', methods=['GET'])
def get_example():
 param = request.args.get('param', 'No parameter passed') # Récupérer un paramètre 

 return jsonify({'message': f'Paramètre reçu : {param}'})
@app.route('/ecriture',methods=['POST'])
def post_example():
 data = request.get_json() # Récupérer les données JSON envoyées
 #name = data.get('name', 'No name provided')
 return jsonify({'message': f'Hello {data}, this data was received!'})



if __name__ == '__main__':
 app.run(debug=True)
# localhost:5000/api / 127.0.0.1:5000/api