FROM python:3.6-alpine
COPY . /app
WORKDIR /app
RUN apk update && apk add postgresql-dev postgresql-client gcc python3-dev musl-dev git
RUN pip install -r requirements.txt
CMD ["/bin/sh"]
