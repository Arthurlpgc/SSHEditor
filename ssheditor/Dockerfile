FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y openssl libssl-dev python-dev
RUN mkdir project
WORKDIR /project
COPY requirements.txt . 
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD python3 server.py