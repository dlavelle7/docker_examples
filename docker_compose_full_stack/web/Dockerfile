FROM alpine:3.6

RUN apk update && apk add python3 python3-dev postgresql-client \
    postgresql-dev build-base gettext

RUN mkdir -p /web/dockering
WORKDIR /web/dockering

# Install python app dependencies first, so dependencies aren't reinstalled
# on every source code change
COPY dockering/requirements.txt dockering/requirements_deploy.txt /web/dockering/

RUN pip3 install --upgrade pip && pip3 install -r requirements_deploy.txt

# Copy app source code near end so only one layer to be build on code change
COPY . /web
