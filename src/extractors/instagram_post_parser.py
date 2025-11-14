thonimport logging
import requests
from datetime import datetime
from .media_utils import extract_media_urls

class InstagramPostParser:
    """
    Simple Instagram scraper stub using public URLs.
    Returns structured data even if HTML parsing is limited.
    """

    def fetch_html(self, url: str) -> str:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text

    def extract_post_data(self, url: str) -> dict:
        try:
            html = self.fetch_html(url)
        except Exception as e:
            logging.error(f"Failed to load URL: {e}")
            html = ""

        photos, videos = extract_media_urls(html)

        return {
            "url": url,
            "user_posted": "unknown_user",
            "description": "Unable to extract caption in demo mode.",
            "hashtags": [],
            "num_comments": 0,
            "date_posted": datetime.utcnow().isoformat(),
            "likes": 0,
            "photos": photos,
            "videos": videos,
            "location": None,
            "latest_comments": [],
            "post_id": "N/A",
            "content_type": "Post",
            "video_view_count": 0,
            "video_play_count": 0,
            "followers": 0,
            "posts_count": 0,
            "profile_image_link": "",
            "is_verified": False,
            "is_paid_partnership": False,
            "audio": None,
            "profile_url": "",
        }