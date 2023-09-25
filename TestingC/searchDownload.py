import os
import shutil
from googlesearch import search
from bs4 import BeautifulSoup
import requests

# List of famous personalities associated with Narendra Modi
famous_personalities = [
    "Barack Obama",
    "Angela Merkel",
    "Shinzo Abe",
    "Justin Trudeau",
    "Vladimir Putin",
    # Add more personalities to the list
]

# Specify the number of images to download for each personality
num_images_to_download = 10

# Create a folder for images if it doesn't exist
output_directory = "images"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Download images for each personality
for personality in famous_personalities:
    search_query = f"{personality} with Narendra Modi"
    image_count = 0

    # Perform image search using Google search
    for url in search(search_query, stop=num_images_to_download):
        try:
            # Fetch the web page content
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, "html.parser")

            # Find the image URL within the web page
            image_url = soup.find("meta", {"property": "og:image"})["content"]

            # Download the image and save it with a unique name
            image_response = requests.get(image_url)
            image_path = os.path.join(output_directory, f"{personality}_{image_count + 1}.jpg")
            with open(image_path, "wb") as f:
                f.write(image_response.content)

            image_count += 1

            print(f"Downloaded {personality} image {image_count}/{num_images_to_download}")

            if image_count >= num_images_to_download:
                break

        except Exception as e:
            print(f"Failed to download {personality} image {image_count + 1}: {str(e)}")

    print(f"Downloaded {image_count} images of {personality} with Narendra Modi.")
