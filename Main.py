import sys
import os
import subprocess

def multiscrape(input_file):
    print(f"Executing multiscrape for input file: {input_file}")
    current_dir = os.path.dirname(__file__)
    multiscrape_script = os.path.join(current_dir, "multiscrape.py")
    subprocess.run(["python", multiscrape_script, input_file])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main_script.py <name> <input_file>")
        sys.exit(1)
    
    name = sys.argv[1]
    input_file = sys.argv[2]

    # Construct the path to the nested input file
    nested_input_file = os.path.join(os.path.join(os.getcwd(), name), "input.txt")
    print(f"Executing main script for input file: {nested_input_file}")
    multiscrape(nested_input_file)
    print("Main script execution completed.")
    input("Press Enter to exit...")
