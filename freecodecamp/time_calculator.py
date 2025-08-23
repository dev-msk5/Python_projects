# Freecodecamp - Scientific Calc. Python - Project No. 2

day_in_minutes = 24*60 #1440
half_day_in_minutes = 12*60
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
def add_time(start, duration, day=''):
   
    parts = start.strip().split()
    am_or_pm = parts[1]
    if am_or_pm == 'AM':
        am_or_pm=0
    else:
        am_or_pm = half_day_in_minutes
    actual_time_in_minutes = convert_time(parts[0]) + convert_time(duration) + am_or_pm
    # print(actual_time_in_minutes)
    if actual_time_in_minutes % day_in_minutes > half_day_in_minutes:
        daytime = 'PM'
    else:
        daytime = 'AM'
    n = actual_time_in_minutes // 1440 
    print(n)
    hour = ((actual_time_in_minutes // 60) if daytime == 'AM' else (actual_time_in_minutes // 60 - 12)) - n*24
    min = (actual_time_in_minutes - hour*60 if daytime == 'AM' else (actual_time_in_minutes - (hour+12)*60)) -n*24*60

    j=0
    if hour == 0:
        hour = 12
    if 10 > min:
        min='0'+str(min)
    if day!='':
        day=day.lower()
        for i in days:
            if i.lower()==day:
                day=days[(j+n)%7]
                if n > 0:
                    if n == 1:
                        new_time = f'{hour}:{min} {daytime}, {day} (next day)'
                    else:
                        new_time = f'{hour}:{min} {daytime}, {day} ({n} days later)'
                else:
                    new_time = f'{hour}:{min} {daytime}, {day}'
            j+=1
                        
                    
    else:
        if n > 0:
            if n ==1:
                new_time = f'{hour}:{min} {daytime} (next day)'
            else:
                new_time = f'{hour}:{min} {daytime} ({n} days later)'
        else:
            new_time =f'{hour}:{min} {daytime}'
    
    
    return new_time

def convert_time(parts):
    time=parts.split(':')
    time[0]= int(time[0])*60
    time[1]= int(time[1])
    return time[0]+time[1] # time in mins

