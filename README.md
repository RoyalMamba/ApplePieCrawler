# ApplePieImageCrawler

This Python script, `objects.py`, is a versatile image crawler designed to download a large number of high-quality images from the web based on search queries provided in an Excel sheet. It utilizes the `icrawler` library, supporting parallel downloading for multiple search queries. The script creates separate folders for each search query, allowing for customization of search parameters to maximize the relevance of downloaded images.

## Getting Started

Before running the script, ensure you have the required Python libraries installed. You can install them using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare the Excel Sheet**: Create an Excel sheet with a column (e.g., 'Objects') containing the search queries. Each row represents a different search query (e.g., objects, personalities, etc.). Save the Excel sheet as 'ListofObjects.xlsx' (or any desired name) in the same directory as the script.

2. **Run the Script**: Execute the `objects.py` script to initiate the image download process. The script reads the search queries from the Excel sheet and creates separate folders for each search query in the 'ObjectsImages' directory (you can customize the output directory). It then downloads images corresponding to each search query.

```bash
python objects.py
```

3. **Customize Download Parameters**: You can customize various parameters within the script to control the download process:

   - `initial_num_images_to_download`: Set the initial number of images to download for each search query.
   - `output_directory`: Specify the directory where images will be saved. By default, it's set to 'ObjectsImages'.
   - `filters`: Adjust filters such as image size, date, color, and type based on your requirements.
   - `max_workers`: Control the number of concurrent download threads. Adjust this based on your system's capabilities.

## Maximizing Relevant Images

### Adjusting Image Size

By specifying a larger image size or resolution limit in the `filters`, you increase the chances of obtaining more relevant images. For example:

```python
filters = dict(
    size="large",  # Use 'large' for very large image sizes
    # Other filters...
)
```

This setting prioritizes larger, higher-quality images which are often more relevant than smaller images.

### Expanding Search Queries

To expand your search and gather a diverse range of images, you can modify the `search_queries` list. Add different combinations and variations of your search query:

```python
search_queries = [
    f'{personality}',
    f'people with {personality}',
    f'{personality} in an event',
    # Add more variations or combinations as needed
]
```

This approach broadens the search scope and brings in a wider variety of images related to your query.

## Downloading All Image Types

If you want to maximize the number of downloaded images without restricting by size or resolution, simply remove the `size` filter from the `filters` dictionary. This will allow the script to download all types of images, including icons, small, medium, and large images:

```python
filters = dict(
    # size="large",  # Remove or comment out this line to download all image sizes
    # Other filters...
)
```

## Advanced Configuration

For more advanced configurations, you can modify the script to use different search engines, adjust the number of images to download, or modify image filters according to your specific requirements.
You can interchange the `BingImageCrawler` and `GoogleImageCrawler` with each other to get the maximum results.

## Important Notes

- The script utilizes the Google Image search engine by default. If you want to use other search engines or sources, you can modify the script accordingly.
- Always be mindful of copyright and licensing when downloading images from the web. Ensure you have the necessary permissions to use the downloaded images for your intended purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize and extend this script to suit your specific image crawling needs. If you have any questions or need further assistance, please don't hesitate to reach out. Happy image crawling!
