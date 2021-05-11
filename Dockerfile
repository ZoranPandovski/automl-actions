FROM pytorch/pytorch:latest

RUN apt-get update && \
    apt-get upgrade -y && \
    pip install mindsdb_native;

COPY mdb.py /mdb.py
ENTRYPOINT["python"]

CMD ["/mdb.py", "--dataset", "$dataset"]