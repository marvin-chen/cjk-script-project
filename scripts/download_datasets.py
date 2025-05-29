import os
import requests
import zipfile
import tarfile
import shutil
from tqdm import tqdm

# Define data directory
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def download_file(url, dest_path):
    """Download a file with a progress bar."""
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    with open(dest_path, "wb") as f:
        for chunk in tqdm(response.iter_content(chunk_size=8192), total=total_size//8192, unit="KB"):
            if chunk:
                f.write(chunk)

# Kuzushiji-MNIST (Japanese)
def download_kuzushiji_mnist():
    urls = [
        "http://codh.rois.ac.jp/kmnist/dataset/kmnist/kmnist-train-imgs.npz",
        "http://codh.rois.ac.jp/kmnist/dataset/kmnist/kmnist-train-labels.npz",
        "http://codh.rois.ac.jp/kmnist/dataset/kmnist/kmnist-test-imgs.npz",
        "http://codh.rois.ac.jp/kmnist/dataset/kmnist/kmnist-test-labels.npz"
    ]
    kuzushiji_dir = os.path.join(DATA_DIR, "kuzushiji_mnist")
    os.makedirs(kuzushiji_dir, exist_ok=True)
    for url in urls:
        filename = os.path.join(kuzushiji_dir, url.split("/")[-1])
        print(f"Downloading {filename}...")
        download_file(url, filename)

# Unihan Database (for Phase 2)
def download_unihan():
    url = "ftp://ftp.unicode.org/Public/UNIDATA/Unihan.zip"
    dest_path = os.path.join(DATA_DIR, "Unihan.zip")
    print(f"Downloading {dest_path}...")
    download_file(url, dest_path)
    with zipfile.ZipFile(dest_path, "r") as zip_ref:
        zip_ref.extractall(os.path.join(DATA_DIR, "unihan"))

# KanjiVG (for Phase 2)
def download_kanjivg():
    url = "https://kanjivg.tagaini.net/release/kanjivg-latest.zip"
    dest_path = os.path.join(DATA_DIR, "kanjivg.zip")
    print(f"Downloading {dest_path}...")
    download_file(url, dest_path)
    with zipfile.ZipFile(dest_path, "r") as zip_ref:
        zip_ref.extractall(os.path.join(DATA_DIR, "kanjivg"))

# CASIA-HWDB (Manual Step)
# def download_casia_hwdb():
#     casia_dir = os.path.join(DATA_DIR, "casia_hwdb")
#     os.makedirs(casia_dir, exist_ok=True)
#     print("CASIA-HWDB requires manual download due to registration.")
#     print("1. Visit http://www.nlpr.ia.ac.cn/databases/handwriting/Download.html")
#     print("2. Register and download HWDB1.1 dataset (train and test)")
#     print("3. Extract files to", casia_dir)

# AI Hub Hangul (Manual Step)
# def download_ai_hub_hangul():
#     hangul_dir = os.path.join(DATA_DIR, "ai_hub_hangul")
#     os.makedirs(hangul_dir, exist_ok=True)
#     print("AI Hub Hangul Dataset requires registration.")
#     print("1. Visit https://aihub.or.kr/")
#     print("2. Register and download the Handwritten Hangul Dataset")
#     print("3. Extract files to", hangul_dir)

if __name__ == "__main__":
    print("Downloading datasets...")
    download_kuzushiji_mnist()
    download_unihan()
    download_kanjivg()
    download_casia_hwdb()
    download_ai_hub_hangul()