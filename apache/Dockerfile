FROM otomato/alpine-netcat
LABEL MAINTAINER="Ant Weiss"
RUN apk add -U apache2 && mkdir /run/apache2
EXPOSE 80 443
CMD ["/usr/sbin/httpd", "-D" ,"FOREGROUND"]
