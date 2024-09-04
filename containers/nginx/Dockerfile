FROM nginx:stable-alpine

RUN rm -f /etc/nginx/conf.d/*
COPY ./containers/nginx/nginx.conf /etc/nginx/conf.d/

CMD /usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf