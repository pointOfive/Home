import time, sys

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #Python 2
        sys.stdout.write("\r" + timeformat)
        sys.stdout.flush()
        #Python 3
        #print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n\n\n\n')
