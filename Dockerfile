FROM python:3.10.5-slim-buster

WORKDIR /app

COPY docker/src/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY docker/src/ /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
