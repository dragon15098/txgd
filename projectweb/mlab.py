import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds151450.mlab.com:51450/txgd
host = "ds151450.mlab.com"
port = 51450
db_name = "txgd"
username = "txgd"
password = "txgd"
def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())
