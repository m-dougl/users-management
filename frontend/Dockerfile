FROM python:3.11-slim

WORKDIR /frontend

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

ENV PYTHONPATH=/frontend

EXPOSE 8501

CMD ["streamlit","run","frontend_app.py"]

