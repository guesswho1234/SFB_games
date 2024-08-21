FROM python:3.11-alpine

WORKDIR /app 
COPY requirements.txt /app

RUN apk add build-base libpq-dev
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 

EXPOSE 3838

ENTRYPOINT ["otree"] 
CMD ["prodserver", "8000"]