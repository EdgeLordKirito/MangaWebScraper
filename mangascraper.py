import sys
import os
import requests
from bs4 import BeautifulSoup

def print_green(text):
    print("\033[92m" + text + "\033[0m")

def print_red(text):
    print("\033[91;1m" + text + "\033[0m")

def download_images(url, folder_name):
    print_green(f"Starting {folder_name}")
    # Make a request to the webpage
    response = requests.get(url)
    if response.status_code != 200:
        print_red("Failed to retrieve webpage")
        return
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all img tags
    img_tags = soup.find_all('img')
    
    # Create the folder
    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Download each image
    for i, img_tag in enumerate(img_tags, start=1):
        img_url = img_tag.get('src')
        if img_url:
            img_extension = os.path.splitext(img_url)[1]
            img_path = os.path.join(folder_path, f"{i}{img_extension}")
            # Download the image
            with open(img_path, 'wb') as img_file:
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    img_file.write(img_response.content)
                    print(f"Downloaded: {os.path.basename(img_path)}")
                else:
                    print_red(f"Failed to download: {os.path.basename(img_path)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <url> <folder_name>")
        sys.exit(1)
    
    url = sys.argv[1]
    folder_name = sys.argv[2]
    download_images(url, folder_name)
