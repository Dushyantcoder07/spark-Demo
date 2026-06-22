FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y default-jdk wget && \
    apt-get clean

RUN pip install pyspark

WORKDIR /app

COPY . .

CMD ["python", "app.py"]