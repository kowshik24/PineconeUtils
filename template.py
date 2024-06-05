import os
from pathlib import Path

package_name = "pineconeutils"

list_of_files = [
   ".github/workflows/ci.yaml",
   "src/__init__.py",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/pinecone_services.py",
   f"src/{package_name}/openai_services.py",
   f"src/{package_name}/cohere_services.py",
   f"src/{package_name}/utils.py",
   f"src/{package_name}/data_handler/__init__.py",
    f"src/{package_name}/data_handler/pdf_handler.py",
    f"src/{package_name}/data_handler/csv_handler.py",
    f"src/{package_name}/data_handler/excel_handler.py",
    f"src/{package_name}/data_handler/json_handler.py",
    f"src/{package_name}/data_handler/sql_handler.py",
    f"src/{package_name}/data_handler/docx_handler.py",
    f"src/{package_name}/data_handler/html_handler.py",
    f"src/{package_name}/data_handler/text_handler.py",
    f"src/{package_name}/embeddings/__init__.py",
    f"src/{package_name}/embeddings/openai_embedding.py",
    f"src/{package_name}/embeddings/cohere_embedding.py",
    f"src/{package_name}/data_upsert/__init__.py",
    f"src/{package_name}/data_upsert/upsert_data.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/unit/unit.py",
   "tests/integration/__init__.py",
   "tests/integration/int.py",
   "init_setup.sh",
   "requirements.txt",
   "requirements_dev.txt", 
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "experiments/experiments.ipynb", 
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file