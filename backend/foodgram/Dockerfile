FROM python:3.7-slim

RUN mkdir /data

WORKDIR ../../data/

COPY ./ ../backend/foodgram/data/

WORKDIR ../backend/foodgram/

RUN mkdir /app

COPY ../ ./

RUN pip3 install -r requirements.txt --no-cache-dir

RUN python manage.py migrate

RUN python manage.py filling_ingridients_db

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"] 
