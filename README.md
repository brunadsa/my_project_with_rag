# my_project_with_rag
A starter tutorial for building a Retrieval-Augmented Generation (RAG) application using LangChain, OpenAI, and ChromaDB to query custom PDF documents.

## Project Overview

This is a **Retrieval-Augmented Generation (RAG) starter project** that processes PDF documents for use with LangChain, OpenAI, and ChromaDB.

### Core Components

**main.py** - Entry Point
- Sets up file paths for PDF inputs and Markdown outputs
- Orchestrates the PDF-to-Markdown transformation process
- Uses logging to track execution progress

**transform_pdf_into_md.py** - PDF Processing Module
Contains three main functions:

1. **`transform_pdf_into_md()`** - Converts individual PDF files to Markdown
   - Validates that the PDF file exists
   - Uses the `pymupdf4llm` library to extract content with proper formatting (tables, fonts, etc.)
   - Saves the output as UTF-8 encoded Markdown

2. **`list_all_pdf_files()`** - Discovers PDFs
   - Recursively searches a directory for all `.pdf` files
   - Returns a list of file paths

3. **`transform_all_pdfs_in_directory()`** - Batch proScessor
   - Creates output directory if needed
   - Iterates through all PDFs in the source directory
   - Converts each one to Markdown and saves it with the same filename

### Data Structure
- **pdf_articles** - Input folder for PDF documents
- **md_articles** - Output folder for converted Markdown files (currently contains `2601.20415v1.md`)

### Purpose
This utility prepares PDF documents by converting them to Markdown format, which can then be indexed and searched by a RAG system for better document retrieval and question-answering capabilities.

## Python Environment

**Active Environment:** Python 3  
**Python Version:** 3.13.5 

### Key Dependencies
- `pymupdf4llm` - PDF to Markdown conversion with table and font preservation
- `loguru` - Enhanced logging functionality
- LangChain - RAG framework integration
- OpenAI - Language model API
- ChromaDB - Vector database for document retrieval

To create the virtual environment in Python, run:
```bash
python3 -m venv .venv
```

To activate the environment, run:
```bash
source .venv/bin/activate
```

To deactive the environment, run:
```bash
deactivate
```