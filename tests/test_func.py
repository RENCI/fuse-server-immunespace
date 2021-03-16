import requests
from pathlib import Path
import logging
import os
import json
import pytest

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

appliance="http://fuse-server-immunespace:8080"
# xxx log.info(f"starting on port (${API_PORT})")

json_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def test_config():
    pytest.skip("Not testing docker container") # xxx

    if os.getenv('TEST_LIBRARY') == 0:
        pytest.skip("Not testing docker container")

    config_path = Path(__file__).parent.parent / "config.json"
    with open(config_path) as f:
        config=json.load(f)
    resp = requests.get(f"{appliance}/config")
    assert resp.json() == config


json_headers = {
    "Accept": "application/json"
}

# other endpoint tests, start with "test_"


# xxx kludged for now
def test_object():
    pytest.skip("Not testing docker container") # xxx

    if os.getenv('TEST_LIBRARY') == 0:
        print("***NOT RUNNING TEST["+os.getenv('TEST_LIBRARY')+"]***")
        pytest.skip("Not testing docker container")

    obj = requests.get(f"{appliance}/Object/TEST")
    print("***RAN TEST!!!***")

    with open('tests/expected/test_1.json', 'r', encoding='utf-8') as f:
        expected = json.load(f)

    assert obj == expected 

