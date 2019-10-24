FROM python:3.6-alpine

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt \
    && rm -rf /root/.cache && rm -rf /tmp/src && mkdir -p /app

COPY dev_reporter /app/dev_reporter

WORKDIR /app
CMD python -m dev_reporter
