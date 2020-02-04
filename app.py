import os
import pythaiapi

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = os.urandom(24)
CORS(app)


@app.route('/api/word_tokenize', methods=['POST'])
def tokenize():
    return jsonify(pythaiapi.tokenize(request))


@app.errorhandler(404)
def not_found(e):
    return jsonify({'success': False, 'message': 'Not Found'})

if __name__ == "__main__":
    app.run()




# @app.route('/api/normalize', methods=['POST'])
# def normalize():
#     return jsonify(pythaiapi.normalize(request))


# @app.route('/api/spell', methods=['POST'])
# def spell():
#     return jsonify(pythaiapi.spell(request))


# @app.route('/api/pos_tag', methods=['POST'])
# def pos_tag():
#     return jsonify(pythaiapi.pos_tag(request))
