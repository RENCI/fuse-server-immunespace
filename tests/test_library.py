from fuse.server.immunespace.dispatcher import GetObject
import json
import os
import pytest

# this takes about 20s to return
# go get a session id and group objectIdfrom immunespace for  user for this to work:
# https://www.immunespace.org/security/externalToolsView.view?returnUrl=%2Fproject%2FStudies%2Fbegin.view%3F
def test_GetObject():

    if os.getenv('TEST_LIBRARY') == "0":
        pytest.skip("Only testing docker container")

    objectId = os.getenv('GROUP')
    sess = os.getenv('APIKEY')
    sess = "TEST" # xxx

    obj = {
        "id": objectId,
        "resourceType": "eset",
        "resource": GetObject(objectId,sess)
    }

    #xxxprint(json.dumps(obj, indent=4, sort_keys=True))

    # Uncomment this to capture output:
    #with open('tests/test_1.out.json', 'w', encoding='utf-8') as f:
    #     json.dump(obj, f, ensure_ascii=False, indent=4, sort_keys=True)

    with open('tests/expected/test_1.json', 'r', encoding='utf-8') as f:
        expected = json.load(f)

    objs = json.dumps(obj, ensure_ascii=False, indent=4, sort_keys=True)
    expecteds = json.dumps(expected, ensure_ascii=False, indent=4, sort_keys=True)

    # xxx sort the keyes, then copy this to test_func.py
    assert objs == expecteds

