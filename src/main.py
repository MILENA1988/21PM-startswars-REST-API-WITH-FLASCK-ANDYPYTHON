"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Favoritos, Planetas, Personajes
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# generate sitemap with all your endpoints
@app.route('/user', methods=['GET'])
def handle_hello():
    response = User.query.all()
    users = list(map(lambda x: x.serialize(), response))

    return jsonify(users), 200

 #para llamar a todos los personajes

@app.route("/personajes", methods=["GET"])
def personajes_todos():

     query = Personajes.query.all()
     results =  list(map(lambda x: x.serialize(),query))

     return jsonify(results)
     #para llamar a un único personaje
@app.route ("/personajes/<int:id>" , methods=["GET"])
def personaje_unico(id):  #

    personaje = Personajes.query.get(id)
    if personaje is None:
        raise APIException("Personaje not found", status_code=404)
    results = personaje.serialize()#me explican

    return jsonify(results), 200

@app.route("/add_personajes", methods=["POST"])
def add_personajes():#consultar

    request_body =  request.get_json()
    print(request_body)

    addpersonajes= personajes(name=request_body["name"], fecha_nacimiento=request_body["fecha_nacimiento"], estatura=["estatura"], genero=["genero"]) #lo que esta en [son las caracters de las tablas]
    db.session.add(add_personajes)
    db.session.commit()

    return jsonify("Perfect"), 200


@app.route("/planetas", methods=["GET"])
def planetas_todos():

    response = Planetas.query.all()
    planetas =  list(map(lambda x: x.serialize(), response))

    return jsonify(planetas), 200 ## el 200 es para indicar el estado, osea q todo bien
 
#para llamar a un único planeta

@app.route ("/planetas/<int:planeta_id>" , methods=["GET"])
def planeta_unico(planeta_id):

    planetas = character.query.get(planeta_id)
    if planetas is None:
        raise APIException("Personaje not found", status_code=404)
    results = planetas.serialize()#me explican
    return jsonify(result), 200

@app.route("/add_planetas", methods=["POST"])
def add_planeta():

    request_body =  request.get_json()
    print(request_body)


    addplanetas= Planetas(name=request_body["name"], poblacion=request_body["poblacion"], diametro=request_body["diametro"], gravedad=request_body["gravedad"]) #lo que esta en [son las caracters de las tablas]
    db.session.add(addplanetas)
    db.session.commit()

    return jsonify("Perfect"), 200    

@app.route("/favoritos", methods=["GET"])
def favoritos_todos():

     query = Personajes.query.all()
     results =  list(map(lambda x: x.serialize(),query))

     return jsonify(results)



@app.route("/add_favoritos/<int:iduser>", methods=["POST"])
def add_fav(iduser):

    request_body =  request.get_json()
    print(request_body)

    fav= Favoritos(planetas_name=request_body["planetas_name"], personajes_name=request_body["personajes_name"], usuario_id=iduser) #lo que esta en [son las caract ers de las tablas]
    db.session.add(fav)
    db.session.commit()

    return jsonify("Perfect"), 200


@app.route("/del_favorito/<int:fid>", methods=["DELETE"])
def del_favorito(fid):
### recibo info del request
    fav =  Favoritos.query.get(fid)
    if fav is None:
       raise APIException("Favorito no encontrado", status_code=404)

    else:
        db.session.delete(fav)
        db.session.commit()

    return jsonify("good job"), 200



  




# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
