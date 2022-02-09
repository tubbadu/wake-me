#!/usr/bin/python3

# 
# wake-me in 5m 2h 
#

import os
import subprocess
import sys
import datetime
import time

def set_procname(Newname):
	newname = bytes(Newname, 'utf-8')
	from ctypes import cdll, byref, create_string_buffer
	libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
	buff = create_string_buffer(len(newname)+1) #Note: One larger than the name (man prctl says that)
	buff.value = newname                 #Null terminated string as it should be
	libc.prctl(15, byref(buff), 0, 0, 0) #Refer to "#define" of "/usr/include/linux/prctl.h" for the misterious value 16 & arg[3..5] are zero as the man page says.

def bash(cmd, read=False):
	if read:
		try:
			x = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			x = False
		return x
	else:
		os.system(cmd)
		return
def Help():
	pass


def main():
	args = list()
	flags = list()
	for arg in sys.argv[1:]:
		if arg[0] == '-':
			flags.append(arg)
		else:
			args.append(arg)

	if len(args) == 0 or '-h' in flags or '--help' in flags:
		Help()
		exit()

	if len(args) < 2:
		print('Patrameter Error')
		exit()
	########################################
	t = 0
	if args[-1][0].isnumeric():
		msg = "wake-me"
		argz = args[1:]
	else:
		msg = args[-1]
		argz = args[1:-1]
	
	set_procname(msg)
	
	if args[0] in "in/tra/fra".split("/"):
		for arg in argz:
			if('s' in arg):
				try:
					t += int(arg.replace('s', '')) * 1
				except:
					print("skipping argument:", arg)
			elif('m' in arg):
				try:
					t += int(arg.replace('m', '')) * 60
				except:
					print("skipping argument:", arg)
			elif('h' in arg):
				try:
					t += int(arg.replace('h', '')) * 3600
				except:
					print("skipping argument:", arg)
			elif('d' in arg):
				try:
					t += int(arg.replace('d', '')) * 86400
				except:
					print("skipping argument:", arg)
	elif args[0] in "at/alle".split("/"):
		at = args[1].replace('.', ':').split(':') # h or h:m or h:m:s
		for i in range(3 - len(at)):
			at.append('0')
		at = datetime.datetime.now().strftime("%Y-%m-%d ") + at[0] + ':' + at[1] + ':' + at[2]
		at = datetime.datetime.strptime(at, "%Y-%m-%d %H:%M:%S")
		nt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		nt = datetime.datetime.strptime(nt, "%Y-%m-%d %H:%M:%S")
		t = (at - nt).total_seconds()
		if t < 0:
			at += datetime.timedelta(1)
			t = (at - nt).total_seconds()
		#print(at, "\n", nt)
	
	
	print("waking you in", t, 'seconds, at', (datetime.datetime.now() + datetime.timedelta(seconds=t)).strftime("%H:%M:%S"))
	time.sleep(t)
	bash(f"kdeconnect-cli -n SM-A750FN --ping-msg '{msg}'")
	if not ('-m' in flags or '--mute' in flags):
		if not ('-s' in flags):
			bash(f'say {msg}')
		else:
			bash('spd-say "beep beep"')
	ret = bash(f'dunstify -a "wake-me" -i "ktimer" -A "+5m","+5m" -A "+15m","+15m" -A "+30m","+30m" -A "+1h","+1h" -A "+{int(t)}s","+{int(t)}s" -A "off","off" "{msg}" -t 0', read=True).strip()
	if ret[0] == '+':
		print('\npostponing:', ret)
		bash(f'wake-me in {ret[1:]} "{msg}" ' + ' '.join(flags))
	else:
		print('\nturned off')
		exit()


if __name__ == "__main__":
	main()
