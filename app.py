import streamlit as st
from streamlit_chat import message
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv

load_dotenv()

INDEX_NAME = "langchain-document-index"

# Initialize Pinecone
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT_REGION"))


def run_llm(query: str, chat_history: list[dict[str, any]] = []) -> any:
    """
    Run the Language Model for Conversational Retrieval.

    This function utilizes the Langchain ChatOpenAI model and Pinecone vector store
    for Conversational Retrieval.

    Parameters:
    -----------
    query : str
        The user's query.
    chat_history : list[dict[str, any]], optional
        The chat history, defaults to an empty list.

    Returns:
    --------
    any
        The generated response.
    """
    embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    docsearch = Pinecone.from_existing_index(index_name=INDEX_NAME, embedding=embeddings)
    chat = ChatOpenAI(verbose=True, temperature=0, api_key=os.getenv("OPENAI_API_KEY"))

    qa = ConversationalRetrievalChain.from_llm(llm=chat, retriever=docsearch.as_retriever(), return_source_documents=True)
    return qa({"question": query, "chat_history": chat_history})


def create_source_string(source: set[str]) -> str:
    """
    Create a formatted string of source documents.

    Parameters:
    -----------
    source : set[str]
        Set of source document URLs.

    Returns:
    --------
    str
        Formatted string of source documents.
    """
    if not source:
        return "No source found"

    source_list = sorted(list(source))
    source_string = "Sources:\n"

    for i, src in enumerate(source_list, start=1):
        source_string += f"{i}. {src}\n"
    return source_string


def main():
    st.header("Explore the Depths of Langchain 🚀")
    
    prompt = st.text_input("Prompt:", placeholder="Curious about Langchain's knowledge? Ask away!")

    if "user_prompt_history" not in st.session_state:
        st.session_state["user_prompt_history"] = []
    if "chat_answers_history" not in st.session_state:
        st.session_state["chat_answers_history"] = []
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    if prompt:
        with st.spinner("Thinking..."):
            
            generated_response = run_llm(query=prompt, chat_history=st.session_state["chat_history"])
            source = set([doc.metadata["source"] for doc in generated_response["source_documents"]])
            formatted_response = f"{generated_response['answer']} \n\n {create_source_string(source)}"
            st.session_state["user_prompt_history"].append(prompt)
            st.session_state["chat_answers_history"].append(formatted_response)
            st.session_state["chat_history"].append((prompt, generated_response["answer"]))

    if st.session_state["chat_answers_history"]:
        for generated_response, user_query in zip(st.session_state["user_prompt_history"],
                                                  st.session_state["chat_answers_history"]):
            message(generated_response, is_user=True, avatar_style="personas")
            message(user_query)


if __name__ == "__main__":
    main()
