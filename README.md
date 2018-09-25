# Perseus

Dockerized Bottle app for testing container orchestration

## Docker

### Steps
* [Validate and Install Prerequisites](#validate-and-install-prerequisites)
* [Sanity Check](#sanity-check)
* [Compile and Install Container Images](#compile-and-install-container-images)
* [Run](#run)
* [Healthcheck](#health-check)
* [Development with Docker](#development-with-docker)
* [Stopping the Service](#stopping-the-service)
* [Makefile Target Summary](#makefile-target-summary)
* [Docker Cheat Sheet](#docker-cheat-sheet)
* [Running tests with Docker](#running-the-tests-with-docker)


### Validate and Install Prerequisites
Make sure the following is installed in your system.

* perseus
* Docker Engine
* Make


For more detail, see below.

#### Perseus:
Clone this git repo in a separate directory.
Repo [link](https://github.com/oliver-nowak/perseus):

```$ git clone https://github.com/oliver-nowak/perseus.git```

#### Docker Engine
Go [here for OSX](https://docs.docker.com/docker-for-mac/install/) or [here for WIN](https://docs.docker.com/docker-for-windows/install/) to download and install *Docker* for your Operating System.

Once installed, verify that *docker-compose* is present on your system via the terminal:
```
$ docker-compose version

docker-compose version 1.22.0, build f46880f
docker-py version: 3.4.1
CPython version: 3.6.4
OpenSSL version: OpenSSL 1.0.2o  27 Mar 2018
```

Docker comes bundled with it.
If you do not have *docker-compose*, follow instructions found [here](https://docs.docker.com/compose/install/), and verify as above.


Verify the Docker Engine is installed:
```
$ docker version

Client:
 Version:           18.06.1-ce
 API version:       1.38
 Go version:        go1.10.3
 Git commit:        e68fc7a
 Built:             Tue Aug 21 17:21:31 2018
 OS/Arch:           darwin/amd64
 Experimental:      false

Server:
 Engine:
  Version:          18.06.1-ce
  API version:      1.38 (minimum version 1.12)
  Go version:       go1.10.3
  Git commit:       e68fc7a
  Built:            Tue Aug 21 17:29:02 2018
  OS/Arch:          linux/amd64
  Experimental:     false
```

When you have a clean system, executing the following command should look like this:
```
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
```

#### Make
Check if you have *Make* installed:
```
$ make -v

GNU Make 3.81
Copyright (C) 2006  Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

This program built for i386-apple-darwin11.3.0
```

If you do not have *Make* installed, you have a few options:

* Install Make via XCode developer tools
    * Download XCode via the AppStore
    * Open XCode, click the 'XCode' menu item, 'Open Developer Tool' -> 'More Developer Tools...' which will open a browser window redirecting you to **https://developer.apple.com/download/more/?=for%20Xcode**.
    * Download and install the *Command Line Tools* for your version of XCode/OSX.
* Install Make via homebrew
    * If you have homebrew installed already:
        * ```$ brew install make```
    * If don't have homebrew installed:
        * Install *homebrew* via these [instructions](https://brew.sh/)
        * Then, install Make via ```$ brew install make```

### Sanity Check
Run `docker run hello-world`. You should see something like this:
```
wintermute::perseus$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
9db2ca6ccae0: Pull complete
Digest: sha256:4b8ff392a12ed9ea17784bd3c9a8b1fa3299cac44aca35a85c90c5e3c7afacdc
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

## Compile and Install Container Images
In this step, you will compile the Perseus container as a Docker image, and run it locally via Docker Compose.

### Build Containers
In the CDA-PEP directory, in a separate terminal session, execute:
```
$ make compile
```

This will commence pulling container images, building them locally, and registering them with the Docker Engine.

Go get a coffee and come back in a few mins.

...

...

Once finished, you should see something that looks like this:
```
$ docker images

REPOSITORY                                      TAG                 IMAGE ID            CREATED             SIZE
cda-data-catalog-service-api_dcs_api            latest              953fb2344d2b        3 days ago          857MB
custom/postgres_extensions_image                latest              bafb2f0ce9d3        4 days ago          542MB
postgres                                        9.6                 6eeaec6956fc        4 days ago          229MB
dev/dcs                                         latest              600aaef026ca        5 days ago          993MB
postgres                                        9.6.10              0178d5af9576        12 days ago         229MB
node                                            8                   55791187f71c        2 weeks ago         673MB
hello-world                                     latest              2cb0d9787c4d        7 weeks ago         1.85kB
fenglc/pgadmin4                                 latest              f7ec662a65ad        5 months ago        853MB
docker.elastic.co/elasticsearch/elasticsearch   5.4.0               865382d9b822        14 months ago       511MB
docker.elastic.co/kibana/kibana                 5.4.0               e4fe4d5612a2        16 months ago       639MB
mobz/elasticsearch-head                         5                   b19a5c98e43b        20 months ago       824MB
```

### Run

In the CDA-PEP directory, execute:
```
$ make up
```

This will start the process of spinning up the compiled images (see above).


Verify the containers are up and running:
```
$ docker ps
```


### Health Check
Once your app is running, you can send a health check with *curl* or *Postman* to `http://localhost:8080/health`

You should see this:
```
$ curl -v http://localhost:8080/health
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 8080 (#0)
> GET /health HTTP/1.1
> Host: localhost:8080
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< X-Powered-By: Express
< Content-Type: application/json; charset=utf-8
< Content-Length: 2
< ETag: W/"2-l9Fw4VUO7kr8CvBlt4zaMCqXZ0w"
< X-Response-Time: 1.402ms
< Vary: Accept-Encoding
< Date: Tue, 04 Sep 2018 17:57:04 GMT
< Connection: keep-alive
<
* Connection #0 to host localhost left intact
[]%
```

### Development with Docker
While containers are running, you can write code in your favorite IDE. 
The docker-compose.yml file contains a volume-mount declaration that will sync your 
local code-changes into the docker container context automatically.

However you will still need to restart your service in order to pick up the changes.

You can do that with:
```
$ make reload
```

### Stopping the Service
```
$ make down
```

### Makefile Target Summary

* *up* -  Start the service.
* *down* - Stop the service.
* *compile* - Compile new container images.
* *tests* - Run the unit tests.
* *clean_build* - Compile, Start the service.
* *start* - Start the service.
* *clean* - Delete old docker containers, volumes, and logs.
* *reload* Reload the service.



### Docker Cheat Sheet

Official Docs [here](https://docs.docker.com/engine/reference/commandline/cli/)

Here are some selected commands I use:

#### Get a list of running containers
```
$ docker ps
```

#### Get a list of *all* containers, running or not
```
$ docker ps -a
```

#### Get a list of docker images
```
$ docker images
```

#### Login to a running docker container
```
$ docker ps

Note the container ID of the container you want to login to.

$ docker exec -it <CONTAINER_ID> bash

This will drop you into the container context at the root. To leave, type 'exit'.
```

#### Get logs from running docker container
```
$ docker logs <CONTAINER_ID>

This will only display the first 100 hundred lines. And, depending on how logging is configured, may not be comprehensive. In order to get comprehensive logs, you will need to login to the container (see command above), and navigate to /var/log in order to see them.

```


## Running the tests with Docker
Running the tests with a container running is very easy. Just run the following in a terminal:
```
make tests
```
