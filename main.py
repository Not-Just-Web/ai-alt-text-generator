from fastapi import FastAPI, Depends, Request
from api.router import router as api_router

app = FastAPI(docs_url="/api-docs", redoc_url="/api-redoc", title="Dragon Dream API", swagger_favicon_url="/favicon.ico")

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)  # Replace 8080 with your preferred port