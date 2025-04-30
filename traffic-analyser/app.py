from flask import Flask, request, jsonify, render_template # type: ignore
from traffic_detection import detect_objects  # Import the detection function

app = Flask(__name__)

@app.route('/')
def index():
    # This will render the HTML file when you access http://127.0.0.1:5000/
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Save the file to a directory
    file_path = "./uploads/" + file.filename
    file.save(file_path)

    # Detect traffic objects
    green_light_road = detect_objects(file_path)
    
    return jsonify({"green_light": green_light_road}), 200

if __name__ == "__main__":
    app.run(debug=True)
