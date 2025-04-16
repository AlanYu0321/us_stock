FROM python:3.9-slim

# 設置工作目錄
WORKDIR /app

# 複製依賴文件
COPY requirements.txt .

# 安裝依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式代碼
COPY . .

# 啟動 FastAPI 服務
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
