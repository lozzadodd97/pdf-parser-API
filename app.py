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

    # Create list of file objects
    files = request.files.getlist('file')
    # Error handling
    # No file present error
    if not files:
        return jsonify({"error": "Bad request, file not included."}), 400
    # Check for errors
    for file in files:
        # Empty file name error
        if file.filename == '' or file.filename == '.pdf':
            return jsonify({"error": "Bad request, empty filename."}), 400
        # File is not supported type (pdf) error
        if not file.filename.endswith('.pdf'):
            return jsonify({"error": "Unsupported file type"}), 415
        # TODO: Allow server errors to be recorded and any 'good' PDFs attached to still be processed (unsure if desired behaviour)

    # Create dictionary to store results
    responses = {
        "errors": [],
        "results": []
    }
    # Ensure temp directory exists
    tmp_dir = '/tmp'
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    # Process the request
    for file in files:
        try:
            # Save file to temp
            file_path = os.path.join(tmp_dir, file.filename)
            file.save(file_path)
            # Parse and contextualize
            text = extract_text(file_path)
            entities = analyze_and_contextualize(text)
            # Add responses
            responses["results"].append({
                "filename": file.filename,
                "entities": entities
            })
            # Clean up temp files
            os.remove(file_path)
        # TODO: Allow server error to be recorded for individual files
        except Exception as e:
            return jsonify({"Server error.": str(e)}), 500
    # Clean up temp directory
    os.rmdir(tmp_dir)
    return jsonify({"message": "Processing completed", "responses": responses["results"]}), 200

if __name__ == '__main__':
    app.run()
