def _knapSack(W, weight, value, n):
	if n == 0 or W == 0:
		return 0
	if(weight[n-1] > W):
		return _knapSack(W, weight, value, n-1)
	else:
		return max(value[n-1] + _knapSack(W-weight[n-1], weight, value, n-1),
			       _knapSack(W, weight, value, n-1))

def KnapSack(maxWeight, weights, values):
	return _knapSack(maxWeight, weights, values, len(values))