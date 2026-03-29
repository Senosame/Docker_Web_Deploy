FROM python:3.11-slim

WORKDIR /app

# Cài đặt thư viện
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn
COPY . .

# Flask chạy cổng 5000
EXPOSE 5000

CMD ["python", "app.py"]