import subprocess
import os

# The path to the SPOTS-10 repository
repo_path = 'https://github.com/Amotica/SPOTS-10/raw/refs/heads/main/'
# The four files to download (in repo_path + dataset/)
files = ['dataset/test-images-idx3-ubyte.gz', 'dataset/test-labels-idx1-ubyte.gz',
          'dataset/train-images-idx3-ubyte.gz', 'dataset/train-labels-idx1-ubyte.gz',
          'utilities/spots_10_loader.py']

def download_files():
    # find out the path where this script is located
    script_path = os.path.dirname(os.path.realpath(__file__))
    # download the files with beautiful progress bars
    for file in files:
        filename = file.split('/')[-1]
        # Check if the file already exists
        if os.path.exists(script_path + '/' + filename):
            print('File', file, 'already exists, skipping download')
            continue
        # Download the file with curl
        subprocess.run(['curl', '-L', '-o', script_path + '/' + filename, repo_path + file], check=True)
        print('Downloaded', file)
    print('All files downloaded successfully')