from flask import Response, request
from database.sucursal import Sucursal
from flask_restful import Resource

class SucursalApi(Resource):
    def get(self):
        agencies = Sucursal.objects().to_json()
        return Response(agencies, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        agency = Sucursal(**body).save()
        id = agency.id
        return {'id': str(id)}, 200
