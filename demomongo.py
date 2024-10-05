from flask import Flask, request, jsonify
from pymongo import MongoClient
app = Flask(__name__)
# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mymongod']
collection = db['user']
@app.route('/create', methods=['POST'])
def create_record():
 data = request.get_json() # Récupérer les données JSON envoyées
 result = collection.insert_one(data)
 return jsonify({'message': 'Record created successfully', 'id': str(result.inserted_id)})

if __name__ == '__main__':
 app.run(debug=True)