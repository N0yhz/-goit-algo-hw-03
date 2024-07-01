# -goit-algo-hw-03

Домашнє завдання до модулю 3.

1) Calc.date

```
from datetime import datetime

def get_days_from_today(date): 
        try:
                give_date = datetime.strptime(date, '%Y-%m-%d').date()           # Change to datetime
                today = datetime.today().date()                                  #todays date
                delta = today - give_date                                        #Calc days bewteen dates
                return delta.days
        except ValueError:
                return 'Invalid date format. Please use YYYY-MM-DD.'

date = input('Enter the date in the format "YYYY-MM-DD":')
days_from_today = get_days_from_today(date)

print(f'From {date} till now is {days_from_today} days')

```


2) Random numbers

```
import random

def get_numbers_ticket(min, max, quantity):
    
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min+ 1):      # check the validality of input data
        return []
    
    numbers = set()                                                             # generation unique random numbers
    while len(numbers) < quantity:
        numbers.add(random.randint(min,max))

    sorted_numbers = sorted(numbers)                                            # converting a set to a sorted list
    return sorted_numbers

#examples 

min_value = 1
max_value = 50
quantity = 6
lottery_numbers = get_numbers_ticket(min_value, max_value, quantity)

print(f'Loterry ticket numbers: {lottery_numbers}')

```