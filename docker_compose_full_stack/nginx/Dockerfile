FROM nginx:1.15.5

RUN rm /etc/nginx/conf.d/default.conf

# Copy over your nginx settings to reverse proxy to your app
COPY conf.d/dockering.conf /etc/nginx/conf.d/
