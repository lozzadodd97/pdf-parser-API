from flask import Flask, request, jsonify
import os
from pdf_parsing import extract_text
from semantic_analysis import analyze_and_contextualize
from config import FLASK_ENV, DEBUG

# Create the flask application object
app = Flask(__name__)

# Apply configurations
app.config['ENV'] = FLASK_ENV
app.config['DEBUG'] = DEBUG

# Define the http request (url and method) and extraction function
@app.route('/api/v1/extract', methods=['POST'])
def extract():
    """
    This function comprises error handling whilst carrying out the pdf parsing and contextualization
    :return: Error message or dictionary of contextualized data
    :rtype: json
    """

    # Error handling
    # TODO: It appears that the error handles no file included as empty filename
    # No file present error
    if 'file' not in request.files:
        return jsonify({"error": "Bad request, file not included."}), 400
    # Create file object
    file = request.files['file']
    # Empty file name error
    if file.filename == '':
        return jsonify({"error": "Bad request, empty filename."}), 400
    # File is not supported type (pdf) error
    if not file.filename.endswith('.pdf'):
        return jsonify({"error": "Unsupported file type"}), 415
    # TODO: Add a new error in case the file is empty
    # Process the request
    try:
        # Ensure temp directory exists
        tmp_dir = '/tmp'
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
        # Save file to temp
        file_path = os.path.join('/tmp', file.filename)
        file.save(file_path)
        # Parse and contextualize
        text = extract_text(file_path)
        entities = analyze_and_contextualize(text)
        # Clean up temp files
        os.remove(file_path)
        os.rmdir(tmp_dir)
        # TODO: Identify why the entity output of the API does not have the keys in the same order that they are defined in the dictionary
        return jsonify({"message": "Successfully extracted entities", "entities": entities}), 200

    except Exception as e:
        return jsonify({"Server error.": str(e)}), 500


if __name__ == '__main__':
    app.run()
