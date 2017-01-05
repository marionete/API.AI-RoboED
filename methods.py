####################################### By @TiagoDanin #######################################
from request import request_telgram
import json

def check_querys(chat_id=None, text=None, parse_mode=None, disable_web_page_preview=None,
				disable_notification=None, reply_to_message_id=None, reply_markup=None,
				inline_keyboard=None, photo=None, caption=None):

	querys = {}
	file_ = {}
	if chat_id:
		querys['chat_id'] = chat_id
	if text:
		querys['text'] = text
	if parse_mode:
		querys['parse_mode'] = parse_mode
	if disable_web_page_preview:
		querys['disable_web_page_preview'] = disable_web_page_preview
	if disable_notification:
		querys['disable_notification'] = disable_notification
	if reply_to_message_id:
		querys['reply_to_message_id'] = reply_to_message_id
	if reply_markup:
		querys['reply_markup'] = reply_markup
	if inline_keyboard:
		querys['reply_markup'] = '{"inline_keyboard":' + inline_keyboard + '}'
	if photo:
		file_['photo'] = photo
	if caption:
		querys['caption'] = caption
	return querys, file_

#https://core.telegram.org/bots/api/#available-methods


def sendMessage(chat_id=None, text=None, parse_mode=None, disable_web_page_preview=None,
				disable_notification=None, reply_to_message_id=None, reply_markup=None,
				inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							text=text,
							parse_mode=parse_mode,
							disable_web_page_preview=disable_web_page_preview,
							disable_notification=disable_notification,
							reply_to_message_id=reply_to_message_id,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendMessage', querys, file_)

def sendPhoto(chat_id=None, photo=None, caption=None, disable_notification=None,
				reply_markup=None, inline_keyboard=None):

	querys, file_ = check_querys(chat_id=chat_id,
							photo=photo,
							caption=caption,
							disable_notification=disable_notification,
							reply_markup=reply_markup,
							inline_keyboard=inline_keyboard)
	return request_telgram('sendPhoto', querys, file_)
