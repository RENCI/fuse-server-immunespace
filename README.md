[![AppVeyor](https://img.shields.io/docker/cloud/build/txscience/fuse-server-immunespace?style=plastic)](https://hub.docker.com/repository/docker/txscience/fuse-server-immunespace/builds)

# fuse-server-immunespace

Clone this repo to create a new FUSE-style appliance.

FUSE stands for "[FAIR](https://www.go-fair.org/)", Usable, Sustainable, and Extensible.

FUSE appliances can be run as a stand-alone appliance (see `up.sh` below) or as a plugin to a FUSE deployment (e.g., [fuse-immcellfie](http://github.com/RENCI/fuse-immcellfie)). FUSE appliances come in 3 flavors:
* server: provides a common data access protocol to a digital object server
* mapper: maps the data from a particular server type into a common data model with consistent syntax and semantics
* analysis: analyzes data from a mapper, providing results and a specification that describes the data types and how to display them.

## prerequisites:
* python 3.8 or higher
* Docker 20.10 or higher
* docker-compose v1.28 and 3.8 in the yml
* cargo 1.49.0 or higher (for installing dockerfile-plus)

Tips for updating docker-compose on Centos:

```
sudo yum install jq
VERSION=$(curl --silent https://api.github.com/repos/docker/compose/releases/latest | jq .name -r)
sudo mv /usr/local/bin/docker-compose /usr/local/bin/docker-compose.old-version
DESTINATION=/usr/local/bin/docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m) -o $DESTINATION
sudo chmod 755 $DESTINATION
```

## configuration

1. Get this repository:
`git clone --recursive http://github.com/RENCI/fuse-server-immunespace

2. Install dockerfile-plus:
`cargo build`

2. Copy `sample.env` to `.env` and edit to suit your server:
* __API_PORT__ pick a unique port to avoid the `up.sh` and `./tests/test.sh` commands from colliding with other installations on the same server

Don't change these:
* __DOCKER_BUILDKIT__ required for dockerfile-plus (INCLUDE+ instruction)
* __COMPOSE_DOCKER_CLI_BUILD__ required for dockerfile-plus (INCLUDE+ instruction)

## start
```
./up.sh
```

## validate installation
```
curl -X GET http://localhost:8082/config
```

## stop
```
./down.sh
```
## regression testing
For repo owners:

Upon any commit to the `main` or tagged branches, this repo will be pulled by dockerhub and `tests/test.sh` will be run. In order for the tests to pass, any variables required to be set in `.env` must also be set in Dockerhub's 'configure automated builds' section of the [txscience/fuse-server-immunespace dockerhub repo](https://hub.docker.com/repository/docker/txscience/fuse-server-immunespace/builds). The tag on this README will indicate testing status of the last commit.
