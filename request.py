####################################### By @TiagoDanin #######################################
from objectjson import ObjectJSON
import config, utils, requests

def request_url(url, type=None, params=None, headers=None, auth=None, files=None, setime=None):
	time = config.timeout
	if setime:
		time = setime
	try:
		data = requests.get(url, params=params, headers=headers, auth=auth, files=files, timeout=time)
	except Exception as error:
		utils.add_log(str(error) + '\nURL: ' + str(url), 'Request-Except', True)
		return False

	if data.status_code == 200:
		return data
	else:
		utils.add_log('Error in request! {}\n{}\n\n{}'.format(url, params, data.text), 'Request', True)
	return False

def request_telgram(method, query=None, file_=None):
	url = config.telegram.format(token=config.token) + method
	data = request_url(url, params=query, files=file_, setime=config.timeout)
	if data == False:
		return False, False
	try:
		json_str = data.json()
	except:
		return False, False
	json_obj = ObjectJSON(json_str)
	return json_obj, json_str
