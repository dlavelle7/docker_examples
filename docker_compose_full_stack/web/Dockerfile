FROM alpine

# Initialize
RUN mkdir -p /web
COPY . /web/
WORKDIR /web/dockering

# Setup
RUN apk update
RUN apk upgrade
RUN apk add --update python3 python3-dev postgresql-client postgresql-dev build-base gettext
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements_deploy.txt

# Clean
RUN apk del -r python3-dev
