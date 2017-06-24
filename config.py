#-*- coding: utf-8 -*-
# encoding: utf-8
####################################### By @TiagoDanin #######################################
timeout = 5
debug = False
ChatADM = "70304549" ### CHAT FROM ADM
source = "http://www.ed.conpet.gov.br/mod_perl/bot_gateway.cgi -F server=0.0.0.0:8085 -F charset=utf-8 -F pure=1 -F js=0 -F msg="' .. input .. '"'" ### Name of the source
WeatherKey = ""
token = "423177099:AAGhY6jBPaqsWK2DmrwGxRePAenmNETPKRc" ## TOKEN KEY FROM BOOT FROM TELEGRAM
telegram = "https://api.telegram.org/bot{token}/"
AiApi = "http://www.{host}.br/mod_perl/bot_gateway.cgi?bot_id={BotID}&charset=utf-8&pure=1&js=0&msg={msg}"
WeatherRequest = "http://api.openweathermap.org/data/2.5/weather?q={cidade}&mode=json&units=metric&appid={key}"
