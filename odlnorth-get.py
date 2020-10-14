#!/usr/bin/python
import json
import requests
from requests.auth import HTTPBasicAuth


def http_get(url):
    url = url
    headers = {'Content-Type': 'application/json'}
    resp = requests.get(url, headers=headers,
                        auth=HTTPBasicAuth('admin', 'admin'))
    return resp


if __name__ == "__main__":
    url = 'http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0/'
    resp = http_get(url)
    data = json.loads(resp.content)
    if data.get("errors"):
        print "active-flow(s): 0"
    else:
        print resp.content
        print "active-flow(s): " + str(len(data["flow-node-inventory:table"][0]["flow"]))
