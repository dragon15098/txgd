import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds157040.mlab.com:57040/txgd
host = "ds157040.mlab.com"
port = 57040
db_name = "txgd"
username = "admin"
password = "admin"
def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())
