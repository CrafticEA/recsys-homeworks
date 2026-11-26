from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

BASE_URL = "https://files.grouplens.org/datasets/movielens"
HERE = Path(__file__).resolve().parent
DATASETS = {
    "ml-1m": ("movies.dat", "ratings.dat", "README"),
    "ml-latest-small": ("movies.csv", "ratings.csv", "README.txt"),
}

for name, files in DATASETS.items():
    folder = HERE / name
    if all((folder / file).is_file() for file in files):
        continue
    print(f"Downloading {name}…")
    with urlopen(f"{BASE_URL}/{name}.zip", timeout=60) as response:
        with ZipFile(BytesIO(response.read())) as archive:
            folder.mkdir(exist_ok=True)
            for file in files:
                (folder / file).write_bytes(archive.read(f"{name}/{file}"))

