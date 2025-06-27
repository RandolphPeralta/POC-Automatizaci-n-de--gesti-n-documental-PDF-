import zipfile
from pathlib import Path

def zip_folder(folder_path, zip_name):
    folder_path = Path(folder_path)
    zip_path = folder_path.parent / zip_name
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in folder_path.rglob("*"):
            if file.is_file():
                zipf.write(file, file.relative_to(folder_path))
