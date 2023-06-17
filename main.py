from flask import Flask
from flask import request
from factura_helper import dame_datos_de_factura
from firebase_helper import update_firebase_data
app = Flask(__name__)

@app.route('/', methods=['POST'])
def hello_world():
    request_json = request.get_json()
    if 'filename' in request_json:
        filename = request_json['filename']
        id = request_json['id']
        row = dame_datos_de_factura(filename)
        update_firebase_data(id, row)
        return row
    else:
        return 'Bad Request', 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
