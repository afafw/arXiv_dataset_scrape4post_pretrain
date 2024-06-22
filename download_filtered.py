import os
import csv
import requests
from concurrent.futures import ThreadPoolExecutor

def extract_arxiv_id(arxiv_url):
    # Extract the arXiv ID from the URL
    return arxiv_url.split('/')[-1]

def download_arxiv_article(arxiv_url, output_folder):
    try:
        arxiv_id = extract_arxiv_id(arxiv_url)
        pdf_url = f"https://export.arxiv.org/pdf/{arxiv_id}.pdf"

        response = requests.get(pdf_url)
        if response.status_code == 200:
            filename = os.path.join(output_folder, f"{arxiv_id}.pdf")
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Error downloading: {pdf_url}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    csv_file = 'filtered.csv'
    output_folder = 'downloaded_pdfs'
    os.makedirs(output_folder, exist_ok=True)

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        urls_to_download = [row['Entry_ID'] for row in reader]

    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in urls_to_download:
            executor.submit(download_arxiv_article, url, output_folder)

    print(f"Downloaded arXiv articles to {output_folder}")

if __name__ == "__main__":
    main()
