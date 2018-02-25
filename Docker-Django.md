# Running Django inside a Docker Container

Notes from: [Django Project Tutorial](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)
      and: [Docker Django ](https://docs.docker.com/compose/django/#define-the-project-components)

Key file for Docker:
1. **Dockerfile** - Defines the apps environment i.e. what version of python and more.  Now the environment can be reproduced anywhere i.e. on the staging server or the production server.  Each line is a build command that is used to configure the image.
2. **docker-compose.yml** - defines the services that make up the app so they run together in an isolated environment.

To run django-admin.py commands in the container use the following command:
>sudo docker-compose run web django-admin.py startapp *name* .

**web** is the target service for the run command and because it has not been built, docker first creates it by running the build command that is in the docker-compose.yml file.

{ToDo} NOTE: I think you have to stop the services before you run this? i.e. docker-compose down

Once you have those:
>docker-compose up

Starts and runs the entire app.

The site name is the name of the Python package for the project.

ED 25519