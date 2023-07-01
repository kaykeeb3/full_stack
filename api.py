from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

OPENAI_ENDPOINT = "https://api.openai.com/v1/engines/davinci-codex/completions"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

class OpenAIRequest:
    def __init__(self, prompt):
        self.prompt = prompt

class OpenAIResponse:
    def __init__(self, choices):
        self.choices = choices

@app.route('/question', methods=['POST'])
def handle_question():
    if not request.json or 'prompt' not in request.json:
        return jsonify({'error': 'Invalid request'}), 400

    prompt = request.json['prompt']
    response = get_openai_response(prompt)
    
    return jsonify(response), 200

def get_openai_response(prompt):
    data = OpenAIRequest(prompt=prompt)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {OPENAI_API_KEY}'
    }
    
    response = requests.post(OPENAI_ENDPOINT, data=json.dumps(data.__dict__), headers=headers)
    
    if response.status_code == 200:
        json_response = json.loads(response.text)
        choices = json_response['choices']
        return OpenAIResponse(choices=choices)
    
    return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
