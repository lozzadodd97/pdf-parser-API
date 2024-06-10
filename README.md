# Entity Extraction API

This application extracts and contextualizes entities from scientific literature PDFs using a publicly available NLP NER 
model and returns them via an API endpoint.

## Usage Instructions

### Cloning the Repository
Clone the repository using the following command:
```console
git clone -b main "https://github.com/lozzadodd97/pdf-parser-API/"
cd pdf-parser-API
```

### Installation
Install Poetry (if not yet installed) and install NLP NER models from Spacy used for semantic analysis:\
(unresolved issue: NLP model must be installed to env before dependencies to avoid conflict)
```console
pip install poetry
poetry shell
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_ner_bc5cdr_md-0.4.0.tar.gz
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.4.0/en_core_sci_lg-0.4.0.tar.gz
```
Build the virtual env:
```console
poetry install
```

### Running the Application Locally
Run the Flask application locally:
```console
poetry run python app.py
```

### Testing with Postman
- Ensure the application is running locally.
- Install Postman and create a free account: https://www.postman.com/downloads/ 
- Import the provided Postman collection file ('API endpoint testing.postman_collection.json') for testing the API endpoints.
- Send the POST request to http://localhost:5000/api/v1/extract - Note that the pdf testing files are all included in the form body. When the request completes, use the postman search bar in the pretty output to find 'filename', noting there are 6 instances and the contextualized entities of all files are also present.
- To test the error handling, unselect all files and add two new files with the key 'file' to the form body. Add 'this_file_has_wrong_format.docx' and '.pdf' from '\Programming Challenge Files' attached in the request body. DISCLAIMER: Postman cloud upload did not work for these two files frustratingly, hence why you have to manually upload them sorry.
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
- **Time Actual**: 45 minutes


---

# Review Questions

# Review Questions

## 1. Technical Choices: What influenced your decision on the specific tools and models used?

To design the solution architecture, I firstly considered my relevant experience with any similar tools and applications as per the task requirements. Most similarly, I created a portfolio website using Django whilst self-learning basic html and web-development. In this sense, I had a basic understanding of application building and APIs. Otherwise, I took some time to read a few blogs, watch some YouTube videos and discuss my options with ChatGPT. The final decisions I took were made on the following basis:

- **API** – I chose to use Flask rather than Django as my skill with the latter is rusty at best, and whilst Django provides more functionality it would require more dev time since it is inherently more complex than Flask, which is a microframework, fast to use out-of-the-box.
- **PDF parsing** – For this purpose, I had no prior experience but the library PyMuPDF appeared a popular option which was said to be robust. Considering the time constraint, I wanted to use only tools which were robust and would therefore yield minimal errors.
- **Semantic analysis** – I chose to use SciSpacy to find an NLP model for contextualization because it offers many models that are well-known, large and reportedly good, as well as some specific to the biomedical and pharmaceutical sectors. The two models I selected for testing were ‘en_core_sci_lg’, which is larger and more general to scientific text, and ‘en_ner_bc5cdr_md’, which is smaller and trained more specifically to identify chemicals and diseases from BC5CDR corpus. Additionally, the latter is also an NER model which I deemed would eventually be useful. After having produced a working MVP I used ChatGPT to compare two result excerpts from contextualization of the same pdf using the two models, and assessed the excerpts myself briefly. We both concluded the same thing, “Overall, based on the provided excerpts, Model 2 [en_ner_bc5cdr_md] appears to offer better contextualization of the biomedical data. It presents the entities in a more cohesive manner, facilitating a clearer understanding of the text.” Optimally, en_ner_bc5cdr_md also provides the following entity types which I thought would be useful in future improvement of the API response; DISEASE, CHEMICAL.
- **API Hosting** - For testing the API hosting I chose to use Postman since I had no experience with API hosting either locally or publicly, and this seemed like the most efficient way to arrive at an MVP and test. Later I would have liked to use Render for public hosting as a good learning opportunity, but time did not permit.
- **Dev environment** – I used PyCharm, Poetry and Git. I typically use PyCharm at work for software/data engineering orientated tasks as I like it for its in-built code suggestions that help to write clean code with best practices and seamless integration with git for version control. I had never used Poetry before but this seemed like a great choice to handle dependency management, which would be crucial for efficiently publishing a solution that was easy for others to test.

## 2. Entity Contextualization: How did you approach the problem of providing context for each identified entity?

