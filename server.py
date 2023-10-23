
from flask import Flask, jsonify, request
from flask_cors import CORS
from wrapper import *
import re

HEIGHT_REGEX = re.compile(r'height="(\d+\.?\d*)(\w*)"', re.IGNORECASE)
WIDTH_REGEX = re.compile(r'width="(\d+\.?\d*)(\w*)"', re.IGNORECASE)

app = Flask(__name__)
CORS(app)


@app.route("/cyk", methods=['POST'])
def work_simulation():
    data = request.json
    lines = data['grammar']
    sentence = data['sentence']
    prefix = data['prefix']
    initial_symbol = data['initialSymbol']

    response = wrapper_cyk(lines, sentence, HEIGHT_REGEX,
                           WIDTH_REGEX, prefix, initial_symbol, True)

    return jsonify(response), 200


@app.route("/healthz", methods=['GET'])
def salute():
    return 'Hello from iGrammar server!', 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
