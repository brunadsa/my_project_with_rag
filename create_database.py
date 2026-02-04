# create_database.py


# Import necessary modules from LangChain
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document


from loguru import logger

def load_documents(DATA_PATH):
    """
    Loads all Markdown files in the given directory.
    Args:
        directory (str): The directory to search for markdown files.
    Returns:
        list: A list of paths to markdown files.
    """
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]):
    """
    Splits a list of Document objects into smaller chunks.
    Args:
        documents (list[Document]): The list of Document objects to split.
    Returns:
        list[Document]: A list of smaller Document chunks.
    """
    logger.info(f"Splitting {len(documents)} documents into smaller chunks.")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=500, length_function=len, add_start_index=True)
    chunks = text_splitter.split_documents(documents)
    logger.info(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    logger.info(f"Document content: {document.page_content}")
    logger.info(f"Document metadata: {document.metadata}")
    return chunks