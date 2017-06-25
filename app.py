#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# encoding: utf-8

import random, urllib, json, re, datetime, os, lang
from config import *
from utils import *
from methods import *
from request import *
from urllib2 import quote
from flask import flash, request, render_template, Flask, make_response

app = Flask(__name__)
@app.route('/webhook', methods=['POST']) ## DEFINING METHOD POST
def webhook():
    req = request.get_json(silent=True, force=True)
    res = AIResquest(req) or Weather(req) or Feedback(req) ## DEFINING WEBHOOK FOR FUNCTION
    res = json.dumps(res, indent=4)
    print("Request: " + json.dumps(req, indent=4))
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def AIResquest(req):
 if req.get("result").get("action") != "input.unknown": ## DEFINING THE PREFIX TO EXECUTE FUNCTION
     return {}
 MsgTxt = req.get("result").get("parameters").get("any").encode('utf8')
 print("Request: " + json.dumps(req, indent=4))
 result = urllib.urlopen(AiApi.format(host="www.ed.compet.gov", BotID="423177099", msg=MsgTxt)).read() ## DEFINING URL
 clean = re.compile('<[^<>]*>') ## REMOVING HTML
 result = re.sub(clean, '', result)
 print("Response: " + result)
 return {
     "speech": result,
     "displayText": result,
     "source": source
 }

def Weather(req):
    if req.get("result").get("action") != "WeatherRequest": ## DEFINING THE PREFIX TO EXECUTE FUNCTION
        return {}
    city = req.get("result").get("parameters").get("geo-city").encode("utf8")
    clean = re.compile('ã') ## REMOVING ERROR UTF8
    city = re.sub(clean, 'a', city)
    city = urllib.quote(city.encode("utf8")) ## REMOVING ACCENTUATION
    result = urllib.urlopen(WeatherRequest.format(cidade=city, key=WeatherKey)).read() ## DEFINING URL
    query = json.loads(result) ## LOADING JSON TO SELECT SOME PARAMETERS
    main = query.get('main')
    speech = lang.WeatherMSG.format(cidade=query.get('name'), temperatura=main.get('temp') + 3)
    return {
        "speech": speech,
        "displayText": speech,
        "source": source
    }

def Feedback(req):
    if req.get("result").get("action") != "Feedback":  ## DEFINING THE PREFIX TO EXECUTE FUNCTION
        return {}
    MsgTxt = req.get("result").get("parameters").get("any").encode('utf8')
    email = req.get("result").get("parameters").get("email").encode('utf8')
    speech = lang.MsgSucesso
    speech_TG = lang.MsgFeedback.format(email=email, msg=MsgTxt)
    sendMessage(chat_id=ChatADM, text=speech_TG, parse_mode='Markdown') ## FUNCTION FOR SENDING MSG OF THE SUPPORT TO THE TELEGRAM
    return {
        "speech": speech,
        "displayText": speech,
        "source": source
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port: %d" % port)
    app.run(debug=debug, port=port, host='0.0.0.0')
