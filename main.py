import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import io

app = FastAPI(title="Simple Text File Uploader")

# Set up CORS (Cross-Origin Resource Sharing)
# This allows the HTML file to communicate with the FastAPI backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.post("/upload/")
async def upload_text_file(file: UploadFile = File(...)):
    """
    This endpoint accepts a file upload.
    It checks if the file is a text file and returns its content.
    """
    # Check if the file is a text file
    if file.content_type != "text/plain":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a .txt file.")

    try:
        # Read the file content as bytes
        contents_bytes = await file.read()
        
        # Decode the bytes into a string (assuming UTF-8 encoding)
        contents_str = contents_bytes.decode("utf-8")
        
        return {
            "filename": file.filename,
            "content": contents_str
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"There was an error reading the file: {e}")
    finally:
        # Ensure the file is closed
        await file.close()

@app.get("/", response_class=HTMLResponse)
async def get_index():
    """
    Serves the main HTML page.
    """
    with open("index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    # To run this file, save it as main.py and run:
    # uvicorn main:app --reload
    print("Starting FastAPI server...")
    print("Go to http://127.0.0.1:8000 in your browser.")
    uvicorn.run(app, host="127.0.0.1", port=8000)