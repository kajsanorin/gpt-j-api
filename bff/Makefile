build:
	- docker build -t frontend .

run:
	- docker run --name frontend -dp 80:80 --restart always --net=host frontend

stop:
	- docker stop frontend
	- docker rm frontend