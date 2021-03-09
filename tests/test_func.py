import requests
from pathlib import Path
import logging
import os
import json

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

appliance="http://fuse-server-immunespace:8080"
# xxx log.info(f"starting on port (${API_PORT})")

json_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def test_config():
    config_path = Path(__file__).parent / "config.json"
    with open(config_path) as f:
        config=json.load(f)
    resp = requests.get(f"{appliance}/config")
    assert resp.json() == config


json_headers = {
    "Accept": "application/json"
}

# other endpoint tests, start with "test_"


# xxx kludged for now
obj = {
    "id": "1",
    "resourceType":"eset",
    "value": {"6005":1.5, "622":0.74, "6120":0.33, "22934":1.2}
}
def test_object():
    resp = requests.get(f"{appliance}/Object/{1}")
    assert resp.json() == obj
