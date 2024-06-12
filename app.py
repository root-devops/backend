import os
from flask import Flask, jsonify
import logging

app = Flask(__name__)


# Get the name from the environment variable
name = os.getenv('NAME', 'World')

# Print the environment variable
print(f"Environment variable NAME: {name}")

@app.route('/api/greet', methods=['GET'])
def greet():
    
    # Create the greeting message
    greeting = f"Hello {name}"
    
    # Return the greeting message as JSON
    return jsonify(greeting=greeting)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
