from flask import Flask, jsonify, request
import redis
import random
import string
import os

app = Flask(__name__)

# Read Redis connection details from environment variables
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)

# Connect to Redis
redis_client = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True
)

# Helper function to generate random strings
def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.route("/")
def index():
    try:
        redis_client.set("test_key", "Hello Redis!")
        value = redis_client.get("test_key")
        return f"Value from Redis: {value}"
    except redis.ConnectionError:
        return "Could not connect to Redis!"

# Endpoint to write a key-value pair to Redis (random or user-provided)
@app.route('/write', methods=['POST'])
def write_to_redis():
    data = request.get_json()

    if data:
        # If key-value pair is provided in the request body
        key = data.get('key')
        value = data.get('value')
        if not key or not value:
            return jsonify({'error': 'Both "key" and "value" are required'}), 400
    else:
        # Generate random key-value pair if no data is provided
        key = random_string()
        value = random_string()

    redis_client.set(key, value)  # No TTL
    return jsonify({'message': 'Key-Value pair added', 'key': key, 'value': value})


# Endpoint to delete a key-value pair from Redis
@app.route('/delete', methods=['DELETE'])
def delete_from_redis():
    key = request.args.get('key')
    if not key:
        return jsonify({'error': 'Key parameter is required'}), 400
    if redis_client.delete(key):
        return jsonify({'message': f'Key {key} deleted'})
    return jsonify({'error': f'Key {key} not found'}), 404

# Endpoint to list all key-value pairs in Redis
@app.route('/list', methods=['GET'])
def list_redis():
    keys = redis_client.keys('*')
    data = {key: redis_client.get(key) for key in keys}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
