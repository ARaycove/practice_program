hours = input ('Please enter your hours for last pay period \n')
hourly_rate = input('Please enter your hourly rate \n')
try:
    hours = float(hours)
    hourly_rate = float(hourly_rate)
    if hours > 40:
        overtime_hours = 1.5 * (hours - 40)
        hours = 40
        total_hours = overtime_hours + hours
        print(total_hours * hourly_rate)
    else:
        print(hours * hourly_rate)
except: 
    print('Include only alphanumeric characters') 
    
