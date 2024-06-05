import os
import pandas as pd
from typing import List, Dict
from ensure import ensure_annotations

class ExcelHandler:
    def __init__(self, path: str):
        self.path = path

    def read_excel(self, **kwargs) -> pd.DataFrame:
        return pd.read_excel(self.path, **kwargs)
    


