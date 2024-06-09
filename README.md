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
TODO: Either create the postman collection files or replace testing method if using public hosting.

Ensure the application is running locally.\
Import the provided Postman collection for testing the API endpoints.\
Send a POST request to http://localhost:5000/api/v1/extract with the PDF files contained in\
'\Programming Challenge Files' attached in the request body.

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
- TODO: Identify key issues with API response (order of start and end entities does nto match dictionary definition.

## Work Item 4 – Finalize Requirements/Config/Readme, Push to Git
- **Time Estimate**: 30 minutes
- **Time Actual**: 1 hour
### Considerations:
- Used README for documentation and MIT license for repository.
- TODO: Create GitHub wiki page for full project documentation.
### Notes:
- Took longer than expected to write documentation, as we typically publish in madcap and have not used markdown before, and I classically underestimated how long properly documenting work takes

## Work Item 5 – Provide a Robust Method of Testing the Application
- **Time Estimate**: 30 minutes
- **Time Actual**: tbd
### Considerations:
- Consider adding a new endpoint for testing or writing test instructions.
- Consider outputting key categories and information to the client application.

## Work Item 6 – Answer Review Questions
- **Time Estimate**: 30 minutes
- **Time Actual**: tbd

## Contingency
- **Time Estimate**: 30 minutes

---

# Review Questions

1. **Technical Choices**:
   - Influence: Considered familiarity, research, and project requirements.
2. **Entity Contextualization**:
   - Approach: Utilized NLP models to provide context for identified entities.
3. **Error Handling**:
   - API handles errors through validation and structured responses.
4. **Challenges and Learnings**:
   - Challenges: New frameworks/tools, decision-making.
   - Learnings: Better understanding of Flask, NLP model selection.
5. **Improvement Propositions**:
   - Additional features: Improved testing, error handling, and NLP model fine-tuning.

