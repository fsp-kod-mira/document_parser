import fitz
from docx import Document
from striprtf.striprtf import rtf_to_text
import docx2txt
import random

def extract_text_from_pdf(file_path):
    document = fitz.open(file_path)
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text


import chardet


"""
def extract_text_from_rtf(file_path):
    with open(file_path, 'r') as open_rtf_file:
        file_content_read = open_rtf_file.read()
        text_content = rtf_to_text(file_content_read)
    return text_content
"""

def extract_text_from_rtf(file_path):
    with open(file_path, 'rb') as open_rtf_file:
        raw_data = open_rtf_file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    
    with open(file_path, 'r', encoding=encoding) as open_rtf_file:
        file_content_read = open_rtf_file.read()
        text_content = rtf_to_text(file_content_read)
    
    return text_content


def extract_text_from_doc(file_path):
    with open(file_path, 'r') as open_rtf_file:
        file_content_read = open_rtf_file.read()    
        text = docx2txt.process(file_content_read)
    return text

def generate_random_name(ext):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    random_name = ''
    for i in range(10):
        random_name += random.choice(characters)
    return random_name + ext