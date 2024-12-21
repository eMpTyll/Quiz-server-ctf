FROM python:3.9-slim
WORKDIR /app
COPY . .
# Sửa quyền truy cập cho các file
RUN chmod +x server.py
# Chạy server
CMD ["python", "server.py"]