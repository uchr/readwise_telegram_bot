FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt 

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py app.py
COPY readwise.py readwise.py

CMD ["python", "./app.py"]