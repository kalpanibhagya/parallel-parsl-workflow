
import parsl
import os
from parsl.app.app import python_app, bash_app

from datetime import datetime

# import configuration files
#===============================
#from local_threads import local_threads
#from local_htex import local_htex
from remote_htex import remote_htex


#parsl.load(local_threads)
#parsl.load(local_htex)
parsl.load(remote_htex)

def getDuration(startTime,endTime):
	difference = endTime - startTime
	#difference = difference.strftime("%H:%M:%S")
	return difference

# App that generates a random number after a delay
@python_app
def generate(limit,delay):
    from random import randint
    import time
    time.sleep(delay)
    return randint(1,limit)

startTime = datetime.now().replace(microsecond=0)
print('Start Time: ' + str(startTime) + '\n')

# Generate 5 random numbers between 1 and 10
rand_nums = []
for i in range(10):
    rand_nums.append(generate(10,i))


# Wait for all apps to finish and collect the results
outputs = [i.result() for i in rand_nums]

endTime = datetime.now().replace(microsecond=0)

print('\nEnd Time: ' + str(endTime) + ' Caluculation Done!\n')
print('Duration ' + str(getDuration(startTime,endTime)))

# Print results
print(outputs)
