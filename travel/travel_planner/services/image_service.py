import requests
import os
import hashlib
from PIL import Image
from io import BytesIO
from config.settings import GOOGLE_SEARCH_API_KEY, GOOGLE_CSE_ID

# Image Cache Directory
IMAGE_CACHE_DIR = "static/images"
os.makedirs(IMAGE_CACHE_DIR, exist_ok=True)  # Ensure directory exists

def get_relevant_image(query):
    import requests
import os
import hashlib
from PIL import Image
from io import BytesIO
from config.settings import GOOGLE_SEARCH_API_KEY, GOOGLE_CSE_ID

# Directory to cache images
IMAGE_CACHE_DIR = "static/images"
os.makedirs(IMAGE_CACHE_DIR, exist_ok=True)

def get_first_image(query):
    """
    Fetch the first valid image URL from Google Custom Search (excluding Wikimedia), 
    download it, resize, and return the local file path.
    """
    try:
        # Generate a unique filename using an MD5 hash of the query
        query_hash = hashlib.md5(query.encode()).hexdigest()
        local_path = os.path.join(IMAGE_CACHE_DIR, f"{query_hash}.jpg")

        # If the image is already cached, return the local path
        if os.path.exists(local_path):
            return f"/{local_path}"

        # Google Custom Search API endpoint
        search_url = "https://www.googleapis.com/customsearch/v1"
        # Use a query filter to exclude Wikimedia/Wikipedia results
        params = {
            "q": f"{query} -site:wikimedia.org -site:wikipedia.org",
            "cx": GOOGLE_CSE_ID,
            "key": GOOGLE_SEARCH_API_KEY,
            "searchType": "image",
            "num": 50  # Retrieve multiple results to choose the best one
        }
        
        response = requests.get(search_url, params=params, timeout=5)
        if response.status_code != 200:
            print("⚠️ Google API error:", response.text)
            return "/static/images/placeholder.jpg"
        
        results = response.json().get("items", [])
        image_url = None
        
        # Iterate over results and select the first URL that is not from Wikimedia
        for result in results:
            url = result["link"]
            if "wikimedia" not in url.lower() and "wikipedia" not in url.lower():
                image_url = url
                break
        
        if not image_url:
            print("⚠️ No valid image found.")
            return "/static/images/placeholder.jpg"
        
        # Download the image and process it
        img_response = requests.get(image_url, stream=True, timeout=5)
        if img_response.status_code == 200:
            img = Image.open(BytesIO(img_response.content))
            img = img.convert("RGB")  # Ensure image is in RGB mode
            img.thumbnail((800, 400))  # Resize image for performance
            
            # Save the processed image locally
            img.save(local_path, "JPEG", quality=85)
            return f"/{local_path}"
        
        print("⚠️ Failed to download image.")
        return "/static/images/placeholder.jpg"
        
    except Exception as e:
        print("⚠️ Error fetching image:", e)
        return "/static/images/placeholder.jpg"
