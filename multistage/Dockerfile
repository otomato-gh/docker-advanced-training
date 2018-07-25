FROM ubuntu as compile
RUN echo compiling > /tmp/compile.txt

FROM alpine as run
COPY --from=compile /tmp/compile.txt /opt/compiled/
CMD ["ls", "/opt/compiled"]
