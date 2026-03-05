from urllib.parse import urlparse
import hashlib

TMP_DIR = 'tmp/'

def cache_file(url:str, name:str, type:str='json'):
    ## this is the __init__() for Cache?
    tmp_dir:str = TMP_DIR
    #try:
    u = urlparse(url)
    #pprint(u)
    f = f"{tmp_dir}{u.netloc}.{name}"

    hashkey:str = f + u.query + u.params
    #try:
    hash = hashlib.sha256(hashkey.encode()).hexdigest()[:8]
    f += f".{hash}.{type}"

    #print("F is:", f)
    return f









