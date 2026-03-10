from flask import Flask, request, jsonify

app = Flask("Rs to $")

@app.route('/convert', methods=['POST'])
def conversion_rs():

    try:
        data = request.get_json()

        amt_rs = data["rs"]

        rate = 0.012

        dollar = amt_rs * rate

        return jsonify({"Result": f"Rs{amt_rs} => ${format(dollar,'.2f')}"})

    except Exception as e:
        return jsonify({"Error": str(e)}), 500


if _name_ == "_main_":
    app.run(debug=True, port=8796)