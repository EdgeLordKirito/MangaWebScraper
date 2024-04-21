#!/bin/bash

# Get the directory of the script
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Check if two command-line arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <name> <input_file>"
    exit 1
fi

# Run CreateInputFile.py with name and inputfile
python3 "$script_dir/CreateInputFile.py" "$1" "$2"

# Change directory to the newly created folder
cd "$1" || exit

# Run multiscrape on input.txt
python3 "$script_dir/multiscrape.py" input.txt

# Move back to the original directory
cd ..

# Pause the script to keep the terminal window open
read -p "Press Enter to exit..."
