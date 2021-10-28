build:
	docker build -t $(DOCKER_IMAGE_TAG) .

run:
	touch $(ENV_FILE)
	docker run --name $(DOCKER_CONTAINER_NAME) --env DEBUG=0 --env-file $(ENV_FILE) -p $(HOST_PORT):8000 --detach $(DOCKER_IMAGE_TAG) -v levensfilosofie_db:/db

update:
	make build
	docker stop $(DOCKER_CONTAINER_NAME)
	docker rm $(DOCKER_CONTAINER_NAME)
	make run
