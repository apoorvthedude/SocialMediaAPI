FROM python:3.10.6-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN  pip3 install -r requirements.txt

COPY . .

CMD ["python3","manage.py","runserver","127.0.0.1:8000","0.0.0.0:8000"]