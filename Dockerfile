# Basic flask container

FROM fanoftal2/flask-crud-base:1

ADD . /home/app/
WORKDIR /home/app/

ENV FLASK_APP=microblog.py
#ENV DATABASE_URL=db

EXPOSE 5000

ENTRYPOINT ["python3", "microblog.py"]
