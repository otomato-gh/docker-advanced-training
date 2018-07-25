# Final exercise

For this exercise please complete the following:
1. Create a Dockerfile that will create an image:
    - based on python:alpine
    - create user 'appuser' ( adduser -D appuser )
    - copy 'requirements.txt' to '/home/appuser/' 
    - set working directory to be /home/appuser
    - install dependency modules  with 'pip install -r requirements.txt'
    - define the container user to be 'appuser'
    - copy the following files to /home/appuser
        - all \*.py files
        - directory /templates
    - define that the app listens on port 5000
    - set the image default command to be "python app.py"
2. Build the image and push it to DockerHub as your_use_name/changes:latest
3. Create a docker-compose file with the following services:
    - app:
        - this is the python web application itself
        - image built from Dockerfile each time a composition is executed (if needed)
        - binds to port 8080 of the host machine
        - networks: front, back
        - logging: maximum 3 log files, maximum 100k size
    - mongo:
        - from official mongo image
        - listens on default port 27017
        - networks: back
    - netdata:
        - from official netdata image
        - has all necessary mounts
        - networks: front
        - binds to port 19999 of the host
 4. Run the composition
    - Verify the application works
    - Verify netdata shows performance data
    - Verify log rotation for the app
