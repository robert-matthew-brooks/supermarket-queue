# Supermarket Queue

https://replit.com/@robertmatthewbr/supermarket-queue

## Kata

You are a middle manager in a large supermarket chain, tasked with overseeing the checkout queue.

Every once in a while, your boss radios you to ask how long the current queues will take to process. You take this job seriously, so you've decided to write a function called `queueTime` to solve the problem.

The function takes two arguments:

- **customers**: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
- **checkouts**: a positive integer, the number of checkout tills.
  The function should return the time required to process all the customers.

<br />

- There is only ONE queue.
- The order of the queue NEVER changes.
- Assume that the front person in the queue (i.e. the first element in the array) proceeds to a till as soon as it becomes free.

## Installation

This projects requires `Python 3` - check on the CLI with `python3 --version`. After cloning the project:

- To run the script: `python3 main.py` (or press '>Run' on replit.com)
- To run the test suite: `python3 test_queue_time.py`
