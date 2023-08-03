from icrawler.builtin import GoogleImageCrawler
from icrawler import ImageDownloader
import os
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import openpyxl

workbook = openpyxl.load_workbook('ListofPersonalities.xlsx')
sheet = workbook['Objects']
Personalities = [personality[0] for personality in sheet.iter_rows(values_only=True, min_row=2)]
# Specify the initial number of images to download for each personality
initial_num_images_to_download = 100

# Create a folder for images if it doesn't exist
output_directory = "ObjectsImages"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)


# Download images for each personality
def download(personality):
    class CustomDownloader(ImageDownloader):
        def get_filename(self, task, default_ext):
            filename = os.path.basename(task['file_url'])
            return f"{search_query}_{filename}"

    # Create a folder for the current personality if it doesn't exist
    folder_name = os.path.join(output_directory, personality)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # search_queries = [f"{personality}", f"{personality}" , f'{personality} in an event']
    search_queries = [f'{personality}', f'people with {personality}']

    # Start with the initial number of images to download and gradually increase it
    num_images_to_download = initial_num_images_to_download
    for search_query in search_queries:
        # Specify the image filters and other parameters
        crawler = GoogleImageCrawler(
            downloader_cls=CustomDownloader,
            feeder_threads=2,
            parser_threads=4,
            downloader_threads=12,
            storage={"root_dir": folder_name}
        )
        crawler.session.verify = False

        filters = dict(
            size="large",  # Use 'large' for very large image sizes
            # date=((2010, 1, 1), None),  # Filter images from 2010 onwards (change the date range if needed)
            color="color",  # Filter images by color type
            type="photo",  # Filter images by type (photo, clipart, face, lineart, etc.)
        )

        # Start image crawling with the specified filters
        crawler.crawl(keyword=search_query, max_num=num_images_to_download, filters=filters)
        sleep(1)

        # Increase the number of images to download for the next iteration
        # num_images_to_download *= 2

    # print(f"Downloaded {max_num_images_to_download} images of {personality} with Narendra Modi together.")


# Use multiple search engines with concurrent downloading
with ThreadPoolExecutor(max_workers=95) as executor:
    futures = [executor.submit(download, personality) for personality in Personalities]
