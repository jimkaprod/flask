# Basic flask container

FROM fanoftal2/flask-crud-base:1

ADD . /home/app/
WORKDIR /home/app/

ENV FLASK_APP=microblog.py

ENV MAIL_SERVER=smtp.googlemail.com
ENV MAIL_PORT=587
ENV MAIL_USE_TLS=1
ENV MAIL_USERNAME=
ENV MAIL_PASSWORD=

#ENV DATABASE_URL=db

EXPOSE 5000

ENTRYPOINT ["python3", "microblog.py"]
