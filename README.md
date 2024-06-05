# PineconeUtils

PineconeUtils is a Python module designed to handle and process data for embedding and indexing using Pinecone, Cohere, and OpenAI services. This utility module makes it easy to load, chunk, prepare, and upsert data into a Pinecone index, making it ideal for applications involving text embedding and retrieval systems(RAG).

## Features

- Load text data from `.txt`, `.docx`, and `.pdf` files.
- Chunk text data for processing.
- Prepare embeddings using either Cohere or OpenAI models.
- Upsert prepared data into a Pinecone index.

## Installation

To install PineconeUtils, you can use pip:

```bash
pip install pineconeutils
```


# Usage
Here's a quick example of how to use PineconeUtils:

## Setup
First, ensure you have the necessary API keys and setup information:
```bash
pinecone_api_key = "your_pinecone_api_key"
cohere_api_key = "your_cohere_api_key"
openai_api_key = "your_openai_api_key"
index_name = "your_index_name"
namespace_id = "your_namespace_id"
```

# Load Data
Load data from a supported file format:

```bash
from pineconeutils import PineconeUtils

# Create instance of PineconeUtils
pinecone = PineconeUtils(pinecone_api_key=cohere_api_key, openai_api_key=openai_api_key, index_name=index_name, namespace_id=namespace_id)

path = "path_to_your_file.docx"
data = pinecone.load_data(path)
print("Loaded Data:", data)
```

# Process Data
## Chunk and prepare data for embedding:

```bash
chunks = pinecone.chunk_data(data, chunk_size=100, chunk_overlap=10)
print("Data Chunks:", chunks)

prepared_data = pinecone.prepare_data(chunks, model="text-embedding-ada-002", service="openai")
```

# Upsert Data
## Upsert data into Pinecone index:

```bash
successful = pinecone.upsert_data(prepared_data)
print("Data upsertion was", "successful" if successful else "unsuccessful")
```

# Development

To contribute to the development of PineconeUtils, you can clone the repository and submit pull requests.

# Support
If you encounter any issues or have questions, please file an issue on the GitHub repository.

# License
This project is licensed under the MIT License - see the LICENSE file for details.



