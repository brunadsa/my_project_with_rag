# main.py
from loguru import logger
from pathlib import Path
from transform_pdf_into_md import transform_all_pdfs_in_directory
from create_database import load_documents, split_text

# Global variables 
# Define the directory containing PDF files and the output directory for Markdown files
pdf_directory = "data/pdf_articles"
md_output_directory = "data/md_articles"


if __name__ == "__main__":

    logger.info("Starting PDF to Markdown transformation process.")
    logger.info(f"Current Directory: {Path.cwd()}")
    # Transform all PDFs in the specified directory
    transform_all_pdfs_in_directory(pdf_directory, md_output_directory)
    logger.info("PDF to Markdown transformation process completed.")
    documents = load_documents(md_output_directory)
    chunks = split_text(documents)
    logger.info("Document loading and splitting process completed.")
