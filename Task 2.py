import random

def get_numbers_ticket(min, max, quantity):
    
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min+ 1):  # check the validality of input data
        return []
    
    numbers = set()                                                         # generation unique random numbers
    while len(numbers) < quantity:
        numbers.add(random.randint(min,max))

    sorted_numbers = sorted(numbers)                                        # converting a set to a sorted list
    return sorted_numbers

#examples 
min_value = 1
max_value = 50
quantity = 6
lottery_numbers = get_numbers_ticket(min_value, max_value, quantity)

print(f'Loterry ticket numbers: {lottery_numbers}')