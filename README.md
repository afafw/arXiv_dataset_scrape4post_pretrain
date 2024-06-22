# arXiv Dataset Scraper

The arXiv Dataset Scraper is a tool designed for scraping datasets from the arXiv repository, specifically focusing on domains relevant for continued pretraining of machine learning models. This scraper utilizes the arXiv API to fetch datasets and relies on the open access interoperability provided by arXiv—special thanks to their team. The tool searches arXiv for specific keywords, such as 'ASD' and 'Autism Spectrum Disorder', and leverages GPT-4/deepseek-chat to filter and identify pertinent articles. The datasets are then downloaded from the mirror site at export.arxiv.org. The downloaded PDFs are converted to Markdown format using [Marker](https://github.com/VikParuchuri/marker), allowing for easier text processing and manipulation.

## Prerequisites

- It is recommended to use [Conda](https://docs.conda.io/en/latest/) for managing your Python environments, as this project was developed with Python 3.10.
- Ensure you have `git` installed to clone the repository.

## Setup and Installation

```bash
# Create a new Conda environment with Python 3.10
conda create -n py310 python=3.10 -y
# Activate the newly created environment
conda activate py310
# Clone the repository
git clone https://github.com/afafw/arXiv_dataset_scrape4post_pretrain.git
# Navigate to the project directory
cd arXiv_dataset_scrape4post_pretrain
# Install the required dependencies
pip install -r requirements.txt
```

## Usage Guide
1. **Fetch Article Names**: Run `Get_ALL_ARXIV_ARTICLE_NAMES.py` to collect all article names from arXiv and export them to `target_titles.csv`.
2. **Filter Unrelated Articles**: Before executing `filter_unrelated.py`, make sure to set the required environment variables. You can either create a `.env` file based on the provided `.env.example` or export the variables directly.
   - Sample `.env` file:
     ```
     OPENAI_API_KEY="your_api_key"
     OPENAI_BASE_URL="https://api.openai.com"
     USE_THIS_MODEL="gpt-4"
     ```
3. **Download Articles**: Use `download_filtered.py` to download the articles that have been identified as related.
4. **Convert PDFs to Markdown**: Convert the downloaded PDF files to Markdown format using Marker.
5. **Access Converted Files**: Check the `converted_pdf` directory for the Markdown-formatted articles.

```bash
python Get_ALL_ARXIV_ARTICLE_NAMES.py
python filter_unrelated.py
python download_filtered.py
# Assuming Marker is installed and in your PATH
marker ./downloaded_pdfs ./converted_pdf
```

