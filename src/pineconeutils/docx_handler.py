import os
from pathlib import Path
import docx
from typing import List, Dict
from ensure import ensure_annotations

class DocxHandler:
    def __init__(self, path: str):
        self.path = path

    def read_docx(self) -> str:
        doc = docx.Document(self.path)
        return '\n'.join([paragraph.text for paragraph in doc.paragraphs])



