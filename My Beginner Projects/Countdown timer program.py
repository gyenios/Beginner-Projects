import time
my_time = int(input('Enter the time in seconds:  '))
for t in range (my_time,0,-1): #Reversed range

    secs = t%60 # if t is less than 60, the remainder is t itself

    mins = (t/60)%60 # t converted to mins and modulo applied to get remainder

    hrs = (t/360)%60 # t converted to hours and modulo applied to get remainder

    print(f'{int(hrs):02}:{int(mins):02}:{int(secs):02}') # introduced 0 padding to enhanace appearance
    
    time.sleep(1)
print('Time\'s is up')
