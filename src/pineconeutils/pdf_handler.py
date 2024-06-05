import os
import PyPDF2
from typing import List, Dict
from ensure import ensure_annotations



class PDFHandler:
    def __init__(self, path: str):
        self.path = path

    def read_pdf(self) -> str:
        pdf_file = open(self.path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = []
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text.append(page.extract_text())
        pdf_file.close()
        return '\n'.join(text)
    

