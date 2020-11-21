FROM python:3.7.7-alpine3.11

WORKDIR /levensfilosofie
ADD . /levensfilosofie/

ENV PORT=8000

RUN apk update && apk add build-base

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE $PORT
CMD ./entrypoint.sh $PORT
