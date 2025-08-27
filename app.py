from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = 'AIzaSyCbsnjQi_xONy2AQzACwQoy1ypv4nypCTo'
CX = '82c12589690c04d0e'

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data.get('q', '')
    if not query:
        return jsonify({'error': 'Brak zapytania'}), 400

    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': API_KEY,
        'cx': CX,
        'q': query,
        'num': 10,
        'lr': 'lang_pl'  # wyniki po polsku
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Błąd pobierania wyników', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)





