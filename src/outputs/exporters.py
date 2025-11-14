thonimport json
import logging
from pathlib import Path

class JSONExporter:
    def export(self, data, output_path: Path):
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            logging.info(f"Exported {len(data)} items to {output_path}")
        except Exception as e:
            logging.error(f"Failed to write JSON: {e}")