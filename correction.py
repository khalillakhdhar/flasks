from flask import Flask, request, jsonify
app = Flask(__name__) # accés aux méthode du protocole http

@app.route('/about', methods=['GET'])
def about():
    return "Hello I am khalil"
@app.route('/writing', methods=['POST'])
def writing():
    fullname = request.args.get('fullname')
    return f"Bienvenue {fullname} !"
if __name__ == '__main__':
    app.run(debug=True)