import os
import re

def rename_files_sequentially(folder_path, prefix):
    """
    Renames all files in a given folder by giving them a new prefix and serial number.
    """
    # Change the current working directory to the target folder
    try:
        os.chdir(folder_path)
    except FileNotFoundError:
        print(f"Error: The folder path '{folder_path}' does not exist.")
        return

    files = [f for f in os.listdir() if os.path.isfile(f)] # List only files, not directories
    files.sort() # Sort files to ensure sequential numbering consistency

    if not files:
        print("No files were found in this directory.")
        return

    print(f"Found {len(files)} files. Starting rename process...")

    for i, old_file in enumerate(files, start=1):
        # Split the filename into name and extension
        name, extension = os.path.splitext(old_file)
        extension = extension.lower() # Standardize extension to lowercase

        # Construct the new filename (e.g., image_001.jpg)
        new_file_name = f"{prefix}_{i:03}{extension}" # :03 adds leading zeros for padding

        # Define full paths for the rename operation
        src = os.path.join(folder_path, old_file)
        dst = os.path.join(folder_path, new_file_name)

        # Safely rename the file, checking for existing destination file
        if not os.path.exists(dst):
            try:
                os.rename(src, dst)
                print(f"✅ Renamed: {old_file} -> {new_file_name}")
            except OSError as e:
                print(f"Skipping {old_file} due to OS error: {e}")
        else:
            print(f"Skipping {old_file} → {new_file_name}: destination file already exists")

    print("Renaming process complete.")

# --- Usage Example ---
# Specify your folder path and desired prefix
# For Windows paths, use double backslashes (\\\\) or a raw string (r'C:\Users\...')
# For this example, ensure the script is run in a directory with a 'test_files' subfolder
folder_to_rename = os.path.join(os.getcwd(), 'test_files')
new_prefix = 'vacation_photo'

# Run the renamer function
rename_files_sequentially(folder_to_rename, new_prefix)
