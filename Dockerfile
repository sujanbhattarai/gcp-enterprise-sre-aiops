FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN groupadd --gid 10001 sre \
    && useradd --uid 10001 --gid 10001 --create-home sre

COPY automation/python/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=10001:10001 automation/python/ .

RUN chown 10001:10001 /app

USER 10001:10001

CMD ["python", "sre_monitor.py"]
