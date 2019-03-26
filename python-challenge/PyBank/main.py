import csv
import os
import pandas as pd

#call direct filepath
path = '/Users/jcasino/Documents/Courses/NUCHI201902DATA3/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv'

#read in file as csv, setting Date as Index
budgetdata = pd.read_csv(path,index_col="Date")
budgetdata.head()

#The total number of months included in the dataset
months = len(budgetdata['Profit/Losses'])
months

#The net total amount of "Profit/Losses" over the entire period
pnl = budgetdata['Profit/Losses'].sum()
pnl

#The average of the changes in "Profit/Losses" over the entire period
avg = budgetdata['Profit/Losses'].mean()
avg

#The greatest increase in profits (date and amount) over the entire period
max = budgetdata['Profit/Losses'].max()
max_date = budgetdata['Profit/Losses'].idxmax()

#The greatest decrease in losses (date and amount) over the entire period
min = budgetdata['Profit/Losses'].min()
min_date = budgetdata['Profit/Losses'].idxmin()

print('')
print('Financial Analysis')
print('----------------------------')  
print(f'Total Months: {months}')
print(f'Total: {pnl}')
print(f'Average Change: {avg}')
print(f'Greatest Increase in Profits: {max_date} ({max})')
print(f'Greatest Decrease in Profits: {min_date} ({min})')
print('')

with open("Output.txt", "w") as text_file:
    print('Financial Analysis',file=text_file)
    print('----------------------------',file=text_file) 
    print(f'Total Months: {months}',file=text_file)
    print(f'Total: {pnl}',file=text_file)
    print(f'Average Change: {avg}',file=text_file)
    print(f'Greatest Increase in Profits: {max_date} ({max})',file=text_file)
    print(f'Greatest Decrease in Profits: {min_date} ({min})',file=text_file)
 

        