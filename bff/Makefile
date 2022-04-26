build:
	- docker build -t bff .

run:
	- docker run --name bff -dp 80:80 --restart always --net=host bff

stop:
	- docker stop bff
	- docker rm bff
