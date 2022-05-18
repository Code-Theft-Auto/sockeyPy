FROM python:3.10.4-alpine
COPY . /app
WORKDIR /app
RUN apk update;apk add git gcc
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
RUN pip install -r requirements.txt
CMD ["python3","main.py"]