Using the NLP model from spaCy, I first identify the named entities in the text. SpaCy provides a list of entities along with their positions in the text. To determine contextual range, for each entity, I simply defined a range either side of the start and end characters of the entity to extract a portion of surrounding text as context. This range was intended to provide enough surrounding words to provide sufficient context without adding unneeded verbosity. I also went an extra step to try and avoid truncation of words and ensure the context contained only full sentences. However, based on the output of the function you will notice this logic does not appear to be working correctly yet and presents an area for future improvement.

## 3. Error Handling: Can you describe how your API handles potential errors?

The API firstly runs checks for the following errors in this order: no file present, (for all files) empty file name (‘ .pdf’), unsupported type (not .pdf). Although the first two errors have the same code 400 they return specific messages. The final type returns code 415 as required. Otherwise, if an error occurs during file processing then a try and except statement ensures that the error code 500 and corresponding message are thrown out. 

The major design decision here was to allow multiple PDFs in the request body to be processed but first check if any single file contained an error and terminate the request. Ideally, error logging would be carried out and any valid PDF should be processed, however the programming exceeded the scope and time-allowance. Negatively, the request yields only the error code of the first error encountered and the remaining files are not processed.

## 4. Challenges and Learnings: What were the top challenges faced, and what did you learn from them?

The top challenges faced were:

- **Dependency management** – One major teething issue was discovering that installing the NLP model to the poetry env before the other dependencies for the application was key to avoiding a conflict which was not easily solvable to me on first inspection. This was completely unexpected as I only found the issue when writing up usage instructions but not during setup of the dev environment initially. I learnt to allow more time for contingency during testing to account for testing not only the application outputs but also the set-up process.
- **Writing documentation** - At work we generate our documentation in MadCap and the format is rather different to that taken for a typical software, e.g., we do not include usage instructions, content is more focused on the models purpose rather than programming, and I have not used markdown extensively. I learnt to write clear documentation in the typical README.md file and feel this will enable me to be more concise in giving future usage instructions in other dev activities. I also learnt to keep on top of this as I go along in future as writing up in retrospect can be more time-consuming.
- **Postman cloud storage** – Frustratingly, Postman gave me grief to upload the testing files to the cloud and I wasted some time troubleshooting what appeared to be an application bug. Resultantly, I had to request the user to add two files manually to the form body rather than it being included with the collection file import.
- **Time-management** – Writing code, particularly on unfamiliar ground and using tools never used before was expected to be hard within tough time constraints. For this reason I created a clear plan and effort estimates to stay focused and I found it really helped. In future I will like to apply this type project management to other smaller tasks I will do rather than saving it for large projects as I typically do. That being said I believe I spent closer to 5 hours of active time (ignoring the above issue with postman and dependency management), so I learnt that I need to focus on improving my efficiency too!

## 5. Improvement Propositions: Given more time, what improvements or additional features would you consider adding?

### NLP model:
- Improve the context entity as current programming does not yield desired results (full sentences without truncated words).
- Tailor entity identification to disease states, chemicals, APIs, antagonist/agonist sites. Optimally, en_ner_bc5cdr_md also provides the following entity types which I thought would be useful in future improvement of the API response; DISEASE, CHEMICAL.


### API handling:
- **Error Logging**:
  - Instead of immediately returning on errors, consider logging the errors and continuing with processing other files to provide a complete report at the end.
- **Detailed Error Reporting**:
  - Add error details to the `responses["errors"]` dictionary value for a more comprehensive response that includes both successes and failures.
- **Selective File Processing**:
  - Allow the processing to continue for valid files even if some files encounter errors.
- **Temporary Directory Management**:
  - Use a context manager for handling temporary directories and files to ensure better cleanup and error handling.

### PDF parsing:
- Consider whether the output could have been cleaner in any way, such as by removing `\n` where new lines were started, or cleaning the authors, affiliations and any other info from the PDF which may not have been relevant information for contextualization.

### Config:
- Consider whether the code can be made more robust by adding additional testing and design parameters to the configuration file. Such as by allowing the API mode to be changed from development to production.

### Test-Driven Development (TDD):
- I was remiss not to include any TDD in the scope due to time constraints, and all testing was left to manual checks via the API requests outputs. A `test.py` file should be added containing test cases for the application to ensure that the pdf parser, contextualizer and application run correctly, and that results remain consistent. This will improve automating of testing and code maintainability. Test cases can include unit tests, integration tests, and functional tests. To do this I would use `pytest` which is widely used because of its simplicity and usefulness.

