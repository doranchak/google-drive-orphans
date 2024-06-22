import os
import subprocess
import argparse

def has_extended_attribute(file_path, attribute):
    try:
        # Use xattr command to get the list of extended attributes for the file
        output = subprocess.check_output(['xattr', file_path]).decode()
        # Check if the specific attribute is in the list
        return attribute in output
    except subprocess.CalledProcessError:
        # If xattr command fails, assume the attribute does not exist
        return False

def find_files_without_attribute(folder_path, attribute):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if not has_extended_attribute(file_path, attribute):
                print(f"{file_path}")

def main():
    parser = argparse.ArgumentParser(description="Find files without a specific extended attribute.")
    parser.add_argument("folder_path", help="Path to the folder to examine")
    args = parser.parse_args()

    attribute = 'com.google.drivefs.item-id#S'
    print(f"Looking for orphans in {args.folder_path}:")
    find_files_without_attribute(args.folder_path, attribute)

if __name__ == "__main__":
    main()
