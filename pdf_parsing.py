import fitz #pymupdf


def extract_text(pdf_path):
    """
    This function uses PyMuPDF to parse the pdfs from the client server's POST
    :param pdf_path: the path of the pdf
    :type pdf_path: string
    :return: text of the pdf as a single concatenated string
    :rtype: string
    """
    loaded_doc = fitz.open(pdf_path)
    text = ""
    for page in loaded_doc:
        text += page.get_text(text)
    return text
