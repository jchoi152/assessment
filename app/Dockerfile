
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
# in builder stage, install dependencies to /install directory to keep the final image clean
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.11-slim

WORKDIR /app
# copy only the installed dependencies from the builder stage to the final image
COPY --from=builder /install /usr/local

COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 8080

# Run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

