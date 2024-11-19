FROM python:3.10.15

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
EXPOSE 8501

CMD ["streamlit","run","app.py","--server.port=8501","server.address=0.0.0.0"]