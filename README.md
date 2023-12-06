# Langchain Document Ingestion and Streamlit App

This repository includes scripts for downloading Langchain documents, ingesting them into Pinecone, and running a Streamlit app to explore the data.

## Getting Started

Follow these steps to set up and run the project:

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/serkanyasr/langchain-chatbot-explorer.git
    cd langchain-chatbot-explorer
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Download Langchain Documents:**
    Run the following command to download Langchain documents.
    ```bash
    python download_docs.py
    ```
     **or**
    ```bash
    wget -r -A.html -P langchain-docs https://api.python.langchain.com//latest/api_reference.html
    ```

4. **Update Pinecone API Key and Environment:**
    Open `ingest_docs.py` and replace the placeholders in the `init_pinecone` function with your Pinecone API key and environment.

5. **Ingest Documents into Pinecone:**
    Run the following command to process and send Langchain documents to Pinecone.
    ```bash
    python ingest_docs.py
    ```

6. **Run the Streamlit App:**
    Run the Streamlit app to explore the data.
    ```bash
    streamlit run app.py
    ```



https://github.com/serkanyasr/langchain-chatbot-explorer/assets/80819652/4445dd74-b3fc-4a62-a0ad-b66c7de246ae



## Project Structure

- `download_docs.py`: Script to download Langchain documents.
- `ingest_docs.py`: Script to ingest documents into Pinecone.
- `app.py`: Streamlit app to explore Langchain data.

## Configuration

- Update Pinecone API key and environment in `ingest_docs.py`.
- Configure Streamlit app in `app.py` if necessary.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
