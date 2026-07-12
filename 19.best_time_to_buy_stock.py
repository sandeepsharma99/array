def maxProfit(array) :
    min_price = float("inf")
    max_profit = 0

    for p in range(len(array)) :
        min_price = min(p,min_price)
        profit = p-min_price
        max_profit = max(profit,max_profit)
    
    return max_profit

array = [7,1,5,3,6,4]
print(maxProfit(array))