from fuse.server.immunespace.dispatcher import GetObject
import json

# this takes about 20s to return
# go get a session id and group objectIdfrom immunespace for  user for this to work:
# https://www.immunespace.org/security/externalToolsView.view?returnUrl=%2Fproject%2FStudies%2Fbegin.view%3F
def test_GetObject():

    objectId="cellfie_group2"
    sess="TEST"
    #sess = os.environ(['APIKEY'])
    #sess = os.environ("TEST")

    obj = GetObject(objectId, sess)
    print(json.dumps(obj, indent=4, sort_keys=True))

    # Uncomment this to capture output:
    # with open('tests/test_1.json', 'w', encoding='utf-8') as f:
    #     json.dump(obj, f, ensure_ascii=False, indent=4)

    with open('tests/expected/test_1.json', 'r', encoding='utf-8') as f:
        expected = json.load(f)

    assert obj == expected 

