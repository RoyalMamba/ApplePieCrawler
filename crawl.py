from icrawler.builtin import BingImageCrawler
import os
from time import sleep
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

# Specify the number of images to download for each personality
num_images_to_download = 25

# Create a folder for images if it doesn't exist
output_directory = "images"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Download images for each personality
for personality in famous_personalities:
    # Create a folder for the current personality if it doesn't exist
    folder_name = os.path.join(output_directory, personality)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    search_query = f"{personality} with Narendra Modi"

    # Set up the BingImageCrawler
    bing_crawler = BingImageCrawler(
        downloader_threads=8, storage={"root_dir": folder_name}
    )

    sleep(1)

    # Specify the image size (large) and other filters
    filters = dict(
        size="large",  # Use 'large' for very large image sizes
        # date=((2010, 1, 1), None),  # Filter images from 2010 onwards (change the date range if needed)
        color="color",  # Filter images by color type
        type="photo",  # Filter images by type (photo, clipart, face, lineart, etc.)
    )

    # Start image crawling with the specified filters
    bing_crawler.crawl(keyword=search_query, max_num=num_images_to_download, filters=filters)

    print(f"Downloaded {num_images_to_download} images of {personality} with Narendra Modi together.")

