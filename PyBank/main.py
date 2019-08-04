# Import modules
import os
import csv

# Create lists
months = []
profit = []
profit_change = []

# Read budget data CSV
csv_path = os.path.join('..','PyBank','budget_data.csv')
with open(csv_path,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)

    # Read through rows to get data and put them into lists
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])

# Analyze profit change data
greatest_increase = max(profit_change)
greatest_decrease = min(profit_change)
month_greatest_increase = profit_change.index(max(profit_change))+1
month_greatest_decrease = profit_change.index(min(profit_change))+1

# Print results
print("Financial Analysis")
print("------------------------")
print(f'Total Months: {len(months)}')
print(f'Total Profit(Loss): ${sum(profit)}')
print(f'Average Change: ${round(sum(profit_change)/len(profit_change),2)}')
print(f'Greatest Increase in Profits: {months[month_greatest_increase]} ${greatest_increase}')
print(f'Greatest Decrease in Profits: {months[month_greatest_decrease]} ${greatest_decrease}')

# Export results to text file
output_file = open("pybank_output.txt","w")
output_file.write("Financial Analysis")
output_file.write("\n")
output_file.write("-------------------")
output_file.write("\n")
output_file.write(f'Total Months: {len(months)}')
output_file.write("\n")
output_file.write(f'Total Profit(Loss): ${sum(profit)}')
output_file.write("\n")
output_file.write(f'Average Change: ${round(sum(profit_change)/len(profit_change),2)}')
output_file.write("\n")
output_file.write(f'Greatest Increase in Profits: {months[month_greatest_increase]} ${greatest_increase}')
output_file.write("\n")
output_file.write(f'Greatest Decrease in Profits: {months[month_greatest_decrease]} ${greatest_decrease}')
