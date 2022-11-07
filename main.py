from flask import Flask, render_template, request, Response,redirect, url_for, jsonify
from client import Client
import database as db

db = db.dbconnection

app = Flask(__name__)

@app.route('/')
def index():
    clientes = db['clientes']
    usuarios = clientes.find()
    return render_template('index.html')

# Method create
@app.route('/clientes', methods=['POST'])
def addClient():
    clientes = db['clientes']
    name = request.form['name']
    lastName = request.form['lastname']
    cel = request.form['cel']

    if name and lastName and cel:
        client = Client(name, lastName, cel)
        clientes.insert_one(client.toDBCollection())
        response = jsonify({
            'name': name,
            'lastName': lastName,
            'cel': cel
        })
        return redirect(url_for('index'))
    else:
        return notFound()

# Method Edit
@app.route('/edit/<string:nameClient>')
def editClient(nameClient):
    clientes = db['clientes']
    name = request.form['name']
    lastName = request.form['lastname']
    cel = request.form['cel']

    if name and lastName and cel:
        clientes.update_one({'name':nameClient},{'$set' : {'name' : name, 'lastName' : lastName, 'cel' : cel}})
        response = jsonify({'message' : 'Cliente' + nameClient + 'Actualizado correctamente'})
        return redirect(url_for('index'))
    else:
        return notFound()

#Method Delete
@app.route('/delete/<string:nameClient>')
def deleteClient(nameClient):
    clientes = db['clientes']
    clientes.delete_one({'name': nameClient})
    return redirect(url_for('index'))


#error de la ruta
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'no encontrado' + request.url,
        'status': '404 not found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True, port=5000)