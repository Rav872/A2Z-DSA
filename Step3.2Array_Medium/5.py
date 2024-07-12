# Stock buy and sell

#inputPrices = [7,1,5,3,6,4]
inputPrices = [7,6,4,3,1]

maxProfit = 0
buyPrice = inputPrices[0]

for price in range(len(inputPrices)):
    if inputPrices[price] < buyPrice:
        buyPrice = inputPrices[price]
    maxProfit = max(maxProfit, inputPrices[price] -  buyPrice)

print("Maximum profit is : ", maxProfit)