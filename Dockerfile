# Build with:
# $ docker build -t server_track .

# Run with:
# $ docker run -d -P --name=server_track server_track

FROM ubuntu

MAINTAINER Matt Skone matt.skone@gmail.com

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["server.py"]

