from flask import Flask, request, jsonify

app = Flask("PaaS")

platform_sw = []


@app.route('/create_app', methods=['POST'])
def create_app():

    try:
        data = request.get_json()

        provider = data.get("provider")
        name = data.get("app_name")
        types = data.get("types")

        if not all([name, types]):
            raise ValueError("Name and type must be given")

        vm_sw = {
            "provider": provider,
            "software_name": name,
            "types_of_sw": types
        }

        platform_sw.append(vm_sw)

        return jsonify({
            "msg": "Successfully created a software",
            "Details": vm_sw
        })

    except Exception as e:
        return jsonify({
            "Error": str(e)
        }), 400


@app.route('/lists', methods=['GET'])
def lists_app():
    return jsonify(platform_sw)


if __name__ == "__main__":
    app.run(debug=True, port=8573)