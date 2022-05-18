FROM python:3.10.4-alpine
COPY . /app
WORKDIR /app
RUN apk update;apk add git gcc libffi-dev
RUN pip install -r requirements.txt
CMD ["python3","main.py"]
