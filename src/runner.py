thonimport json
import logging
from pathlib import Path

from extractors.instagram_post_parser import InstagramPostParser
from outputs.exporters import JSONExporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
INPUT_FILE = DATA_DIR / "input_urls.txt"
OUTPUT_FILE = DATA_DIR / "sample_output.json"

def load_urls(file_path: Path):
    if not file_path.exists():
        logging.error(f"Input file not found: {file_path}")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    urls = load_urls(INPUT_FILE)
    if not urls:
        logging.warning("No URLs found to scrape.")
        return

    parser = InstagramPostParser()
    exporter = JSONExporter()

    results = []
    for url in urls:
        logging.info(f"Processing: {url}")
        try:
            data = parser.extract_post_data(url)
            results.append(data)
        except Exception as e:
            logging.error(f"Error scraping {url}: {e}")

    exporter.export(results, OUTPUT_FILE)
    logging.info(f"Saved output to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()