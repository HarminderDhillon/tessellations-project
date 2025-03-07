FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy everything at once to fix the editable install issue
COPY . .

# Install requirements and the package in editable mode
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -e .

# Create a non-root user and switch to it
RUN useradd -m appuser
RUN mkdir -p /app/output && chown -R appuser:appuser /app/output
USER appuser

# Set Python path
ENV PYTHONPATH=/app

CMD ["tessellate"]