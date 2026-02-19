#RC 1st, Code that manage the last time it was updated

#Import time for management
import time

#Create function to load the time
def read_time():
    #Get a reable time
    current_time = time.time()
    readable_time = time.ctime(current_time)
    #Return readble time
    return readable_time
     