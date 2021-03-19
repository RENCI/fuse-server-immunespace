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
    sess = os.getenv('APIKEY')
    if sess == None:
        sess="TEST"
        # xxx AND return 505

    return {
        "id": objectId,
        "resourceType": "eset",
        "resource": GetObject(objectId,sess)
    }


