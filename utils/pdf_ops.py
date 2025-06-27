from PyPDF2 import PdfReader

def extract_pdf_title(pdf_path):
    try:
        reader = PdfReader(str(pdf_path))
        if reader.metadata and reader.metadata.title:
            return reader.metadata.title.strip().replace(" ", "_")
    except Exception:
        pass
    # Si no hay título en metadatos, usar el nombre base
    return pdf_path.stem
