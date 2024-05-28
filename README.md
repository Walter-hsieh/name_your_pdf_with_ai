# smartNamer.py

**smartNamer.py** is a Python script designed to rename PDF files based on their content using a language model.

## Overview

This script reads the content of each PDF file in the specified directory, generates a new name based on the content using a language model, and then renames the files accordingly.

## Features

- **Uses OpenAI's GPT-3.5-turbo language model**
- **Processes PDF content to generate meaningful file names**
- **Automates renaming of PDF files**

## How It Works

### Imports Required Libraries

- `ChatOpenAI` from `langchain_openai` to use OpenAI's language model.
- `PyPDFLoader` from `langchain_community.document_loaders` to load PDF files.
- Other necessary libraries such as `os` for file operations.

### Initialize the Language Model

The script initializes a `ChatOpenAI` model with specified parameters like temperature and model name.

```python
llm = ChatOpenAI(
    temperature=0, 
    model_name="gpt-3.5-turbo",
    api_key="openai_api_key"
)
```

### Define the PDF Directory

The variable `pdfs` holds the path to the directory containing PDF files.

```python
pdfs = 'C:\\Users\\walte\\Desktop\\pdf_ai_reader\\pdfs'
```

### List PDF Files

`files` contains the list of PDF files in the specified directory.

```python
files = os.listdir(pdfs)
```

### AI Reader Function

The function `ai_reader()` processes each PDF file, extracts its content, and uses the language model to generate a new name for the file based on its content.

- Constructs a prompt to instruct the language model to create a short but perfect file name based on the content.
- Uses `ChatPromptTemplate` and `StrOutputParser` to format the prompt and parse the response.
- Iterates over each PDF file, loads its content, and invokes the language model to generate a new name.
- Collects the generated names in a list `res`.

```python
def ai_reader():
    res = []
    user_input = 'create a short but perfect file name according to the content of the file provided'

    from langchain_core.prompts import ChatPromptTemplate
    rag_prompt = ChatPromptTemplate.from_messages([
        ("system", 'You are a helpful assistant. Use the following context when responding:\n\n{context}.'),
        ("human", "{question}")
    ])

    from langchain_core.output_parsers import StrOutputParser
    output_parser = StrOutputParser()
    rag_chain = rag_prompt | llm | StrOutputParser()

    for f in files:
        pdf_path = pdfs + f"\\{f}"
        loader = PyPDFLoader(file_path=pdf_path)
        documents = loader.load()
        response = rag_chain.invoke({
            "question": user_input,
            "context": documents
        })
        res.append(response)

    return res
```

### Rename Function

The `rename()` function takes the list of original file names and the generated names, then renames each file accordingly.

```python
def rename():
    names = ai_reader()
    print(names)
    for i, j in zip(files, names):
        old_file_path = pdfs + f"\\{i}"
        new_file_path = pdfs + f"\\{j}"
        os.rename(old_file_path, new_file_path)
```

### Main Function

The `main()` function calls the `ai_reader()` and `rename()` functions to perform the renaming operation.

```python
def main():
    ai_reader()
    rename()

main()
```
"# name_your_pdf_with_ai" 
