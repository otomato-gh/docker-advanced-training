# Final exercise

For this exercise please complete the following:
1. Create a Dockerfile that will create an image:
    - based on python:alpine
    - create user 'appuser' ( adduser -D appuser )
    - define the container user to be 'appuser'
    - copy the following files to /home/appuser
        - all \*.py files
        - directory /templates
        - requirements.txt
    - set working directory to be /home/appuser
    - install dependency modules  with 'pip install -r requirements.txt'
    - define that the app listens on port 5000
    - set the image default command to be "python app.py"
2. Create a docker-compose file with the following services:
    - app:
        - this is the python web application itself
        - image built from Dockerfile each time a composition is executed (if needed)
        - binds to port 8080 of the host machine
        - networks: front, back
    - mongo:
        - from official mongo image
        - listens on default port 27017
        - networks: back
    - netdata:
        - from official netdata image
        - has all necessary mounts
