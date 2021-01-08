<<<<<<< HEAD
FROM python:3.6

EXPOSE 5000


WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["python","/deployment/app.py"]
=======
# start from base

FROM ubuntu:18.04
LABEL maintainer="Your Name <youremailaddress@provider.com>"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python", "./app.py" ]
>>>>>>> 72b363b521e4db65a4b34b9a6ca8cf4ac85ffce0
