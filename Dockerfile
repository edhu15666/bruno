FROM python:3.8
COPY . /tmp/docker
WORKDIR /tmp/docker
RUN apt-get update -y
RUN apt-get install  pkg-config libcairo2-dev python3-gi libgirepository1.0-dev python3-cairo-dev libssl-dev -y
RUN pip install Flask
RUN pip install -r requirements.txt
EXPOSE 5000
CMD flask --app app run --host=0.0.0.0
