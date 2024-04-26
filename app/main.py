from fastapi import FastAPI, HTTPException
import tabula
import requests
from io import BytesIO

app = FastAPI()


@app.get("/")
async def read_root():
    pdf_url = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"

    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error downloading PDF: {e}")

    try:
        dfs = tabula.read_pdf(BytesIO(response.content), pages="all", stream=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading PDF: {e}")

    if dfs:
        return dfs[0].to_json(orient="records")
    else:
        raise HTTPException(status_code=404, detail="No data found in PDF")
