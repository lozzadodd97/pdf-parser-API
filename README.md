# Entity Extraction API

This application extracts and contextualizes entities from scientific literature PDFs using a publicly available NLP NER 
model and returns them via an API endpoint.

## Usage Instructions

### Cloning the Repository
Clone the repository using the following command:
```console
git clone -b "https://github.com/lozzadodd97/pdf-parser-API/"
cd pdf-parser-API
```

### Installation
Install Poetry for dependency management (if not yet installed):
```console
pip install poetry
poetry install
```
Install NLP NER models from Spacy used for semantic analysis:
```console
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_lg-0.4.0.tar.gz
```

### Running the Application Locally
Run the Flask application locally:
```console
poetry run python app.py
```

### Testing with Postman
- Ensure the application is running locally.\
- Install Postman and create a free account: https://www.postman.com/downloads/ 
- Import the provided Postman collection file ('API endpoint testing.postman_collection.json') for testing the API endpoints.
- Send the POST request to http://localhost:5000/api/v1/extract - Note that the pdf testing files are all included in the form body. When the request completes, use the postman search bar in the pretty output to find 'filename', noting there are 6 instances and the contextualized entities of all files are also present.
- To test the error handling, unselect all files and add two new files with the key 'file' to the form body. Add 'this_file_has_wrong_format.docx' and '.pdf' from '\Programming Challenge Files' attached in the request body. DISCLAIMER: Postman cloud uplaod did not work for these two files frustratingly, hence why you have to manually upload them sorry.
- Try to send the request with (a) no files, (b) .pdf and (c) this_file_has_wrong_format.docx, noting the differing error messages and codes.
- Try to send the request with a working pdf file and one that will create an error, noting that the error code is returned and the file is not processed.

Considerations:
- It would be good to allow errors to be recorded for individual files and reported as currently the first file containing an error attached to the form will determine the only error code.
- It may be better to allow any 'good' PDFs attached to still be processed, if desired behaviour.

## Contributors
Laurence Dodd

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# Solution Architecture

## Client Application
TODO: Build a website or at least use a public hosting service such as Render\
to replace the current local hosting using Postman.

- Sends a POST request to the API endpoint (`/api/v1/extract`) with PDF file(s) in the body.
- Waits for the response containing the extracted entities.

## Server Application
### API Framework (Flask)
- Receives the POST request with the PDF file.
- Validates the request to ensure a file is provided and is of the correct type.

### PDF Parser
- Extracts the text from the PDF file using the PyMuPDF library (fitz).

### NLP Model
- Processes the extracted text to identify entities using a pre-trained model from SciSpaCy.
  - NLP models to test for semantic analysis of biomedical texts:
    - `en_core_sci_lg` (large and more general to scientific text)
    - `en_ner_bc5cdr_md` (Chemicals and diseases from BC5CDR corpus)

### Response Formatter
- jsonify from flask formats the extracted entities and their context into a JSON response.


## Public Hosting (Bonus if time)
- Render – Provides a free tier suitable for hosting the API endpoint.

## Local Hosting / Testing
- Postman

## Development Environment
- PyCharm community edition (IDE)
- Poetry (Dependency management)
- Git (Version control and documentation)

---

# Project Implementation Plan, Workflow, and Effort

## Work Item 1 – Determine Solution Architecture
- **Time Estimate**: 5 minutes
- **Time Actual**: 10 minutes
### Considerations:
- Relevant experience: Creation of a website for project portfolio using Django.
- Unfamiliar with Flask, but expected benefits with less dev time.
- Research on PyMuPDF for PDF parsing and SciSpaCy for NLP.
- Research on approach to use for PDF parsing and contextualization to arrive at using PyMuPDF for its robustness and popularity, and Spacy given availability of strong NLP models specifically trained on scientific literature in the medical sector.

## Work Item 2 – Determine Project Implementation Plan and Workflow
- **Time Estimate**: 20 minutes
- **Time Actual**: 20 minutes
### Approach:
- Provided ChatGPT with the solution architecture as designed above and constraints of the API endpoint for guidance in creating a plan with code implementation details.

## Work Item 3 – Implement the MVP of the Server Application and Test Using Postman
- **Time Estimate**: 1 hour
- **Time Actual**: 1.5 hours
### Notes:
- Evaluated two NLP models and chose based on contextualization quality.

## Work Item 4 – Provide a Robust Method of Testing the Application
- **Time Estimate**: 30 minutes
- **Time Actual**: 1 hour
### Considerations:
- Do testing in Postman, providing collection files for testing and instructions in documentation.
- Make error handling of the api robust
- Consider outputting key or common categories and information to the client application.
- Allow api to process multiple files at once.
### Notes:
- Took longer than expected due to unfamiliarity of formatting responses using jsonify and overspent time improving the error handling and multiple file handling.

## Work Item 5 – Finalize Requirements/Config/Readme, Push to Git
- **Time Estimate**: 30 minutes
- **Time Actual**: 1 hour
### Considerations:
- Used README for documentation and MIT license for repository.
- TODO: Create GitHub wiki page for full project documentation.
### Notes:
- Took longer than expected to write documentation, as we typically publish in madcap and have not used markdown before, and I classically underestimated how long properly documenting work takes/ should have done this as I went along.


## Work Item 6 – Answer Review Questions
- **Time Estimate**: 30 minutes
- **Time Actual**: tbd


---

# Review Questions

1. **Technical Choices**:
    - What influenced your decision on the specific tools and models used?
2. **Entity Contextualization**:
   - How did you approach the problem of providing context for each identified entity?
3. **Error Handling**:
   - Can you describe how your API handles potential errors?
4. **Challenges and Learnings**:
   - What were the top challenges faced, and what did you learn from them?
5. **Improvement Propositions**:
   - Given more time, what improvements or additional features would you consider adding?
