FROM python3.10.4
COPY . /app
WORKDIR /app
RUN apk update;apk add git
RUN pip install -r requirements.txt
CMD ["python3","main.py"]