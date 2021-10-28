source .env
deploy/build.sh
docker stop ${DOCKER_CONTAINER_NAME}
docker rm ${DOCKER_CONTAINER_NAME}
deploy/run.sh
