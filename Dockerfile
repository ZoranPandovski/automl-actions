FROM pytorch/pytorch:latest

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install mindsdb_native;

COPY mdb.py /mdb.py

CMD ["python", "/mdb.py", "--dataset", "$dataset"]