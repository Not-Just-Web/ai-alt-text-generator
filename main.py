from fastapi import FastAPI, Depends, Request
from api.router import router as api_router

from fastapi.responses import HTMLResponse

app = FastAPI(docs_url="/api-docs", redoc_url="/api-redoc", title="Dragon Dream API", swagger_favicon_url="/favicon.ico")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def home():
    html_content = """
    <html>
        <head>
            <title>Dragon Dream API</title>
        </head>
        <body>
            <h1>Welcome to API server!</h1>
            <p>API documentation is available at:</p>
            <ul>
                <li><a href="/api-docs">Swagger UI</a></li>
                <li><a href="/api-redoc">ReDoc</a></li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)  # Replace 8080 with your preferred port