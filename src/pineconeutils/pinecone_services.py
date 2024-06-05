from pinecone import Pinecone, ServerlessSpec
import itertools
from typing import List, Dict, Any


class PineconeServices:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def describe_index(self, index_name: str) -> Dict:
        pinecone = Pinecone(api_key=self.api_key)
        index = pinecone.Index(index_name)
        return index.describe_index_stats(index=index_name)
    
    def get_namespace_ids(self, index_name: str) -> List[str]:
       data = self.describe_index(index_name=index_name)
       namespace_ids = list(data['namespaces'].keys())
       return namespace_ids
    
    def createIndex(self,index_name: str , dimension: int , metric: str , cloud: str, region: str) -> bool:
        pinecone = Pinecone(api_key=self.api_key)
        if index_name not in pinecone.list_indexes():
            pinecone.create_index(index_name=index_name, dimension=dimension, metric=metric, cloud=cloud, region=region)
            return True
        else:
            return False
        
    def deleteIndex(self,index_name: str) -> bool:
        pinecone = Pinecone(api_key=self.api_key)
        if index_name in pinecone.list_indexes():
            pinecone.delete_index(index_name=index_name)
            return True
        else:
            return False
        
    def delete_data(self,index_name: str, namespace_id: str) -> bool:
        pinecone = Pinecone(api_key=self.api_key)
        index = pinecone.Index(index_name)
        try:
            index.delete(delete_all=True,namespace=namespace_id)
            return True
        except:
            return False
    
    def chunks(self, iterable, batch_size: int):
        """A helper function to break an iterable into chunks of size batch_size."""
        it = iter(iterable)
        chunk = list(itertools.islice(it, batch_size))
        while chunk:
            yield chunk
            chunk = list(itertools.islice(it, batch_size))

    def upsert_data(self, index_name: str, data: List[Dict[str, Any]], namespace_id: str=None, batch_size: int = 100) -> bool:
        pinecone = Pinecone(api_key=self.api_key)
        index = pinecone.Index(index_name)
        try:
            if namespace_id is None:
                for chunk in self.chunks(data, batch_size):
                    index.upsert(chunk)
            else:
                for chunk in self.chunks(data, batch_size):
                    index.upsert(chunk, namespace=namespace_id)
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        
    def query(self, index_name: str, query: str, top_k: int, namespace_id: str=None) -> List[Dict[str, Any]]:
        pinecone = Pinecone(api_key=self.api_key)
        index = pinecone.Index(index_name)
        if namespace_id is None:
            response = index.query(query=query, top_k=top_k)
        else:
            response = index.query(query=query, top_k=top_k, namespace=namespace_id)

        return response
    

