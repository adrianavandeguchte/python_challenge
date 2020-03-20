# PyPoll main sript

# import dependencies
import os
import csv

# path to csv resource file
csvpath = os.path.join("Resources","election_data.csv")

# starts vote count for the 4 candidates at zero, setting them as variables
khan=0
correy=0
li=0
otooley=0

# opens the resource file and sets to read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader, None)

    # loops through all the rows in the reader
    for row in csvreader:
        # adds a tally to each canididate if they appear as vote choice
        if row[2]=="Khan":
            khan+=1
        elif row[2]=="Correy":
            correy+=1
        elif row[2]=="Li":
            li+=1
        else:
            otooley+=1

# sets a dictionary with the canididates as keys and their vote count as values
votedict = {"Khan":khan,"Correy":correy,"Li":li, "O'Tooley":otooley}
# uses the dictionary to assign the winning candidate based on max vote count
winner = max(votedict,key=votedict.get)
# sums all candidate vote counts to find the total number of votes
total = khan+correy+li+otooley

# prints results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")
# for candidate vote total and percentage the print statement includes calculations to round values
print(f"Khan: {round(100*(khan/total),3)}% ({khan})")
print(f"Correy: {round(100*(correy/total),3)}% ({correy})")
print(f"Li: {round(100*(li/total),3)}% ({li})")
print(f"O'Tooley: {round(100*(otooley/total),3)}% ({otooley})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# reports out to text file
output = "election_results.txt"
# open and write to ouput text file
with open(output,"w",newline="") as text_file:
    # prints report into opened text file
    print("Election Results",file=text_file)
    print(f"Total Votes: {total}",file=text_file)
    print(f"Khan: {round(100*(khan/total),3)}% ({khan})",file=text_file)
    print(f"Correy: {round(100*(correy/total),3)}% ({correy})",file=text_file)
    print(f"Li: {round(100*(li/total),3)}% ({li})",file=text_file)
    print(f"O'Tooley: {round(100*(otooley/total),3)}% ({otooley})",file=text_file)
    print(f"Winner: {winner}",file=text_file)
