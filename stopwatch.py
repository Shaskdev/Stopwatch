#Create simple stopwatch
import time
print('Press ENTER to START timing. Press ENTER again to "click" the stop watch. Use CTRL-C to STOP.')
input()
print('STARTED')
start_time =  time.time()  # Get the start time
last_time = start_time
lapNum =  1

# start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - last_time, 2)
        totalTime = round(time.time() - start_time, 2)
        print('Lap %#s: %s (%s)' % (lapNum, lapTime, totalTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Handle the  CTRL-C exception to keep its error message from displaying
    print('\nDone.')
