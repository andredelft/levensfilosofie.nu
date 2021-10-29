source .env
docker run --name ${DOCKER_CONTAINER_NAME} --env DEBUG=0 --env-file ${ENV_FILE} -p ${HOST_PORT}:8000 --detach -v ${DOCKER_DB_VOLUME}:/db ${DOCKER_IMAGE_TAG}
