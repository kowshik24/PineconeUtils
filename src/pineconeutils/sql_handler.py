import os
from typing import List, Dict




class SqlHandler:
    def __init__(self, path: str):
        self.path = path

    def read_sql(self) -> List[Dict]:
        with open(self.path, 'r') as f:
            data = f.readlines()
        return data
    
