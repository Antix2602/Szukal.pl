from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "AIzaSyCbsnjQi_xONy2AQzACwQoy1ypv4nypCTo"
CX = "82c12589690c04d0e"

@app.route("/search")
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Brak zapytania"}), 400

    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Błąd pobierania wyników"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)






