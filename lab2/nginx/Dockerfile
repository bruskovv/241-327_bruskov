FROM nginx:stable

RUN mkdir -p /etc/nginx/certs

COPY certs/lab2.crt /etc/nginx/certs/lab2.crt
COPY certs/lab2.key /etc/nginx/certs/lab2.key
COPY templates/default.conf.template /etc/nginx/templates/default.conf.template
