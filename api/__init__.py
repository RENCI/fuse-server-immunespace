import os
import logging
from pathlib import Path
from fuse.server.immunespace.dispatcher import GetObject

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add one "get_" function for each operationId in the ./openapi/api.yml file

import json
def get_config():
    config_path = Path(__file__).parent.parent / "config.json"
    with open(config_path) as f:
        return json.load(f)

# xxx kludged for now
# how does session get passed in?
def get_object(objectId):
    # sess = os.environ(['APIKEY']
    # sess = "session|056401be3718ed9e1a34391bd78ad335" # xxx kludged
    sess = "TEST" # xxx kludged
    return {
        "id": objectId,
        "resourceType": "eset",
        "resource": GetObject(objectId,sess)
    }


