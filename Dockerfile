FROM python:3.11.6-bookworm as builder

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --progress-bar off .

USER 1001:1001

ENTRYPOINT [ "python", "/app/backend/app.py" ]