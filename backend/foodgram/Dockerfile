FROM python:3.7-slim

RUN mkdir app

RUN mkdir app/data

COPY ../../data/ ./app/data/

WORKDIR /app

COPY ./ ./

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"] 
