# Download the files from the SPOTS-10 repository
# download_files()

from .downloader import download_files

def SPOTS10():
    download_files()
    from .spots_10_loader import SPOT10Loader
    X_train, y_train = SPOT10Loader.get_data(dataset_dir="./dataset", kind='train')
    X_test, y_test = SPOT10Loader.get_data(dataset_dir="./dataset", kind='test')
    return X_train, y_train, X_test, y_test