from flask import Blueprint, request, jsonify, abort
from app.extension import db
from app.models.Marca import Marca

marca_blueprint = Blueprint("marca", __name__)

@marca_blueprint.route("/", methods=["GET"])
def get_marcas():
    marcas = Marca.query.all()
    return jsonify([
        {
            'id': marca.id,
            'name': marca.name,
            'owner_name': marca.owner_name,
            'creation_date': marca.creation_date
        } for marca in marcas
    ])

@marca_blueprint.route("/", methods=["POST"])
def create_marca():
    data = request.get_json()
    name = data.get('name')
    owner_name = data.get('owner_name')

    if not name:
        abort(400, owner_name="El campo 'name' es obligatorio.")

    marca = Marca(name=name, owner_name=owner_name)
    db.session.add(marca)
    db.session.commit()

    return jsonify({
        'id': marca.id,
        'name': marca.name,
        'owner_name': marca.owner_name,
        'creation_date': marca.creation_date
    }), 201

@marca_blueprint.route("/<int:id>", methods=["GET"])
def get_marca(id):
    marca = Marca.query.get(id)
    if not marca:
        abort(404, owner_name="Marca no encontrada.")

    return jsonify({
        'id': marca.id,
        'name': marca.name,
        'owner_name': marca.owner_name,
        'creation_date': marca.creation_date
    })

@marca_blueprint.route("/<int:id>", methods=["PUT"])
def update_marca(id):
    data = request.get_json()
    marca = Marca.query.get(id)
    if not marca:
        abort(404, owner_name="Marca no encontrada.")

    name = data.get('name')
    owner_name = data.get('owner_name')

    if name:
        marca.name = name
    if owner_name:
        marca.owner_name = owner_name

    db.session.commit()

    return jsonify({
        'id': marca.id,
        'name': marca.name,
        'owner_name': marca.owner_name,
        'creation_date': marca.creation_date
    })

@marca_blueprint.route("/<int:id>", methods=["DELETE"])
def delete_marca(id):
    marca = Marca.query.get(id)
    if not marca:
        abort(404, owner_name="Marca no encontrada.")

    db.session.delete(marca)
    db.session.commit()

    return jsonify({"message": "Marca eliminada exitosamente."}), 200
