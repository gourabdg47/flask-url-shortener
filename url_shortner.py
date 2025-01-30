import re
import os
import json
import random
import string

def code_generator(length=6):
    """Generate a random alphanumeric code of given length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def is_valid_url(url):
    """Validate if the given URL is in correct format."""
    pattern = re.compile(
        r'^(https?:\/\/)?'  # Optional "http" or "https"
        r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}'  # Domain (e.g., "example.com")
        r'(:\d{1,5})?'  # Optional port (e.g., ":8080")
        r'(\/[^\s]*)?$'  # Optional path (e.g., "/path/to/page")
    )
    return bool(pattern.match(url))

def get_unique_filename(base_name="default.json"):
    """Generate a unique filename if the base file already exists."""
    if not os.path.exists(base_name):
        return base_name

    counter = 1
    while True:
        new_name = f"{os.path.splitext(base_name)[0]}_{counter}.json"
        if not os.path.exists(new_name):
            return new_name
        counter += 1

def read_json(file_name="default.json"):
    """Load JSON data from a file, returning an empty dictionary if missing or corrupted."""
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def write_json(data, json_file="default.json"):
    """Save dictionary data to a JSON file."""
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)

def get_original_url(short_code, json_file="default.json"):
    url_data = read_json(json_file)
    if short_code in url_data:
        # url_data[short_code]["clicks"] = url_data[short_code].get("clicks", 0) + 1

        return url_data[short_code]

def add_click(short_code, json_file="default.json"):
    url_data = read_json(json_file)
    if short_code in url_data:
        url_data[short_code]['clicks'] += 1
        write_json(url_data, json_file)

def get_stat(short_code, json_file='default.json'):
    url_data = read_json(json_file)
    if short_code in url_data:
        return url_data[short_code]

def url_engine(url=None):
    """Shorten a URL and store it in a JSON file."""

    if not url or not is_valid_url(url):
        print("Invalid URL. Please provide a valid URL.")
        return None

    url_code = code_generator()
    json_file = "default.json"

    if not os.path.exists(json_file):
        json_file = get_unique_filename(json_file)

    url_data = read_json(json_file)

    while url_code in url_data:
        url_code = code_generator()

    url_data[url_code] = {
        'url': url,
        'clicks': 0
    }
    write_json(url_data, json_file)

    print(f"Shortened URL: {url_code} -> {url}")
    return url_code

def main(original_url):
    """Main function for testing."""

    short_code = url_engine(original_url)
    if short_code:
        print(f"Generated Short Code: {short_code}")
    return short_code

