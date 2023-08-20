import os
from concurrent.futures import ThreadPoolExecutor

directory = r"A:\text"

def delete_file(file_path):
    os.remove(file_path)

with ThreadPoolExecutor(max_workers=100) as executor:
    files_to_delete = [os.path.join(directory, filename) for filename in os.listdir(directory)]
    for file_path in files_to_delete:
        executor.submit(delete_file, file_path)