FROM python:3.10.4-alpine
WORKDIR ./app
COPY . .
ARG DEPS="gcc libc-dev linux-headers postgresql-dev git"
ARG PYTHONUNBUFFERED=1
ARG PYTHONDONTWRITEBYTECODE=1
RUN apk update &&\
 apk add --update --no-cache --virtual .build-deps ${DEPS} &&\
 apk add libffi-dev &&\
 pip install -r  requirements.txt &&\
 apk del .build-deps &&\
 apk del libffi-dev
ENTRYPOINT ["python3","main.py"]
