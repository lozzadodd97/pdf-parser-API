import os
from pdf_parsing import extract_text

file = 'Enfothelial dysfunction.pdf'
folder_path = r'C:\Users\z004kp4a\OneDrive - Siemens AG\Documents\Admin\1, 36-38 Mildmay Park\Other\Every Cure - Data Scientist\PDF parsing API endpoint\Programming Challenge Files'
file_path = os.path.join(folder_path, file)
text = extract_text(file_path)
print(text)