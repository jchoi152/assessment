import logging

from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

# Simple logger setup
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("app")

app = FastAPI()


# Log every incoming request (method + path)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"{request.method} {request.url.path}")
    response = await call_next(request)
    return response


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": "1.0.0"}


@app.get("/", response_class=PlainTextResponse)
def root():
    return "Welcome the service is running"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
