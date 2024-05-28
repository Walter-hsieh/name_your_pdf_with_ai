from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from rename import numbering, rename

pdfs_dir = 'C:\\Users\\walte\\Desktop\\smartNamer\\pdfs_test'

def ai_reader(api, pdfs_dir):

    files = numbering(pdfs_dir)
    
    llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    google_api_key=api)

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
        if len(context) > 32800 :  # Adjust this limit as needed
            context = context[:32800 ]

        # Initiate the LLM response
        response = rag_chain.invoke({
            "question": user_input,
            "context": context
        })

        res.append(response.strip())
        print(response)
    
    rename(pdfs_dir, res)



def main():
    names = ai_reader(pdfs_dir)


if __name__ == "__main__":
    main()



