from flask import Flask, request, jsonify
from parser.lr1_web import generate_tables, parse_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "LR(1) backend running ✅"})

@app.route("/api/generate-tables", methods=["POST"])
def api_generate_tables():
    data = request.get_json()
    grammar_text = data.get("grammar", "")
    result = generate_tables(grammar_text)
    return jsonify(result)

@app.route("/api/parse-string", methods=["POST"])
def api_parse_string():
    data = request.get_json()
    grammar_text = data.get("grammar", "")
    input_string = data.get("input", "")
    result = parse_string(grammar_text, input_string)
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
