FROM python:3.9-alpine
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt
ADD . /
ENV PORT=8000
EXPOSE $PORT
CMD ./entrypoint.sh $PORT
