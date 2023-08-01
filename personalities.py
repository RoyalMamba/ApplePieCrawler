import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

# Function to download images for a given search query
def download_images(query, num_images=10):
    search_url = f"https://www.google.com/search?q={quote(query)}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    image_urls = [img["src"] for img in soup.find_all("img") if img.get("src")]

    # Create a folder for the personality's images
    folder_name = query.replace(" ", "_")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Download images
    for i, url in enumerate(image_urls[:num_images]):
        try:
            image_response = requests.get(url)
            image_path = os.path.join(folder_name, f"{query}_{i+1}.jpg")
            with open(image_path, "wb") as f:
                f.write(image_response.content)
            print(f"Downloaded {query} image {i+1}/{num_images}")
        except Exception as e:
            print(f"Failed to download {query} image {i+1}: {str(e)}")

# List of famous personalities associated with Narendra Modi
famous_personalities = [
    'Narendra modi with Hemant Soren'
    # Add more personalities to the list
]

# Download images for each personality
for personality in famous_personalities:
    download_images(personality, num_images=50)
