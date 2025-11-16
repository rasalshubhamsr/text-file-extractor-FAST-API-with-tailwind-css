# Simple Text File Uploader

A lightweight web application that allows users to upload text files and view their contents through a clean, responsive interface. Built with FastAPI backend and vanilla JavaScript frontend.

## Features

- 📁 **File Upload**: Select and upload `.txt` files from your computer
- 👀 **Content Display**: View uploaded file contents in a formatted display area
- ✅ **File Validation**: Client-side and server-side validation for text files only
- 🎨 **Modern UI**: Clean, responsive design using Tailwind CSS
- 🔒 **Error Handling**: Comprehensive error messages for various scenarios
- 📡 **API Documentation**: Auto-generated Swagger UI documentation

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, JavaScript (ES6+), Tailwind CSS
- **Server**: Uvicorn ASGI server
- **API Documentation**: OpenAPI 3.1 / Swagger UI

## Project Structure

```
simple-text-file-uploader/
├── main.py           # FastAPI backend application
├── index.html        # Frontend HTML interface
├── sample.txt        # Sample test file
├── ui.png           # UI screenshot
└── README.md        # Project documentation
```

## Installation & Setup

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install required Python packages**:
   ```bash
   pip install fastapi uvicorn python-multipart
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```
   
   Or alternatively:
   ```bash
   uvicorn main:app --reload
   ```

4. **Open your browser** and navigate to:
   - **Main Application**: http://127.0.0.1:8000
   - **API Documentation**: http://127.0.0.1:8000/docs

## Usage

### Web Interface

1. Open the application in your browser at `http://127.0.0.1:8000`
2. Click "Choose File" and select a `.txt` file from your computer
3. Click "Upload and Display Content" button
4. View the file contents in the display area below

### API Endpoints

#### Upload File
- **Endpoint**: `POST /upload/`
- **Description**: Upload a text file and receive its contents
- **Parameters**: 
  - `file`: Text file (multipart/form-data)
- **Response**: JSON with filename and content
- **Example**:
  ```bash
  curl -X 'POST' \
    'http://127.0.0.1:8000/upload/' \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F 'file=@sample.txt;type=text/plain'
  ```

#### Get Homepage
- **Endpoint**: `GET /`
- **Description**: Serves the main HTML interface
- **Response**: HTML page

### Response Format

Successful upload returns:
```json
{
  "filename": "sample.txt",
  "content": "Hello FastAPI!\n\nThis is a sample text file..."
}
```

## Error Handling

The application handles various error scenarios:

- **Invalid File Type**: Returns 400 error for non-text files
- **File Reading Errors**: Returns 500 error for corrupted or unreadable files
- **Network Errors**: Frontend displays connection error messages
- **No File Selected**: Client-side validation prevents empty submissions

## Configuration

### CORS Settings

The application is configured with permissive CORS settings for development:
- Allows all origins (`*`)
- Allows all HTTP methods
- Allows all headers
- Supports credentials

**Note**: For production deployment, configure CORS with specific allowed origins.

### Server Configuration

Default server settings:
- **Host**: 127.0.0.1 (localhost)
- **Port**: 8000
- **Auto-reload**: Enabled in development

## Development

### File Structure Details

- **`main.py`**: Contains the FastAPI application with upload endpoint and HTML serving
- **`index.html`**: Single-page frontend with drag-and-drop styling and JavaScript handling
- **`sample.txt`**: Example text file for testing upload functionality

### Key Features Implementation

1. **File Validation**: Both client-side (`file.type` check) and server-side (`content_type` validation)
2. **Async Processing**: Uses FastAPI's async capabilities for file handling
3. **Error Boundaries**: Comprehensive try-catch blocks with proper HTTP status codes
4. **Responsive Design**: Mobile-friendly interface using Tailwind CSS utilities

## Testing

Use the included `sample.txt` file to test the upload functionality:

1. Start the server
2. Open the web interface
3. Upload `sample.txt`
4. Verify the content displays correctly

## API Documentation

FastAPI automatically generates interactive API documentation available at:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **OpenAPI Schema**: http://127.0.0.1:8000/openapi.json

## Browser Support

- Modern browsers with ES6+ support
- File API support required for file handling
- Fetch API support required for HTTP requests

## Security Considerations

- File type validation prevents execution of malicious files
- Content-type checking on both client and server sides
- UTF-8 encoding assumption for text file processing
- CORS configuration should be restricted in production environments

## License

This project is provided as-is for educational and development purposes.

---

**Note**: This is a development server. For production deployment, consider using a production ASGI server like Gunicorn with proper security configurations.