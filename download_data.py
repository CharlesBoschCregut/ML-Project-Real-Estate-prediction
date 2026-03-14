import os
import gzip
import shutil
import requests
from datetime import datetime

BASE_URL = "https://files.data.gouv.fr/geo-dvf/latest/csv/{year}/departements/77.csv.gz"

RAW_DIR = "./dataset_raw"
TMP_DIR = "./tmp_downloads"

# Wipe folders
shutil.rmtree(RAW_DIR, ignore_errors=True)
shutil.rmtree(TMP_DIR, ignore_errors=True)

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(TMP_DIR, exist_ok=True)

current_year = datetime.now().year
downloaded = 0
year = current_year

while downloaded < 5:
    url = BASE_URL.format(year=year)
    gz_path = os.path.join(TMP_DIR, f"77_{year}.csv.gz")
    csv_path = os.path.join(RAW_DIR, f"77_{year}.csv")

    print(f"\nTrying {year} → {url}")

    r = requests.get(url, stream=True)

    if r.status_code == 404:
        print(f"{year} not available, skipping")
        year -= 1
        continue

    r.raise_for_status()

    print("Downloading...")
    with open(gz_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

    print("Extracting CSV...")
    with gzip.open(gz_path, "rb") as f_in:
        with open(csv_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

    downloaded += 1
    year -= 1

print(f"\nDone. Downloaded {downloaded} datasets.")