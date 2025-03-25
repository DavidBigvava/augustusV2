from flask import Flask, render_template, request, jsonify
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
    app.run(debug=True) 