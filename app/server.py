from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__, template_folder="/www")

# Fichier de stockage des restrictions
RESTRICTIONS_FILE = "/data/restrictions.json"

def load_restrictions():
    if not os.path.exists(RESTRICTIONS_FILE):
        return {}
    with open(RESTRICTIONS_FILE, "r") as file:
        return json.load(file)

def save_restrictions(data):
    with open(RESTRICTIONS_FILE, "w") as file:
        json.dump(data, file)

@app.route("/")
def index():
    restrictions = load_restrictions()
    return render_template("index.html", restrictions=restrictions)

@app.route("/save", methods=["POST"])
def save():
    data = request.json
    save_restrictions(data)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
