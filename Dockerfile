FROM python:3.10.4-slim
COPY . /app
WORKDIR /app
RUN apt update;apt install git
RUN pip install -r requirements.txt
CMD ["python3","main.py"]
