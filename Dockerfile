FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY automation/python/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY automation/python/ .

CMD ["python", "sre_monitor.py"]
