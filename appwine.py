from flask import Flask, url_for, request, jsonify

app = Flask(__name__)

@app.route("/greetings", methods=["POST"])
def greetings():
    if request.method == "POST" and request.is_json:
        json_data = request.get_json()
        if "firstName" in json_data.keys() and "lastName" in json_data.keys():
            response = {
                "msg": f"Welcome {json_data['firstName']} {json_data['lastName']}"
            }
            return jsonify(response), 200
    else:
        return jsonify({"msg": "I don't know you but you are welcome too!"}), 200