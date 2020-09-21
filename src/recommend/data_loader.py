import os
import urllib.request
import zipfile


base_url = "http://files.grouplens.org/datasets/movielens/"
dir_path = "./datasets"
os.makedirs(dir_path, exist_ok=True)


if __name__ == "__main__":
    dataset_name = "ml-100k"
    dataset_path = dir_path + "/" + dataset_name
    if os.path.exists(dataset_path):
        print("dataset already exists.")
        exit()

    zip_file_name = dataset_name + ".zip"
    url = base_url + zip_file_name
    urllib.request.urlretrieve(url, dir_path + "/" + zip_file_name)

    with zipfile.ZipFile(dir_path + "/" + zip_file_name) as zip_file:
        zip_file.extractall(dir_path)
    os.remove(dir_path + "/" + zip_file_name)
