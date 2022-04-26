build:
	@ sudo docker build -t gpt-j .

build-gpu:
	@ sudo docker build -f gpu.Dockerfile -t gpt-j . 

run:
	@ sudo docker run -detach --restart always --name gpt-j \
	  -e API_KEY=${API_KEY} \
	  -v /home/kajsa.norin/models/hf_weights:/data \
	  -dp 8001:8001 gpt-j

run-gpu:
	@ sudo docker run -detach --restart always --gpus all --name gpt-j \
	  -e API_KEY=${API_KEY} \
	  -v /home/kajsa.norin/models/hf_weights:/data \
	  -dp 8001:8001 gpt-j

stop:
	- sudo docker stop gpt-j
	- sudo docker rm gpt-j