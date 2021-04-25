FROM python:3.8.0-buster

RUN apt-get update && \
    apt-get install -y vim nano

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt


COPY . /consumer_project/
WORKDIR /consumer_project

# Run the application
CMD ["python", "consumer.py"]

