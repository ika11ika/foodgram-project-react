FROM python:3.7-slim

WORKDIR ../../data/

COPY ./ ../backend/foodgram/

WORKDIR ../backend/foodgram/

WORKDIR /app

COPY ./ ./

RUN pip3 install -r requirements.txt --no-cache-dir

RUN python manage.py migrate

RUN python manage.py filling_ingridients_db

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"] 
