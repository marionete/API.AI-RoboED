Artificial Intelegincia simsimi request via webapp for API.AI

## Instructions:
Open the `config.py` file and to configure it, you will add your keys and add the other information as requested - follow the example below:

>> * debug = False
>> * ChatADM = "-10002303823" ### CHAT FROM ADM
>> * source = "ROBOED" ### Name of the source
>> * WeatherKey = "adaeqaweqegtewrrhhewr"
>> * token = "145641654:n2l3n2bn43b2kj4bbjb24" ## TOKEN KEY FROM BOOT FROM TELEGRAM

Then open the `app.py` file and configure what is required, follow the examples below:

>> * result = urllib.urlopen(AiApi.format(host="HostFromAi", BotID="botid", msg=MsgTxt)).read() ## DEFINING URL


Then create an account at https://api.ai/ and follow the steps below

* Step 1

Sign up to Heroku (or sign in if you already have an account).

* Step 2

click 'Deploy to Heroku' button.

# Deploy to:
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


* Step 3

The Heroku site will open and you will be asked to fill in the name of the application. Enter the name of the application (choose any name) and click the 'Deploy for Free' button.

* Step 4

Create an API.AI agent and enable webhook:

>> * Click on Fulfillment in the left side menu

>> * Turn Webhook on

>> * Insert the link `https://[App Name].herokuapp.com/webhook` into the URL field

>> * Click ‘Save’.

For your own service, you may want to secure it with basic auth and/or headers (if you don’t want other people using your web hooks).

* Step 5

Create a return intent that matches your artificial intelligence requests. The action should be set to `input.unknown`, make sure the 'Enable webhook for this intent' option in the 'Fulfillment' section is checked. And the 'Text response' field, define the response that will be displayed in case of web service errors, do the same for the other function, but define the action of each as defined in the 'app.py' file - The following are the actions of each function below:

>> * AIResquest = input.unknown
>> * Weather = WeatherRequest
>> * Feedback = Feedback

* Step 6

You can now test requests for each action in the API.AI test console.

## In the returned JSON, the “fulfillment” object will look like this:

>>
`{
  "id": "2j3nb2obh3ob2o3bo2-b3olkn2lk3n2",
  "timestamp": "2017-01-05T22:52:17.269Z",
  "result": {
    "source": "agent",
    "resolvedQuery": "ed",
    "action": "input.unknown",
    "actionIncomplete": false,
    "parameters": {
      "any": "ed"
    },
    "contexts": [],
    "metadata": {
      "intentId": "j2bn3oj-kb2j3blj2bn3ljb2ljk3bjkl",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "true",
      "intentName": "IA"
    },
    "fulfillment": {
      "speech": "Eu?\n\n",
      "source": "ROBOED",
      "displayText": "Eu?\n\n",
      "messages": [
        {
          "type": 0,
          "speech": "Eu?\n\n"
        }
      ]
    },
    "score": 1
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "21hkj12bh3kjb1k3bb23bk-jb2jk3b"
}`
