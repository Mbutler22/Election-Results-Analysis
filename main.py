#Modules

import os
import csv

#Set path for file
csvpath =os.path.join("PyBank", "budget_data.csv")

#Set the output of the text file
text_path = 'output.txt'

#Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase =["", 0]
revenue_change_list =[]
revenue_average = 0 

#Open  the CSV
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Get values of row one and skip, since there is no change in this row
    row_one = next(csvreader)
    total_months = total_months + 1
    total_revenue = total_revenue + int(row_one[1])
    previous_revenue = int(row_one[1])
    
    #Loop through change rows
    for row in csvreader:
            #Count the total number of months
            total_months = total_months + 1
            #Calculate the total revenue over the entire period
            total_revenue = total_revenue + int(row[1])
            #Calculate the average change in revenue between months over entire period
            revenue_change = int(row[1])- previous_revenue
            previous_revenue = int(row[1])
            revenue_change_list = revenue_change_list + [revenue_change]
            month_of_change = month_of_change +[row[0]]

            #The greatest increase in revenue (date and amount) over entire period
            if revenue_change>greatest_increase[1]:
                greatest_increase[1]= revenue_change
                greatest_increase[0] = row[0]

            #The greatest decrease in revenue (date and amount) over entire period
            if revenue_change<greatest_decrease[1]:              
                greatest_decrease[1]= revenue_change
                greatest_decrease[0] = row[0]

#The average revenue change over the entire period
revenue_average = sum(revenue_change_list)/len(revenue_change_list)

#Print out to git bash
print("Financial Analysis\n")
print("-------------------\n")
print("Total Months: %d\n" % total_months)
print("Total Revenue: $%d\n" % total_revenue)
print("Average Change $%.2f\n" % revenue_average)
print("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
print("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))

#Write changes to csv
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Change $%.2f\n" % revenue_average)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))

