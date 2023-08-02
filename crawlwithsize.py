from icrawler.builtin import BingImageCrawler, GoogleImageCrawler
import os
from time import sleep
from concurrent.futures import ThreadPoolExecutor

# List of famous personalities associated with Narendra Modi
famous_personalities = '''Yogi Adityanath
Xi Jinping
Vijay Rupani
Donald Trump
Joe Biden
Shivraj Singh Chouhan
Ram Naik
Rajnath Singh
Nirmala Sitharaman
Ram Nath Kovind
Vladimir Putin
Sonia Gandhi
Ratan Tata
PV Sindhu
Ravi Shankar Prasad
Sharad Pawar
shinzo abe
YS Jagan Mohan Reddy
Yoweri K. Museveni
Yoshihide Suga
Droupadi Murmu
Benjamin Netanyahu
Jagat Prakash Nadda
Amit Shah
Uddhav Thackeray
Himanta Biswa Sarma
Akshay Kumar
Anthony Albanese
Antonio Costa
Anurag Thakur
Arun Jaitley
Arvind Kejriwal
B D Mishra
Barack Obama
Bhagwant mann
Bhupendrabhai Patel
Biswabhusan Harichandan
Borris Johnson
conrad sangma
Devendra Fadnavis
Eknath Shinde
Emmanuel Macron
Fumio Kishida
Gurinder Singh Dhillon
Gurmit Singh
Hema Malini
Hemant Soren
Justin Trudeau
Kamala Harris
L.K. Advani
mamta banerjee
Manik Saha
Manish Sisodia
Manmohan Singh
Manohar Lal Khattar
Manohar Parrikar
Manoj Tiwari
Mayawati
Melania Trump
Mohammed bin Salman Al Saud
Mukesh Ambani
Mulayam Singh Yadav
N. Biren Singh
Neeraj Chopra
Neiphiu Rio
Nita Ambani
Nitin Gadkari
Nitish Kumar
Olaf Scholz
P. S. Sreedharan Pillai
P.Chidambaram
Parmod Sawant
Piyush Goyal
PK Mishra
Pratibha Patil
Radha Mohan singh
Raghubar Das
Rahul Ghandhi
Ramdas Atvale
Recep Tayyip Erdogan
Reuven Rivlin
S Jaishankar
Sachin Tendulkar
Sheikh Mohammed bin Zayed Al Nahyan
Smriti Irani
Sushil Modi
Sushma Swaraj
Tejasvi Surya
Thawar Chand Gehlot
Uma Bharti
Ursula Von Der Leyen
Venkaiah Naidu
Vicky Kaushal
willem-alexander
Yogendra Yadav
'''

famous_personalities = famous_personalities.split('\n')

# Specify the initial number of images to download for each personality
initial_num_images_to_download = 50

# Maximum number of images to download for each personality
max_num_images_to_download = 400

# Create a folder for images if it doesn't exist
output_directory = "images"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Download images for each personality
def download(personality):
    # Create a folder for the current personality if it doesn't exist
    folder_name = os.path.join(output_directory, personality)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    search_queries = [f"{personality} with Narendra Modi", f"{personality}" , f'{personality} in an event']

    # Set up the BingImageCrawler
    bing_crawler = GoogleImageCrawler(
        downloader_threads=100, storage={"root_dir": folder_name}
    )
    bing_crawler.session.verify = False

    # Start with the initial number of images to download and gradually increase it
    num_images_to_download = initial_num_images_to_download
    while num_images_to_download <= max_num_images_to_download:
        for search_query in search_queries:
            # Specify the image filters and other parameters
            filters = dict(
                size="large",  # Use 'large' for very large image sizes
                # date=((2010, 1, 1), None),  # Filter images from 2010 onwards (change the date range if needed)
                color="color",  # Filter images by color type
                type="photo",  # Filter images by type (photo, clipart, face, lineart, etc.)
            )

            # Start image crawling with the specified filters
            bing_crawler.crawl(keyword=search_query, max_num=num_images_to_download, filters=filters)

        # Increase the number of images to download for the next iteration
        num_images_to_download *= 2

    print(f"Downloaded {max_num_images_to_download} images of {personality} with Narendra Modi together.")


# Use multiple search engines with concurrent downloading
with ThreadPoolExecutor(max_workers=95) as executor:
    futures = [executor.submit(download, personality) for personality in famous_personalities]
