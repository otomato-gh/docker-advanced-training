FROM python:alpine
RUN adduser -D appuser
WORKDIR /home/appuser
COPY . /home/appuser
RUN pip install -r requirements.txt
USER appuser
COPY . /home/appuser
EXPOSE 5000
CMD ["python", "app.py"]
