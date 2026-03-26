# Section 1 Part B Bonus: Multi-stage build to keep image small
FROM python:3.12-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy app code
COPY main.py .

# Section 1 Part B Bonus: Non-root user for security
RUN useradd -m -u 1000 appuser
USER appuser

EXPOSE 8080

CMD ["python", "main.py"]
