from google_images_download import google_images_download
import os
import shutil

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
    # Replace double quotes with underscores in the search query
    search_query = f'{personality} with Narendra Modi after_2022_01_01'

    # Set the arguments for image download
    arguments = {
        "keywords": search_query,
        "limit": num_images_to_download,
        "output_directory": output_directory,
        "format": "jpg",
    }

    # Download images
    response = google_images_download.googleimagesdownload()
    paths = response.download(arguments)

    print(f"Downloaded {len(paths[0][search_query])} images of {personality} with Narendra Modi.")
