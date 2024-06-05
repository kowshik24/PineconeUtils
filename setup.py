import os
from setuptools import setup,find_packages
from typing import List

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("Base Directory: ", BASE_DIR)


HYPEN_E_DOT ="-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



with open('README.md', 'r') as f:
    long_description = f.read()


with open('README.md', 'r') as f:
    long_description = f.read()


print("Current Directory: ", os.getcwd())
print("Current Files: ", os.listdir("."))


__version__ = "0.0.3"
REPO_NAME = "PineconeUtils"
PKG_NAME = "pineconeutils"
AUTHOR_NAME = "kowshik24"
AUTHOR_EMAIL = "kowshikcseruet1998@gmail.com"



setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="PineconeUtils is a Python module designed to handle and process data for embedding and indexing using Pinecone, Cohere, and OpenAI services. This utility module makes it easy to load, chunk, prepare, and upsert data into a Pinecone index, making it ideal for applications involving text embedding and retrieval augmented systems(RAG)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements_dev.txt"),
)