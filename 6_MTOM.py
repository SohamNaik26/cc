from flask import Flask, request, send_from_directory, jsonify
import os

app = Flask(__name__)

# Folder where files will be stored
UPLOAD_FOLDER = "uploads"

# Create folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Upload API
@app.route('/upload', methods=['POST'])
def upload_file():

    file = request.files.get('file')

    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        return {
            "message": f"File '{file.filename}' uploaded successfully!"
        }

    return {"error": "No file uploaded"}, 400


# Download API
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):

    try:
        return send_from_directory(
            UPLOAD_FOLDER,
            filename,
            as_attachment=True
        )

    except FileNotFoundError:
        return {"error": "File not found"}, 400


# Run server
if __name__ == "__main__":
    app.run(debug=True)