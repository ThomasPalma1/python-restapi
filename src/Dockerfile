FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pwd
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]