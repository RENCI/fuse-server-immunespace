#!/bin/bash

export $(cat tests/test.env|grep -v '^#')
export TEST_LIBRARY=0

docker-compose -f docker-compose.yml -f tests/docker-compose.yml up --build -V  --timeout 600 --exit-code-from fuse-server-immunespace-test
