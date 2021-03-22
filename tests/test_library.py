from fuse.server.immunespace.dispatcher import GetObject
import json
import os
import pytest
import numpy as np

# this takes about 20s to return
# go get a session id and group objectIdfrom immunespace for  user for this to work:
# https://www.immunespace.org/security/externalToolsView.view?returnUrl=%2Fproject%2FStudies%2Fbegin.view%3F
#g_debug = True
g_debug = False
def test_GetObject():

    if os.getenv('TEST_LIBRARY') == "0":
        pytest.skip("Only testing docker container")

    objectId = os.getenv('GROUP')
    username = os.getenv('USERNAME')
    sess = os.getenv('APIKEY')

    obj = {
        "id": objectId,
        "resourceType": "eset",
        "resource": GetObject(objectId,sess,username)
    }

    with open('tests/expected/test_1.json', 'r', encoding='utf-8') as f:
        expected = json.load(f)

    #make smaller chunks for easier debugging
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
        
    # Uncomment this to capture output:
    #with open('tests/test_1.out.json', 'w', encoding='utf-8') as f:
    #     json.dump(obj, f, ensure_ascii=False, indent=4, sort_keys=True)

    objs = json.dumps(obj, ensure_ascii=False, indent=4, sort_keys=True)
    expecteds = json.dumps(expected, ensure_ascii=False, indent=4, sort_keys=True)

    if(g_debug):
        print("obj:")
        print(obj["resource"]["exprs"])
        #print("expected:")
        #print(expected["resource"]["exprs"])
        
    # xxx sort the keyes, then copy this to test_func.py
    assert objs == expecteds

