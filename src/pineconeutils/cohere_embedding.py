import os
import numpy as np
import cohere
from typing import List, Dict


class CohereEmbedding:
    def __init__(self, api_key: str , input_type: str , model: str):
        self.api_key = api_key
        self.input_type = input_type
        self.model = model


    def get_embedding(self, texts: list) -> np.ndarray:
        client = cohere.Client(self.api_key)
        response = client.embed(texts=texts, input_type=self.input_type, model=self.model).embeddings[0]
        return np.asarray(response).tolist()
    

