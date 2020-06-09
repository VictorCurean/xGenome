from flask import make_response, jsonify, request, Response, render_template
import requests
from . import recipes_blueprint
from flask import url_for
from werkzeug.utils import secure_filename
import os

from xgenom.persistence.utils import store_fasta

@recipes_blueprint.route('/')
def index():
    return render_template("recipes/index.html")

@recipes_blueprint.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@recipes_blueprint.route('/upload-fasta', methods=['POST'])
def upload_fasta():
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ["fasta"]

    a = request
    print(a.values)

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')

        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join("D:\Licenta\Git Repository\\xGenome\\xgenom\\temp_data", filename))

            store_fasta(filename, "victor", None, "human")
            os.remove("D:\Licenta\Git Repository\\xGenome\\xgenom\\temp_data\\" + filename)

            print('File saved')
            return Response(status=200)