# python image in docker hub and version;
FROM python:3.10
# port on which the flask app will run;
EXPOSE 5000
# set the working directory of a Docker container;
# and then it's gonna move into the app folder;
WORKDIR /app
# installing flask microframework
RUN pip3 install Flask
# copying files or directories to the container's file system
# in my case, I'm copying the entire directory inside the current directory in the container (/app)
COPY . .
# finally, we're gonna tell it what command should run when this image starts up as a container
CMD ["flask", "run", "--host", "0.0.0.0"]