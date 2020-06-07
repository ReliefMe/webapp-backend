FROM ubuntu

RUN apt-get update -y
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip
RUN apt-get update && \
      apt-get -y --no-install-recommends install sudo && \
      sudo apt-get -y --no-install-recommends install libsndfile1-dev 


COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app

RUN python3 -m pip install -r requirements.txt 

COPY . /opt/app

ENTRYPOINT ["python3"]

CMD [ "/opt/app/application.py" ]


