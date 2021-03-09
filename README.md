[![AppVeyor](https://img.shields.io/docker/cloud/build/txscience/fuse-appliance-template?style=plastic)](https://hub.docker.com/repository/docker/txscience/fuse-appliance-template/builds)

# fuse-appliance-template

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

## use this template:

Note, an applianece must specify a pluginType, so for the purpose of this demonstration we ues type 's' (for digital object 'Server')
* To add a new repository to the RENCI organization, [click here](https://github.com/organizations/RENCI/repositories/new) and select this repo for the template, otherwise new repo will be added to your username.
* Get your new repo using the 'recursive' tag (see below)
```
git clone --recursive http://github.com/RENCI/<your-repo-name>
```
* Make sure the following passes exactly 1 test: `./tests/test.sh`
* Edit this README.md file and replace all occurrences of `fuse-appliance-template` with your repo's name
* Update the source files appropriately:
 - [ ] **config.json**: describe your appliances pluginType ["s":"Server", "m":"Mapper", "a":"Analysis"], required parameters, supported selector values, and supported/required objectVariables
 - [ ] **docker-compose.yml**: replace `fuse-appliance-template` with your repo's name and customize accordingly
 - [ ] **requirements.txt**: add your *version-locked* library requirements to the list
 - [ ] **sample.env**: add any required environmental variables, don't forget to also document them in this readme
 - [ ] **api/openapi.yml**: 
   - [ ]  Search for all occurrences of `fuse-appliance-template` and replace
   - [ ] Define and add endpoints for your appliance
   - [ ] Define the openApi for your appliance, adding an `operationId:` for each endpoint using pattern `api.get_<endpoint>`
 - [ ] **api/__init__.py**: Add one "get_" function for each operationId in the ./openapi/api.yml file
 - [ ] ...optionally... create **api/routes.py**: map a 'route' function to each of the endpoints handled by __init__.py for readability(?)
 - [ ] ...optionally... create **api/src/app.py**: that can be included into a python library to support non-openapi access to the appliance's logic (to run the application logic in a more performant, imported library instead of as a stand-alone appliance)
 - [ ] **tests/test_func.py**: replace fuse-server-immunespace with your repo name and add tests for your endpoints
 - [ ] **tests/docker-compose.yml**: replace fuse-appliance-template with your repo name
 - [ ] **tests/test.sh**: same as above
 - [ ] add any tools you need to share across appliances to `tx-utils`
 - [ ] make sure the following passes all tests: `./tests/test.sh`
 - [ ] contact the dockerhub/txscience organization administrator (email:txscience@lists.renci.org) to add a dockerhub repo for your container
* remove this section from the README.md
* checkin your mods: 
```
git status # make sure everything looks OK
git commit -a -m 'Initial customization'
git push
```

## configuration

1. Get this repository:
`git clone --recursive http://github.com/RENCI/fuse-appliance-template

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

Upon any commit to the `main` or tagged branches, this repo will be pulled by dockerhub and `tests/test.sh` will be run. In order for the tests to pass, any variables required to be set in `.env` must also be set in Dockerhub's 'configure automated builds' section of the [txscience/fuse-appliance-template dockerhub repo](https://hub.docker.com/repository/docker/txscience/fuse-appliance-template/builds). The tag on this README will indicate testing status of the last commit.
