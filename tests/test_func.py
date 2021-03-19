import requests
from pathlib import Path
import logging
import os
import json
import pytest

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

appliance="http://fuse-server-immunespace:8080"
log.info(f"starting ("+appliance+")")

json_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def test_config():
    if os.getenv('TEST_LIBRARY') == "1":
        pytest.skip("Only testing docker lib")

    if os.getenv('TEST_LIBRARY') == 1:
        pytest.skip("Not testing docker container")

    config_path = Path(__file__).parent / "config.json"
    with open(config_path) as f:
        config=json.load(f)
    resp = requests.get(f"{appliance}/config")
    assert resp.json() == config


json_headers = {
    "Accept": "application/json"
}

# other endpoint tests, start with "test_"

import numpy as np
#g_debug = True
g_debug = False
def test_object():

    if os.getenv('TEST_LIBRARY') == "1":
        pytest.skip("Only testing docker lib")

    objectId = "cellfie_group2"
    sess = os.getenv('APIKEY')

    log.info(f"Asking for ({objectId}) with API key ({sess})")

    obj = requests.get(f"{appliance}/Object/{objectId}").json() # decode('utf-8')

    with open('tests/expected/test_1.json', 'r', encoding='utf-8') as f:
        expected = json.load(f)


    if(g_debug):
        max_subjs=3
        max_pheno=4
        max_genes=5
        obj["resource"]["exprs"] = np.array(obj["resource"]["exprs"])[0:max_genes,0:max_subjs].tolist() # 3 genes, 2 subjects
        obj["resource"]["featureNames"] = np.array(obj["resource"]["featureNames"])[0:max_genes].tolist()
        obj["resource"]["pData"] = np.array(obj["resource"]["pData"])[0:max_pheno,0:max_subjs].tolist() # 4 phenoetypes, 2 subjects
        
        expected["resource"]["exprs"] = np.array(expected["resource"]["exprs"])[0:max_genes,0:max_subjs].tolist() # 3 genes, 2 subjects
        expected["resource"]["featureNames"] = np.array(expected["resource"]["featureNames"])[0:max_genes].tolist()
        expected["resource"]["pData"] = np.array(expected["resource"]["pData"])[0:max_pheno,0:max_subjs].tolist() # 4 phenoetypes, 2 subjects
        
    objs = json.dumps(obj, ensure_ascii=False, indent=4, sort_keys=True)
    expecteds = json.dumps(expected, ensure_ascii=False, indent=4, sort_keys=True)

    if(g_debug):
        print("obj:")
        print(obj["resource"]["exprs"])
        #print("expected:")
        #print(expected["resource"]["exprs"])
        

    objs = json.dumps(obj, ensure_ascii=False, indent=4, sort_keys=True)
    expecteds = json.dumps(expected, ensure_ascii=False, indent=4, sort_keys=True)
    
    assert objs == expecteds


