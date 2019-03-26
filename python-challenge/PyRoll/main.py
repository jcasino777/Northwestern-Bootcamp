import pandas as pd

#import data from direct path, read into dataframe
path = '/Users/jcasino/Documents/Courses/NUCHI201902DATA3/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv'
electiondata = pd.read_csv(path)

#get total number of votes
count = len(electiondata['Voter ID'])

#get unique candidates, store in list
candidates = electiondata['Candidate'].unique()

#create new dataframe with Candidate as Index, and total Votes as column
#use groupby.count() to get total votes by candidate
#rename column from Voter ID to Votes
votes_df = electiondata.groupby(['Candidate']).count()[['Voter ID']]
votes_df = votes_df.rename(columns={'Voter ID':"Votes"})

#add new column to dataframe, with percent of votes e/a candidate recieved
votes_df['Percent']= votes_df["Votes"] / count

#find winner based on who recieved the maximun number of votes
winner = votes_df["Percent"].idxmax()

#variables for print statement below
#format percent
K_pct = "{0:.0%}".format(votes_df.loc['Khan','Percent'])
C_pct = "{0:.0%}".format(votes_df.loc['Correy','Percent'])
L_pct = "{0:.0%}".format(votes_df.loc['Li','Percent'])
O_pct = "{0:.0%}".format(votes_df.loc["O'Tooley",'Percent'])
K_tot = votes_df.loc['Khan','Votes']
C_tot = votes_df.loc['Correy','Votes']
L_tot = votes_df.loc['Li','Votes']
O_tot = votes_df.loc["O'Tooley",'Votes']

#print results
print('')
print('Election Results')
print('-------------------------')
print(f'Total Votes: {count}')
print('-------------------------')
print(f'Khan: {K_pct} ({K_tot})')
print(f'Khan: {C_pct} ({C_tot})')
print(f'Khan: {L_pct} ({L_tot})')
print(f'Khan: {O_pct} ({O_tot})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

with open("Output.txt", "w") as text_file:
    print('Election Results', file=text_file)
    print('-------------------------', file=text_file)
    print(f'Total Votes: {count}', file=text_file)
    print('-------------------------', file=text_file)
    print(f'Khan: {K_pct} ({K_tot})', file=text_file)
    print(f'Khan: {C_pct} ({C_tot})', file=text_file)
    print(f'Khan: {L_pct} ({L_tot})', file=text_file)
    print(f'Khan: {O_pct} ({O_tot})', file=text_file)
    print('-------------------------', file=text_file)
    print(f'Winner: {winner}', file=text_file)
    print('-------------------------', file=text_file)