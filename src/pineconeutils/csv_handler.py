import os
import pandas as pd
from typing import List, Dict
from ensure import ensure_annotations

class CSVHandler:
    def __init__(self, path: str):
        self.path = path

    def read_csv(self, **kwargs) -> pd.DataFrame:
        return pd.read_csv(self.path, **kwargs)
    

    
