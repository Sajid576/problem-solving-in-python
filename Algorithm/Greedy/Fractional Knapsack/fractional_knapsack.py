

def maxProfit(items, capacity):
    for item in items:
        item.append(item[0]/item[1])

    # Sort items in descending order according to ratio(profit/value)
    items.sort(key=lambda x: x[2], reverse=True)
    print(items)

    max_profit = 0
    fractions = [0]*len(items)
    for i in range(len(items)):
        if(items[i][1] <= capacity):
            fractions[i] = 1
            max_profit += items[i][0]
            capacity -= items[i][1]
        else:
            fractions[i] = capacity/items[i][1]
            max_profit += items[i][0]*(capacity/items[i][1])
            break

    return max_profit, fractions


# Driver code
# (profit,weight)
items = [[45, 20], [36, 10], [17, 40], [28, 15], [19, 30]]
capacity = 100
print(maxProfit(items, capacity))
