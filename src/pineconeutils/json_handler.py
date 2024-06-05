import json
import os
from typing import List, Dict
from ensure import ensure_annotations


class JSONHandler:
    def __init__(self, path: str):
        self.path = path

    def read_json(self) -> List[Dict]:
        with open(self.path, 'r') as f:
            data = json.load(f)
        return data
    

