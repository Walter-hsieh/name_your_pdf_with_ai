from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os


# Initialize the OpenAI chat model
llm = ChatOpenAI(
    temperature=0, 
    model_name="gpt-3.5-turbo",
    api_key="openai_api_key"
    )

# Directory containing the PDFs
pdfs_dir = 'C:\\Users\\walte\\Desktop\\smartNamer\\pdfs'
origin_files = os.listdir(pdfs_dir)

i=0
for file in origin_files:
    old_file_path = os.path.join(pdfs_dir, file)
    new_file_path = os.path.join(pdfs_dir, f"{str(i)}.pdf")
    print(new_file_path)
    os.rename(old_file_path, new_file_path)
    i+=1


files = os.listdir(pdfs_dir)

def ai_reader():

    res = []

    # Static question for LLM
    user_input = 'Based on file provided, generate a file name in this foramt:[Year]_[Main Topic]_[Specific Focus]_[Geographic Area].pdf. Please do not give any response except for the file name.'
    # Instruction for LLM to generate the response
    rag_prompt = ChatPromptTemplate.from_messages([
        ("system", 'You are a helpful assistant. Use the following context when responding:\n\n{context}.'),
        ("human", "{question}")
    ])

    # Organize LLM's response into structured output
    output_parser = StrOutputParser()
    rag_chain = rag_prompt | llm | StrOutputParser()


    for f in files:
        pdf_path = os.path.join(pdfs_dir, f)
        loader = PyPDFLoader(file_path=pdf_path)
        documents = loader.load_and_split()


        # Summarize document content to avoid exceeding token limit
        context = " ".join(page.page_content for page in documents)
        if len(context) > 16385 :  # Adjust this limit as needed
            context = context[:16385 ]

        # Initiate the LLM response
        response = rag_chain.invoke({
            "question": user_input,
            "context": context
        })

        res.append(response)
        print(response)

    return res

def rename():
    names = ai_reader()
    print(names)
    for old_name,new_name in zip(files, names):
        old_file_path = os.path.join(pdfs_dir, old_name)
        new_file_path = os.path.join(pdfs_dir, new_name)
        os.rename(old_file_path,new_file_path)



def main():
    rename()

if __name__ == "__main__":
    main()



