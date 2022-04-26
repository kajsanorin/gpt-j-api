FROM tensorflow/tensorflow:latest-gpu
CMD nvidia-smi

#set up environment
RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl
RUN apt-get -y install python3.7
RUN apt-get -y install python3-pip
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade pip

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV TF_FORCE_GPU_ALLOW_GROWTH true

COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip3 install -r requirements.txt

EXPOSE 8001

COPY . /app
WORKDIR /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]