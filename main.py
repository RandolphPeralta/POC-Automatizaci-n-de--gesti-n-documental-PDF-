from utils.pdf_ops import extract_pdf_title
from utils.file_ops import rename_and_move_pdf
from utils.zipper import zip_folder
from config import INPUT_DIR, OUTPUT_DIR, ZIP_NAME
from pathlib import Path

def main():
    input_path = Path(INPUT_DIR)
    output_path = Path(OUTPUT_DIR)
    output_path.mkdir(parents=True, exist_ok=True)

    for pdf_file in input_path.glob("*.pdf"):
        title = extract_pdf_title(pdf_file)
        rename_and_move_pdf(pdf_file, title, output_path)

    zip_folder(output_path, ZIP_NAME)
    print(f"✅ Proceso completado. ZIP generado: {ZIP_NAME}")

if __name__ == "__main__":
    main()
