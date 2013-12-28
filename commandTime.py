import time
import sys
import cmd

class startTime(cmd.Cmd):
	"""Python timer from the command line"""

	def do_startTime(self, minutes):
		if minutes:
			minutes = float(minutes)
			start_time = time.time()
    		seconds = minutes * 60
    		print 'Starting ' + str(minutes) + ' minute timer'
    		time.sleep(seconds)
    		print 'Timer is up '

	def do_EOF(self, line):
	    return True

if __name__ == '__main__':
	startTime().cmdloop()