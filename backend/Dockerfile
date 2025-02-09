FROM python:3.11-slim

WORKDIR /backend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

ENV PYTHONPATH=/backend

EXPOSE 8000

CMD ["python", "app.py"]

