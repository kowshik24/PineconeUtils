import os
from setuptools import setup,find_packages
from typing import List



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

print("Current Directory: ", os.getcwd())
print("Current Files: ", os.listdir("."))

setup(
    name="pineconeutils",
    version="0.0.1",
    author="kowshik24",
    author_email="kowshikcseruet1998@gmail.com",
    description="Utilities for embedding and indexing with Pinecone, Cohere, and OpenAI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kowshik24/PineconeUtils",
    project_urls={"Bug Tracker": "https://github.com/kowshik24/PineconeUtils/issues"},
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements_dev.txt"),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
