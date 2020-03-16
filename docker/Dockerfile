FROM python:3.7-slim

COPY ./skimmer ../skimmer
COPY ./models ../models
WORKDIR /skimmer

RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev
RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["./run_directory.sh"]