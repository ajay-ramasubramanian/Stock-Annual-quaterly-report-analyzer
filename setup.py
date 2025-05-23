from setuptools import setup, find_packages

setup(
    name='fin-rag-agent',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'streamlit==1.28.0',
        'beautifulsoup4==4.11.1',
        'pandas==2.0.3',
        'numpy==1.24.3',
        'plotly==5.15.0',
        'langchain==0.0.267',
        'ollama==0.1.5',
        'chromadb==0.4.18',
        'requests==2.31.0',
        'sentence-transformers==2.2.2',
        'python-dotenv==1.0.0',
        'llama-index'
    ],
)
