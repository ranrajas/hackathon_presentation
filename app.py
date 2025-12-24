from flask import Flask, request, jsonify
from create_ppt import create_ppt
from r2_upload import upload_to_r2
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/create-ppt", methods=["POST"])
def create_ppt_api():
    if not request.is_json:
        return {"error": "JSON body required"}, 400

    data = request.get_json()
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
    object_key = f"presentations/{os.path.basename(ppt_file)}"

    download_url = upload_to_r2(ppt_file, object_key)

    return jsonify({
        "status": "success",
        "ppt_url": download_url
    })
