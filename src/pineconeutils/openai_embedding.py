import openai
from openai import OpenAI
import os
import numpy as np
from typing import List, Dict
from ensure import ensure_annotations



class OpenAIEmbedding:
    def __init__(self, api_key: str , model: str):
        self.api_key = api_key
        self.model = model
        

    def get_embedding(self, texts: list) -> np.ndarray:
        client = OpenAI(api_key=self.api_key)
        openai.api_key = self.api_key
        response = client.embeddings.create(model=self.model, input=texts)
        return np.asarray(response.data[0].embedding).tolist()
    


