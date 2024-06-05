from typing import List, Dict
import uuid
from .text_handler import TextHandler
from .docx_handler import DocxHandler
from .pdf_handler import PDFHandler
from .pinecone_services import PineconeServices
from .cohere_services import CohereServices
from .cohere_embedding import CohereEmbedding
from .openai_embedding import OpenAIEmbedding
from langchain.text_splitter import RecursiveCharacterTextSplitter

class PineconeUtils:
    def __init__(self, pinecone_api_key: str, index_name: str, cohere_api_key: str=None, openai_api_key: str=None, namespace_id: str=None):
        self.pinecone_services = PineconeServices(api_key=pinecone_api_key)
        self.cohere_api_key = cohere_api_key
        self.openai_api_key = openai_api_key
        self.index_name = index_name
        self.namespace_id = namespace_id

    def load_data(self, path: str) -> str:
        if path.endswith('.txt'):
            handler = TextHandler(path)
            return handler.read_text()
        elif path.endswith('.docx'):
            handler = DocxHandler(path)
            return handler.read_docx()
        elif path.endswith('.pdf'):
            handler = PDFHandler(path)
            return handler.read_pdf()
        else:
            raise ValueError("Unsupported file format")
        


    def chunk_data(self, data: str, chunk_size: int, chunk_overlap: int) -> List[str]:
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = splitter.create_documents([data])
        return [doc.page_content for doc in chunks]

    def prepare_data(self, chunks: List[str], model: str, service: str , input_type: str = None) -> List[Dict]:
        if service.lower() == "cohere":
            embedding_service = CohereEmbedding(api_key=self.cohere_api_key, input_type=input_type, model=model)
        elif service.lower() == "openai":
            embedding_service = OpenAIEmbedding(api_key=self.openai_api_key, model=model)
        else:
            raise ValueError("Unsupported service")
        
        data = []
        for chunk in chunks:
            data.append({
                'id': str(uuid.uuid4()),
                'values': embedding_service.get_embedding([chunk]),
                'metadata':{'text': chunk}
            })
        return data

    def upsert_data(self, data: List[Dict]):
        return self.pinecone_services.upsert_data(index_name=self.index_name, namespace_id=self.namespace_id, data=data, batch_size=100)



