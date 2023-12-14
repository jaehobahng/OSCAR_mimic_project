import os

def get_filenames(folder_path):
    """
    Retrieves all file names in the given directory "foler_path"
    """
    filenames = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            filenames.append(filename)
    return filenames


def get_folder_size(folder_path):
    """
    A funciton to retrieve folder size in order to check if duplicates were removed
    """
    # folder directory to check size
    total_size = 0
    # Start with size 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        # Creates list of filenames and the directory in a folder
        for filename in filenames:
            # Iterates through the list of filenames
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
            # adds size of every file into the original total_size
    return total_size

def format_size(size):
    """
    Convert bytes to a human-readable format (e.g., KB, MB, GB)
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0