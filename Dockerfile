FROM node:current-alpine3.10
COPY static/src/scss src/
RUN npm install -g sass && sass src/index.scss main.css

FROM python:3.7.7-alpine3.11
WORKDIR /levensfilosofie
ADD . /levensfilosofie/
ENV PORT=8000
COPY --from=0 main.css static/dist/main.css
RUN apk update && apk add build-base && pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE $PORT
CMD ./entrypoint.sh $PORT
