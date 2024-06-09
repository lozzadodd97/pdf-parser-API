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
    if 'file' not in request.files:
        return jsonify({"error": "Bad request, file not included or empty filename."}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Bad request, file not included or empty filename."}), 400

    if not file.filename.endswith('.pdf'):
        return jsonify({"error": "Unsupported file type"}), 415

    try:
        file_path = os.path.join('/tmp', file.filename)
        file.save(file_path)

        text = extract_text(file_path)
        entities = analyze_and_contextualize(text)

        os.remove(file_path)
        # TODO: Identify why the entity output of the API does not have the keys in the same order that they are defined in the dictionary
        return jsonify(entities), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run()
