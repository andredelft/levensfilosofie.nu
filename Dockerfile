FROM node:current-alpine3.10
COPY package*.json *.config.js ./
COPY static static/
RUN npm install -g npm@latest && npm install && npm run build

FROM python:3.7.7-alpine3.11
WORKDIR /levensfilosofie
ADD . /levensfilosofie/
ENV PORT=8000
COPY --from=0 static/build static/build/
RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE $PORT
CMD ./entrypoint.sh $PORT
