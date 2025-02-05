FROM python:3.12-slim

WORKDIR /social_net

USER root


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install gunicorn


COPY requirements.txt .

RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
      pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["gunicorn", "app.wsgi"]
