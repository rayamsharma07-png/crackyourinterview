from fastapi import FastAPI, UploadFile, File
from parse_resume import parse_resume, extract_text_from_pdf, extract_text_from_docx
import tempfile

app = FastAPI()

@app.post("/parse")
async def parse(file: UploadFile = File(...)):
    suffix = ".pdf" if file.filename.endswith(".pdf") else ".docx"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    if suffix == ".pdf":
        text = extract_text_from_pdf(tmp_path)
    else:
        text = extract_text_from_docx(tmp_path)

    return parse_resume(text)
