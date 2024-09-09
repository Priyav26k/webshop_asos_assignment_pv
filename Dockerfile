FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q", "--html=reports/report.html"]
