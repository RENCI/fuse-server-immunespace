#!/bin/bash

set -a
source .env
set +a

export TEST_LIBRARY=1

PYTHONPATH=. pytest -rxXs ${TAP_STREAM}


