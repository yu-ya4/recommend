import os
import urllib.request
import zipfile


base_url = "http://files.grouplens.org/datasets/movielens/"
dir_path = "./datasets"
os.makedirs(dir_path, exist_ok=True)


def load_data(dataset_name: str = "ml-100k") -> None:
    dataset_path = dir_path + "/" + dataset_name
    if os.path.exists(dataset_path):
        print("dataset already exists.")
        return

    zip_file_name = dataset_name + ".zip"
    url = base_url + zip_file_name
    urllib.request.urlretrieve(url, dir_path + "/" + zip_file_name)

    with zipfile.ZipFile(dir_path + "/" + zip_file_name) as zip_file:
        zip_file.extractall(dir_path)
        unzip_dir_name = zip_file.namelist()[0].split("/")[0]
        if unzip_dir_name != dataset_name:
            os.rename(dir_path + "/" + unzip_dir_name, dataset_path)
    os.remove(dir_path + "/" + zip_file_name)


if __name__ == "__main__":
    load_data(dataset_name="ml-10m")
