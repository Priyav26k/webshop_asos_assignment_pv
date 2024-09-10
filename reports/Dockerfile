# Dockerfile
FROM python:3.9-slim

# Set working directory to /app
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY reports .

# Expose port 4444 for Selenium
EXPOSE 4444

# Run tests when container starts
CMD ["pytest"]