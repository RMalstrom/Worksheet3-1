"""
Richard Malstrom
CMSC-1380

This program is my solution to the following problem:


There is an election with three candidates: Alpha, Bravo, Charlie.
Write a program to accept votes from an unknown number of voters.
Their input will consist of their candidate's name.
The attendent will enter "finish" when voting is complete.
So the input stream will look like the text below.
After the attendent enters "finish", the program should output
the number of votes each candidate received.

In some manner of your choosing, the program should indicate the winner.
This could be by sorting a list of the three candidates with vote totals,
or it could simply be an output of "the winner is Charlie with 8 votes".

Date Last Modified: 10.29.2024
"""
# Initialize and set votes to 0
alphaVoteCount = 0
bravoVoteCount = 0
charlieVoteCount = 0

# Declare exit variable for loop
exitVar = False

while not exitVar:
    userInput = input("Please enter your vote: ") # Take users input for vote

    # Assign votes to correct candidate or decline input if invalid
    if userInput.upper() == "ALPHA":
        print("Vote cast!")
        alphaVoteCount = alphaVoteCount + 1
    elif userInput.upper() == "BRAVO":
        print("Vote cast!")
        bravoVoteCount = bravoVoteCount + 1
    elif userInput.upper() == "CHARLIE":
        print("Vote cast!")
        charlieVoteCount = charlieVoteCount + 1
    elif userInput.upper() == "FINISH":
        print("Tallying votes...")
        exitVar = True
    else:
        print("Invalid input!")

# Tally votes and decide who has the most votes
if alphaVoteCount > bravoVoteCount and alphaVoteCount > charlieVoteCount:
    winner = "Alpha"
    winnerCount = alphaVoteCount
elif bravoVoteCount > alphaVoteCount and bravoVoteCount > charlieVoteCount:
    winner = "Bravo"
    winnerCount = bravoVoteCount
else:
    winner = "Charlie"
    winnerCount = charlieVoteCount

# Print out the full results and the winner explicitly
print(f"Alpha: {alphaVoteCount}, Bravo: {bravoVoteCount}, Charlie: {charlieVoteCount}")
print(f"Winner is {winner} with {winnerCount} votes!")



