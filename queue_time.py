import os

def queue_time(customers, number_of_tills):
  # inital setup
  elapsed_time = 0
  queue = customers.copy()
  tills = [0] * number_of_tills
  report(elapsed_time, queue, tills, 'initial setup...', True)

  # initial assign empty tills
  for i in range(number_of_tills):
    if len(queue):
      tills[i] = shift(queue)
      report(elapsed_time, queue, tills, 'customer moved to empty till...', True)

  # main loop
  while is_not_empty(tills) or len(queue) > 0:

    # move queueing customer to empty till
    if tills.count(0) > 0 and len(queue) > 0:
      empty_till = tills.index(0)
      tills[empty_till] = shift(queue)
      status = 'customer moved to empty till...'
    else:
      elapsed_time += 1
      for i in range(number_of_tills):
        if tills[i]:
          tills[i] -= 1
          status = 'time passed...'
    
    if (is_not_empty(tills) == False and len(queue) == 0):
      report(elapsed_time, queue, tills, f'type {colours.YELLOW}python3 main.py{colours.RED} to restart...', False)
      return elapsed_time
    
    report(elapsed_time, queue, tills, status, True)
  
##################
# util functions #
##################

def shift(array):
  array.reverse()
  el = array.pop()
  array.reverse()
  return el

def is_not_empty(array):
  return any(el > 0 for el in array)

##################################
#       reporting function       #
# for user feedback of algorithm #
##################################

class colours:
  GREY = '\033[90m'
  RED = '\033[31m'
  YELLOW = '\033[33m'
  GREEN = '\033[92m'
  END = '\033[0m'

def report(elapsed_time, queue, tills, status, isRunning):
  os.system('clear')

  print(f'Status: {colours.RED}{status}{colours.END}')
  print('')
  print('--------------------')
  print('')
  
  queueStr = 'Q) '
  if len(queue) == 0:
    queueStr += f'{colours.GREY}empty...{colours.END}'
  else:
    for customer in queue:
      queueStr += f'{colours.YELLOW}({str(customer)}) {colours.END}'

  print(queueStr)
  print('')

  for tillIndex in range(len(tills)):
    tillStr = f'{str(tillIndex+1)}] '

    if (tills[tillIndex]):
      tillStr += f'{colours.YELLOW}{tills[tillIndex] * chr(9608)} ({str(tills[tillIndex])}){colours.END}'
    else:
      tillStr += f'{colours.GREY}empty...{colours.END}'

    print(tillStr)

  print('')

  timeStr = 'T) '
  if (elapsed_time):
    timeStr += f'{colours.RED}{elapsed_time * chr(9608)} {str(elapsed_time)} min(s){colours.END}'
  else:
    timeStr += f'{colours.RED} 0 min(s){colours.END}'

  print(timeStr)
  print('')
  if isRunning:
    input(f'{colours.GREEN}(press Enter to continue...){colours.END}')