import shutil
from pathlib import Path

def rename_and_move_pdf(original_path, new_name, output_dir):
    new_name_clean = new_name.replace(" ", "_").replace("/", "_")
    new_path = Path(output_dir) / f"{new_name_clean}.pdf"
    shutil.copy2(original_path, new_path)
