import sys
import os
import subprocess

def create_input_file(name, input_file):
    create_input_file_script = os.path.join(os.path.dirname(__file__), "createInputFile.py")
    command = f'python "{create_input_file_script}" "{name}" "{input_file}"'
    os.system(command)

def multiscrape(input_file):
    current_dir = os.path.dirname(__file__)
    mangascraper_script = os.path.join(current_dir, "mangascraper.py")
    
    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            parts = line.split(' ', 1)
            if len(parts) == 2:
                url, folder_name = parts
                print(f"Executing for folder: {folder_name}")
                mangascraper_abs_path = os.path.abspath(mangascraper_script)
                subprocess.run(["python", mangascraper_abs_path, url, folder_name])
            else:
                print("Invalid line format.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python multiscrape.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    multiscrape(input_file)
