import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds159180.mlab.com:59180/txgd
host = "ds159180.mlab.com"
port = 59180
db_name = "txgd"
username = "txgd"
password = "admin"
def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())
