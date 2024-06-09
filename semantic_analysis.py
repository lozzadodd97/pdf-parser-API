import spacy

# Define the NLP model
# nlp = spacy.load("en_core_sci_lg")
nlp = spacy.load("en_ner_bc5cdr_md")


def analyze_and_contextualize(text):
    """
    This function is used for semantic analysis of the PDF, specifically to
    contextualize medical literature with a focus on disease states and drugs.
    :param text: text returned from the parsed pdf
    :type text: string
    :return: entities
    :rtype: dictionary containing contextualized data, including:
     - the entity (excerpt of text)
     - the context of the entity
     - the start and end characters of the entity
    """
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append({
            "entity": ent.text,
            "context": text[max(0, ent.start_char-30):min(len(text), ent.end_char+30)],
            "start": ent.start_char,
            "end": ent.end_char
        })
    return entities
