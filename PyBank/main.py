#PyBank main script
# dependencies
import os
import csv

# path to csv resource file
csvpath = os.path.join("Resources","budget_data.csv")

# opens csv input and pulls data for analysis through list assignment
with open(csvpath) as csvfile:
    # establishes lists for csv data
    row1 = []
    row0 = []
    csvreader = csv.reader(csvfile,delimiter=",") # places the open readable csv into a variable
    header = next(csvreader) # skips header
    for row in csvreader:
        row1.append(int(row[1])) # adds each value for column 2 (profit/loss) to profit/loss(row1) list
        row0.append(row[0]) # adds each value for column 1 (months) to months(row0) list
    # terminal output
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {(len(row0))}") # total months printed via the length of the months list
    print(f"Total: ${(sum(row1))}") # net total printed via the sum of the profit/loss list
    change = [row1[i+1]-row1[i] for i in range(len(row1)-1)] # for loop to create list of differences between each month
    print(f"Average Change: ${(round((sum(change)/len(change)),2))}") # finds average profit/loss using sum and len of the profit/loss lists
    print(f"Greatest Increase in Profits: {(row0[(change.index(max(change)))+1])} (${(max(change))})") # greatest increase in change list printed along with month using change list max and th max index + 1 as the index in the month list
    print(f"Greatest Decrease in Profits: {(row0[(change.index(min(change)))+1])} (${(min(change))})") # same as above but for greatest decrease using the min value in place of max value

# output path
# all output files lines mirror the above terminal outputs
output = ("financial_analysis.txt")
# open and write to ouput text file
with open(output,"w",newline="") as text_file:
    # prints report into opened text file
    print("Financial Analysis",file=text_file) # report title
    print("----------------------------",file=text_file)
    print(f"Total Months: {(len(row0))}",file=text_file) # total months printed via the length of the months list
    print(f"Total: ${(sum(row1))}",file=text_file) # net total printed via the sum of the profit/loss list
    print(f"Average Change: ${(round((sum(change)/len(change)),2))}",file=text_file) # finds average profit/loss using sum and len of the profit/loss lists
    print(f"Greatest Increase in Profits: {(row0[(change.index(max(change)))+1])} (${(max(change))})",file=text_file) # greatest increase in change list printed along with month using change list max and th max index + 1 as the index in the month list
    print(f"Greatest Decrease in Profits: {(row0[(change.index(min(change)))+1])} (${(min(change))})",file=text_file) # same as above but for greatest decrease using the min value in place of max value
