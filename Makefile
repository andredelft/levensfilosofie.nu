HOST_PORT=80
IMAGE_TAG=levensfilosofie
ENV_FILE=.env
CONTAINER_NAME=levensfilosofie

build:
	docker build -t $(IMAGE_TAG) .

run:
	touch $(ENV_FILE)
	docker run --name $(CONTAINER_NAME) --env DEBUG=0 --env-file $(ENV_FILE) -p $(HOST_PORT):8000 --detach $(IMAGE_TAG)
