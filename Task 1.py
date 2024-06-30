from datetime import datetime

def get_days_from_today(date): 
        try:
                give_date = datetime.strptime(date, '%Y-%m-%d').date()    # Change to datetime
                today = datetime.today().date()       #todays date
                delta = today - give_date            #Calc days bewteen dates
                return delta.days
        except ValueError:
                return 'Invalid date format. Please use YYYY-MM-DD.'

date = input('Enter the date:')
days_from_today = get_days_from_today(date)

print(f'From {date} till now is {days_from_today} days')