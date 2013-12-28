#!/usr/bin/env python

import time
import os
import sys
import argparse

start_time = time.time()


def main(args):
    parser = argparse.ArgumentParser(description='timer from the command line', prog='timer')
    parser.add_argument('minutes', type=int)
    parser.add_argument('message', nargs='*', type=str)
    opts = parser.parse_args(args) # command line arguments
    startTimer(opts.minutes, opts.message)

def startTimer(minutes, message):

    message = ' '.join(message)

    # COMMENTS FOR SAIDEL

    # os.system() sends a comman do the bash prompts as a raw string
    # notify-send is a bash program that gives you desktop notifications
    # someday you might want to implement this with Growl and the growlnotify extention,
    # which is the equivalent on Mac: https://itunes.apple.com/us/app/id467939042?mt=12
    # For now, you can simply replace the os.system calls with print statements
    
    print message
    seconds = minutes * 60
    print 'Starting ' + str(minutes) + ' minute timer'
    time.sleep(seconds)
    print 'Timer is up '+ message

if __name__ == '__main__':    
    main(sys.argv[1:])

