thonimport re

def extract_media_urls(html: str):
    """
    Attempts to extract image and video URLs using regex.
    Simple fallback logic suitable for demo purposes.
    """

    image_pattern = r'https?://[^"]+\.jpg'
    video_pattern = r'https?://[^"]+\.mp4'

    photos = re.findall(image_pattern, html) or []
    videos = re.findall(video_pattern, html) or []

    return photos, videos