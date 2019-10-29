#!/usr/bin/python
import time
import argparse

start_time = time.time()

def find_max_profit(prices):
  buy = prices[0]
  sell = 0

  for price in prices[1:]:
        

  max_profit = buy - sell
return max_profit


Day1 = [10, 7, 5, 8, 11, 9] # / 6
Day2 = [100, 90, 80, 50, 20, 10] # / 10
find_max_profit(Day1)
find_max_profit(Day2)

# * Prints execution time to console
print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))