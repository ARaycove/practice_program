hours = input ('Please enter your hours for last pay period \n')
hourly_rate = input('Please enter your hourly rate \n')
def calculate_overtime(hours, hourly_rate): 
    try:
        hours = float(hours)
        hourly_rate = float(hourly_rate)
        if hours > 40:
            overtime_hours = 1.5 * (hours - 40)
            hours = 40
            total_hours = overtime_hours + hours
            return total_hours
        else:
            total_hours = hours
            return total_hours
    except: 
        print('Include only integers')
        

pay = calculate_overtime(hours, hourly_rate) * hourly_rate #For brevity, we try the hourly_rate conditional inside the function iteself.
print(pay)