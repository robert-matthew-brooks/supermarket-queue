import random
from queue_time import queue_time

class colours:
  GREY = '\033[90m'
  END = '\033[0m'

def convert_to_int(x):
  return int(x)

while 1:
  try:
    customers = input('Customer waiting times ' + colours.GREY + '(eg. "2 6 9", leave blank for random)' + colours.END + ':')
    if len(customers) == 0:
      customers = [0] * random.randint(8, 12)
      for i in range(len(customers)):
        customers[i] = random.randint(5, 9)
    else:
      customers = customers.split()
      customers = list(map(convert_to_int, customers))
    break
  except:
    print('invalid input...')

while 1:
  try:
    number_of_tills = input('Number of tills ' + colours.GREY + '(leave blank for random)' + colours.END + ':')
    if len(number_of_tills) == 0:
      number_of_tills = random.randint(3, 5)
    else:
      number_of_tills = int(number_of_tills)
    break
  except:
    print(number_of_tills, 'invalid input...')

queue_time(customers, number_of_tills)


