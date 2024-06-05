import os
import numpy as np
import cohere
from typing import List, Dict

class CohereServices:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def query_embedding(self, query: str, input_type: str, model: str) -> np.ndarray:
        client = cohere.Client(self.api_key)
        response = client.embed(texts=[query], input_type=input_type, model=model).embeddings[0]
        return np.asarray(response).tolist()

    def rerank_results(self, docs: List[str], query: str, model: str, top_n: int, rerank_fields: List[str] = None, return_documents: bool = False) -> List[Dict]:
        client = cohere.Client(self.api_key)
        if rerank_fields is None:
            if return_documents:
                response = client.rerank(query=query, documents=docs, model=model, top_n=top_n, return_documents=return_documents)
                return response
            else:
                response = client.rerank(query=query, documents=docs, model=model, top_n=top_n)
                return response
        else:
            if return_documents:
                response = client.rerank(query=query, documents=docs, model=model, top_n=top_n, rerank_fields=rerank_fields, return_documents=return_documents)
                return response
            else:
                response = client.rerank(query=query, documents=docs, model=model, top_n=top_n, rerank_fields=rerank_fields)
                return response
