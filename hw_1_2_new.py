time_sec = int(input("Enter the time in seconds: "))
hour = time_sec//3600
minute = (time_sec - (hour*3600))//60
sec = time_sec - hour*3600 - minute*60
time = '{:02d}:{:02d}:{:02d}'.format(hour, minute, sec)

print(time)