import os
import requests
from urllib.parse import urljoin

def download_docs(base_url, output_dir):
    """
    Download Langchain documents from the specified base URL and save them to the output directory.

    Parameters:
    -----------
    base_url : str
        The base URL from which documents will be downloaded.
    output_dir : str
        The directory where downloaded documents will be saved.

    Returns:
    --------
    None
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Send a request to the base URL
    response = requests.get(base_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        html_content = response.text

        # Find all links ending with ".html"
        links = [link.split('"')[1] for link in html_content.split("href=") if link.endswith(".html")]

        # Download each HTML file
        for link in links:
            absolute_url = urljoin(base_url, link)
            file_name = os.path.join(output_dir, os.path.basename(link))
            file_response = requests.get(absolute_url)

            if file_response.status_code == 200:
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(file_response.text)
                print(f"Downloaded: {file_name}")
            else:
                print(f"Failed to download: {absolute_url}")

if __name__ == "__main__":
    base_url = "https://api.python.langchain.com/en/latest/api_reference.html"
    output_directory = "langchain-docs"
    download_docs(base_url, output_directory)
