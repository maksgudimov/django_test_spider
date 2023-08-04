FROM python:3.11

WORKDIR /app

RUN apt update \
 && apt -y upgrade \
 && pip install --upgrade pip \
 && apt install -y --no-install-recommends build-essential git \
 && pip install starlette \
 && pip install django \
 && pip install djangorestframework \
 && pip install fuzzywuzzy \
 && pip install drf-yasg \
 && pip install psycopg2 \
 && apt autoremove -y \
 && apt clean all \
 && rm -rf /etc/apk/cache \
 && rm -rf /var/lib/apt/lists/*
EXPOSE 8000
COPY . .

CMD ["python3", "manage.py","runserver","0.0.0.0:8000"]