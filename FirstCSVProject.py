import pandas as pd
import statistics

data = pd.read_csv("sample_sales_data_v2.csv")
print(f'Total revenue: {sum(data["revenue"])}')
print(f'Average order value: {round(statistics.mean(data["revenue"]), 2)}')
print(f'Most popular item: {statistics.mode(data["product"])}')

productTotals = {}

for i in range(len(data)):
    product = data["product"][i]
    quantity = int(data["quantity"][i])

    if product in productTotals:
        productTotals[product] += quantity
    else:
        productTotals[product] = quantity

sortedTotals = sorted(productTotals.items(), key=lambda x: x[1], reverse=True)
print(f'Quantity of each item: {sortedTotals}')

revenueTotals = {}

for i in range(len(data)):
    product = data["product"][i]
    revenue = float(data["revenue"][i])

    if product in revenueTotals:
        revenueTotals[product] += revenue
    else:
        revenueTotals[product] = revenue

sortedRevenue = sorted(revenueTotals.items(), key=lambda x: x[1], reverse=True)
roundedRevenue = {k: round(v, 2) for k, v in sortedRevenue}
print(f'Revenue by item: {roundedRevenue}')