import random
from queue_time import queue_time

class colours:
  GREEN = '\033[92m'
  END = '\033[0m'

def cast_int(x):
  return int(x)

while 1:
  try:
    inputStr = input(f'{colours.GREEN}Press Enter to start...{colours.END}')
    if len(inputStr) == 0:
      customers = [0] * random.randint(8, 12)
      for i in range(len(customers)):
        customers[i] = random.randint(5, 9)
      number_of_tills = random.randint(3, 5)
    else:
      input_nums = list(map(cast_int, inputStr.split()))
      number_of_tills = input_nums.pop()
      customers = input_nums
    break
  except:
    print('invalid input...')

queue_time(customers, number_of_tills)


