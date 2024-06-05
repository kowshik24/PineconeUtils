import os
from typing import List, Dict
from ensure import ensure_annotations


class TextHandler:
    def __init__(self, path: str):
        self.path = path

    def read_text(self) -> str:
        with open(self.path, 'r') as f:
            data = f.readlines()
        return '\n'.join(data)
    


