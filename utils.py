####################################### By @TiagoDanin #######################################
from config import *
from PythonColorize import *
import datetime
def add_log(f=None, type_=None, save=None):
	time = datetime.datetime.now()
	if print_log:
		type_  = colors.lg_red + type_ + colors.nocolor
		time   = colors.lg_blue + str(time) + colors.nocolor
		f      = colors.green + str(f) + colors.nocolor
		div    = colors.lg_yellow + '----' + colors.nocolor
		text   = '\n{div}\t{type_}\t{div}\t{time}\t{div}\n{f}\n\n'.format(div=div,
																	type_=type_,
																	time=time,
																	f=f)
		print(text)
	return
