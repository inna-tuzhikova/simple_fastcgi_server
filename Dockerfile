FROM python:3.7-slim
WORKDIR /app

COPY server.py requirements.txt /app/
RUN pip install -r /app/requirements.txt
CMD ["python", "/app/server.py"]
