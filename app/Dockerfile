FROM python:3.9-slim
WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip --no-cache-dir --progress-bar off
RUN pip install -r requirements.txt --no-cache-dir --progress-bar off

COPY app /app
CMD ["python", "app.py"]

