# This is Python Programming for AI

# Assignment 3
#Jodabeni Dondeli
import csv
nba = open('nba.txt', 'r') #open and read the nba.txt file
Wins = open('Wins.csv','w') #opens wins.csv, if doesnt exist it writes it.
# #Create a dictionary where the key is the team, and the
# # value is the number of wins.
team_dictionary = {}  # assigning an empty dictionary to variable teams_dictionary

with nba as file:  # contents of nba.txt
    read_nba = csv.reader(file, delimiter ="\t")
    for row in read_nba:
        team1 = row[0] # First row that shows VisitorTeam
        score1 = row[1] #VisitorPTS
        team2 = row[2] #HomeTeam
        score2 = row[3] #HomePTS

        if score1.isdigit() and score2.isdigit(): # confirm both are numbers to use "int"
            if int(score1) > int(score2):
                if team1 in team_dictionary:
                    team_dictionary[team1] += 1 #adds a win
                else:
                    team_dictionary[team1] = 1
            else:
                if team2 in team_dictionary:
                    team_dictionary[team2] += 1
                else:
                    team_dictionary[team2] = 1


with Wins as output :
    for key , value in team_dictionary.items(): #iterate key represents the team name, and value = number of wins.
        print(key, value)
        output.writelines(str(key) + ',' + str(value) + '\n')

