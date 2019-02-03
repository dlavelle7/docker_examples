FROM alpine:3.6

RUN apk update && apk add python3 python3-dev build-base gettext curl

RUN mkdir -p /web/search_engine
WORKDIR /web/search_engine

# Install python app dependencies first, so dependencies aren't reinstalled
# on every source code change
COPY search_engine/requirements.txt /web/search_engine/

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Clean up packages that are only required for install to reduce image size
#RUN apk del -r python3-dev

# Copy app source code near end so only one layer to be build on code change
COPY . /web
