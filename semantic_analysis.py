def analyze_and_contextualize(text, nlp):
    """
    This function is used for semantic analysis of the PDF, specifically to
    contextualize medical literature with a focus on disease states and drugs.
    :param text: text returned from the parsed pdf
    :type text: string
    :return: entities
    :rtype: dictionary containing contextualized data, including:
     - the entity (excerpt of text) as string
     - the context of the entity as string
     - the start and end characters of the entity as integers
    """
    doc = nlp(text)
    entities = []
    for ent in doc.ents:

        # TODO: Improve the context entity as current programming does not yield desired results (full sentences).
        # TODO: Tailor entity identification to disease states, chemicals, APIs, antagonist/agonist sites.
        # Determine context size based on entity's position
        start_context = max(0, ent.start_char - 30)
        end_context = min(len(text), ent.end_char + 30)

        # Extend context to include complete words
        while start_context > 0 and not text[start_context].isspace():
            start_context -= 1
        while end_context < len(text) and not text[end_context].isspace():
            end_context += 1

        # Extract context
        context = text[start_context:end_context]

        # Ensure context contains complete sentences
        sentences = context.split('.')
        for i, sentence in enumerate(sentences):
            if ent.text in sentence:
                context = ' '.join(sentences[max(0, i - 1):i + 2])
                break

        entities.append({
            "entity": ent.text,
            "context": context,
            "start": ent.start_char,
            "end": ent.end_char
        })
    return entities
