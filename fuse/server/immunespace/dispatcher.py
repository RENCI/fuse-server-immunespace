# xxx implement a cache like this:
# import fuse.server.cache as cache

import docker


# library API
# from fuse.server.immunespace.dispatcher import GetObject
def GetObject(objectId,sess):
    resc = _get_object(objectId, sess)

    if resc is not None:
        return resc
    else:
        return "not found", 404

# internal methods
def unique_pairs(n):
    """Produce pairs of indexes in range(n)"""
    for i in range(n):
        for j in range(i+1, n):
            yield i, j

# process lists returned from ImmGeneBySampleMatrix
def make_matrix(mxbytes):
    mxbytes = mxbytes.decode('utf-8')
    mxbytes= [l.split(",") for l in mxbytes.split("\n")]
    del mxbytes[0]
    del mxbytes[-1]
    return mxbytes

def _get_object(objectId, sess):
    g_test= ""
    if(sess == "TEST"):
        g_test = "--test"

    # xxx implement a cache like this:
    # resc = cache.get_object(objectId)
    #if resc is not None:
    #    return resc

    client = docker.from_env()
    ret = client.containers.run("tx-immunespace-groups", "./ImmGeneBySampleMatrix.R "+ g_test + " -g " + objectId + " -a " + sess)

    scrap, experimentData, phenoMetadata, pdata, featureNames, exprs=ret.split(b"===")

    pdata=make_matrix(pdata)
    featureNames=make_matrix(featureNames)
    exprs=make_matrix(exprs)
    experimentData=make_matrix(experimentData)
    phenoMetadata=make_matrix(phenoMetadata)
    
    obj = { 
        "id": objectId,
        "pData":  pdata,
        "exprs":  exprs,
        "featureNames": featureNames,
        "system": "HUGO",
        "experimentData": experimentData,
        "phenoMetadata": phenoMetadata
    }
    

    resc=obj

    # xxx implement a cache like this:
    # cache.update_object(resc)

    return(resc)

