from flask import Flask, request, jsonify, send_file
from create_ppt import create_ppt

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}

@app.route("/create-ppt", methods=["POST"])
def create_ppt_api():
    data = request.json
    data = {
        "title": "Cloud Migration Strategy",
        "slides": [
            {
            "title": "Agenda",
            "points": [
                "What is Cloud Migration",
                "Benefits",
                "Challenges",
                "Strategy"
            ]
            },
            {
            "title": "Migration Approaches",
            "points": [
                "Rehost (Lift & Shift)",
                "Refactor",
                "Replatform",
                "Retire"
            ]
            }
        ]
    }
    ppt_file = create_ppt(data)
    return send_file(ppt_file, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
