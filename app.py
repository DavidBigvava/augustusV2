from flask import Flask, render_template, request, jsonify
import os
from src.mistral_client import MistralHandler

app = Flask(__name__)
mistral = MistralHandler()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = mistral.get_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    # Get port from environment variable or default to 10000
    port = int(os.environ.get('PORT', 10000))
    # Bind to 0.0.0.0 to listen on all available interfaces
    app.run(host='0.0.0.0', port=port) 