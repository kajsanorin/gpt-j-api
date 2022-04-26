FROM python:3.8

COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip install -r requirements.txt

EXPOSE 80

COPY . /app
WORKDIR /app

# CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "80"]

# ENTRYPOINT python app/main.py

ENTRYPOINT ["python", "-u"]
CMD ["app/main.py"]