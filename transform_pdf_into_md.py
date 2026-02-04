# transform_pdf_into_md.py

# Standard library imports
import pymupdf4llm
from pathlib import Path
import os
from loguru import logger

# Function to transform a single PDF file into a Markdown file
def transform_pdf_into_md(pdf_path: str, md_output_path: str) -> None:
    """
    Transforms a PDF file into a Markdown file.
    
    Args:
        pdf_path (str): The path to the input PDF file.
        md_output_path (str): The path to the output Markdown file.
    
    Returns:
        None"""
    # 1. Check if file exists
    path = Path(pdf_path)
    if not path.exists():
        logger.error(f"Error: {pdf_path} not found.")
        return

    # 2. Convert PDF to Markdown text
    # This library handles tables and font styles automatically
    md_text = pymupdf4llm.to_markdown(pdf_path)

    # 3. Save the output
    with open(md_output_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    
    logger.success(f'Transforming PDF: {pdf_path} to Markdown: {md_output_path}... - Done.')


def list_all_pdf_files(directory: str) -> list:
    """
    Lists all PDF files in the given directory.

    Args:
        directory (str): The directory to search for PDF files.
    Returns:
        list: A list of paths to PDF files.
    """
    logger.info(f"Listing all PDF files in directory: {directory}")
    pdf_files = []
    path = Path(directory)
    for file in path.rglob("*.pdf"):
        pdf_files.append(str(file))
    return pdf_files

def transform_all_pdfs_in_directory(pdf_directory: str, md_output_directory: str) -> None:
    """
    Transforms all PDF files in a given directory into Markdown files.

    Args:
        pdf_directory (str): The directory containing PDF files.
        md_output_directory (str): The directory to save the Markdown files.
    
    Returns:
        None
    """
    # Ensure the output directory exists
    os.makedirs(md_output_directory, exist_ok=True)

    # List all PDF files in the specified directory
    pdf_files = list_all_pdf_files(pdf_directory)

   # Transform each PDF file into a Markdown file
    for pdf_file in pdf_files:
        md_file_name = os.path.splitext(os.path.basename(pdf_file))[0] + ".md"
        md_file_path = os.path.join(md_output_directory, md_file_name)
        logger.info(f'Transforming PDF: {pdf_file} to Markdown: {md_file_path}...')
        transform_pdf_into_md(pdf_file, md_file_path)