# Import library
from urllib import response
from flask import Flask, app, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Inisiasi object flask
app = Flask(__name__)

# Inisialisasi object flask_restful
api = Api(app)

# Inisialisasi object flask_cors
CORS(app)

# Inisiasi variabel kosong bertipe dictionary
identitas = {} # variabel global, dictionary = json

# Membuat class resource
class ContohResource(Resource):
    # metode get dan post
    def get(self):
        # response = {"msg":"Hallo dunia, ini app restful pertamaku"}
        return identitas

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "Data berhasil dimasukan"}
        return response

# Setup resourcenya
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)