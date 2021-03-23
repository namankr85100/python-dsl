# Python3 implementation of the approach

# Function to return the maximum profit
# that can be made after buying and
# selling the given stocks
def maxProfit(price, start, end):

	# If the stocks can't be bought
	if (end <= start):
		return 0;

	# Initialise the profit
	profit = 0;

	# The day at which the stock
	# must be bought
	for i in range(start, end, 1):

		# The day at which the
		# stock must be sold
		for j in range(i+1, end+1):

			# If byuing the stock at ith day and
			# selling it at jth day is profitable
			if (price[j] > price[i]):
				
				# Update the current profit
				curr_profit = price[j] - price[i] +\
							maxProfit(price, start, i - 1)+ \
							maxProfit(price, j + 1, end);

				# Update the maximum profit so far
				profit = max(profit, curr_profit);

	return profit;

# Driver code
if __name__ == '__main__':
	price = [100, 180, 260, 310, 40, 535, 695];
	n = len(price);

	print(maxProfit(price, 0, n - 1));

# This code is contributed by Rajput-Ji






# Python3 Program to find 
# best buying and selling days

# This function finds the buy sell
# schedule for maximum profit
def stockBuySell(price, n):
	
	# Prices must be given for at least two days
	if (n == 1):
		return
	
	# Traverse through given price array
	i = 0
	while (i < (n - 1)):
		
		# Find Local Minima
		# Note that the limit is (n-2) as we are
		# comparing present element to the next element
		while ((i < (n - 1)) and
				(price[i + 1] <= price[i])):
			i += 1
		
		# If we reached the end, break
		# as no further solution possible
		if (i == n - 1):
			break
		
		# Store the index of minima
		buy = i
		i += 1
		
		# Find Local Maxima
		# Note that the limit is (n-1) as we are
		# comparing to previous element
		while ((i < n) and (price[i] >= price[i - 1])):
			i += 1
			
		# Store the index of maxima
		sell = i - 1
		
		print("Buy on day: ",buy,"\t",
				"Sell on day: ",sell)
		
# Driver code

# Stock prices on consecutive days
price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)

# Fucntion call
stockBuySell(price, n)

# This is code contributed by SHUBHAMSINGH10



def maxProfit(prices):
	
	n = len(prices)
	cost = 0
	maxcost = 0

	if (n == 0):
		return 0

	# Store the first element of 
	# array in a variable
	min_price = prices[0]

	for i in range(n):
		
		# Now compare first element with all
		# the element of array and find the 
		# minimum element
		min_price = min(min_price, prices[i])

		# Since min_price is smallest element 
		# of the array so subtract with every
		# element of the array and return the
		# maxCost
		cost = prices[i] - min_price

		maxcost = max(maxcost, cost)

	return maxcost

# Driver Code
prices = [ 7, 1, 5, 3, 6, 4 ]

# Stock prices on consecutive days
print(maxProfit(prices))

# This code is contributed by avanitrachhadiya2155
