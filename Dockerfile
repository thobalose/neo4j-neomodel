FROM python:2.7-slim
LABEL maintainer="thoba@sanbi.ac.za"

RUN apt-get update -y --fix-missing \
    && pip install -U pip \
    && mkdir /code
WORKDIR /code

ADD requirements.txt .
RUN pip install -Ur requirements.txt

ADD . .

EXPOSE 5000

ENTRYPOINT ["./docker-entrypoint.sh"]