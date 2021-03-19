#!/bin/bash

set -e

export $(cat tests/test.env|grep -v '^#')
export TEST_LIBRARY=0

docker-compose -f docker-compose.yml -f tests/docker-compose.yml up --build -V 

#fuse-server-immunespace 
