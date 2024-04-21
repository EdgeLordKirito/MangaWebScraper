import sys
import os
import re

def create_input_file(folder_name, urls_file):
    # Read the URLs from the input file
    with open(urls_file, 'r') as file:
        urls = file.readlines()
    
    if not urls:
        print("URLs file is empty.")
        return
    
    # Create the folder if it doesn't exist
    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Create the input.txt file
    input_file_path = os.path.join(folder_path, 'input.txt')
    with open(input_file_path, 'w') as file:
        # Write each URL with corresponding chapter number
        for i, url in enumerate(urls, start=1):
            url = url.strip()
            if url:
                # Extract chapter number from the URL
                chapter_match = re.search(r'chapter-(\d+)[._-](\d+)', url, re.IGNORECASE)
                if chapter_match:
                    chapter_number = f"{chapter_match.group(1)}.{chapter_match.group(2)}"
                    chapter_name = f"{folder_name}_Chapter_{chapter_number}"
                else:
                    # If no decimal chapter number found, fall back to the enumeration
                    chapter_name = f"{folder_name}_Chapter_{i}"
                file.write(f"{url} {chapter_name}\n")
    
    print(f"Input file created: {input_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python DownloadManga.py <folder_name> <urls_file>")
        sys.exit(1)
    
    folder_name = sys.argv[1]
    urls_file = sys.argv[2]
    create_input_file(folder_name, urls_file)
