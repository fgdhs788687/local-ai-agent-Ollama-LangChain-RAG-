from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a pizza restaurant

Here are some relavant reviews: {reviews}

Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 

while True:
    question = input("ask your question (q or Q to quit): ")
    if question == 'q' or question == 'Q':
        break

    reviews = retriever.invoke(question)
    print("\n\n")
    result = chain.invoke({"reviews": reviews,"question": question})
    print(result)
    print("\n\n")

