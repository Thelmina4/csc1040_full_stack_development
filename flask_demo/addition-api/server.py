# server.py
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# In-memory storage for our list of numbers
numbers = []

# Swagger UI configuration
SWAGGER_URL = '/docs'  # URL for Swagger UI
API_URL = '/openapi.yaml'  # URL for the OpenAPI spec

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Numbers API"}
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/openapi.yaml')
def serve_openapi_spec():
    """Serve the OpenAPI specification file."""
    return send_from_directory(BASE_DIR, 'openapi.yaml', mimetype='text/yaml')


@app.route('/add', methods=['POST'])
def add_two_numbers():
    """Add two numbers together and return the result."""
    data = request.get_json()

    if data is None:
        return jsonify({'error': 'Request body must be JSON'}), 400

    if 'a' not in data:
        return jsonify({'error': 'Missing required field: a'}), 400
    if 'b' not in data:
        return jsonify({'error': 'Missing required field: b'}), 400

    if not isinstance(data['a'], (int, float)):
        return jsonify({'error': 'Field "a" must be a number'}), 400
    if not isinstance(data['b'], (int, float)):
        return jsonify({'error': 'Field "b" must be a number'}), 400

    result = data['a'] + data['b']
    return jsonify({'result': result})


@app.route('/numbers', methods=['GET'])
def get_numbers():
    """Return the current list of numbers."""
    return jsonify({
        'numbers': numbers,
        'count': len(numbers)
    })


@app.route('/numbers', methods=['POST'])
def add_number_to_list():
    """Add a new number to the list."""
    data = request.get_json()

    if data is None:
        return jsonify({'error': 'Request body must be JSON'}), 400

    if 'number' not in data:
        return jsonify({'error': 'Missing required field: number'}), 400

    if not isinstance(data['number'], (int, float)):
        return jsonify({'error': 'Field "number" must be a number'}), 400

    numbers.append(data['number'])

    return jsonify({
        'message': 'Number added successfully',
        'numbers': numbers
    }), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)