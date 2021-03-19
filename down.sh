#!/bin/bash

set -a
source .env
set +a

docker-compose -f docker-compose.yml down --remove-orphans
