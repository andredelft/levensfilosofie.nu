FROM node:current-alpine
COPY package*.json *.config.js ./
COPY static static/
RUN npm install && npm run build

FROM python:3.7.7-alpine3.11
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt
COPY --from=0 static/build static/build/
ADD . /
ENV PORT=8000
EXPOSE $PORT
CMD ./entrypoint.sh $PORT
