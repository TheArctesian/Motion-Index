from flask import Flask, request, jsonify
from Utils.file_processor import process_file

app = Flask(__name__)

@app.route('/', methods=['GET'])

@app.route('/health', methods=['GET'])
def health_check():
    """Simple endpoint to check if the server is running"""
    return jsonify({'status': 'ok'}), 200

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    # If user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        # Process the file using the function from the separate file
        result = process_file(file)
        return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)