#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)
API_CONPET = ''
error_msg = [""]

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:" + json.dumps(req, indent=4))
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    if req.get("result").get("action") != "ApiConpet":
        return {}
        if host is None:
            return {
                "speech": "ERROR BOT! Missing the host",
                "displayText": "ERROR BOT! Missing the host",
                "source": "ApiSimsimi"
            }
    text = makeTextQuery(req).encode('utf8')
    if text == False:
        return {
            "speech": "ERROR BOT! " + random.choice(error_msg),
            "displayText": "ERROR BOT! " + random.choice(error_msg),
            "source": "ApiConpet"
        }
    url = API_CONPET + makeTextQuery(req).encode('utf8')
    result = urllib.urlopen(url).read()
    res = makeWebhookResult(result)
    return res

def makeTextQuery(req):
    mentioned_text = req.get("result").get("resolvedQuery")
    if mentioned_text is None:
        return False
    return mentioned_text

def makeWebhookResult(result):
    print("Response: " + result)
    return {
        "speech": result,
        "displayText": result,
        "source": "ApiConpet"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port: %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
