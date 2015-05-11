# Project-2
Full Stack Nanodegree Project 2
This project contains the files tournament.sql and tournament.py
This project is used to run a swiss-style tournament where players are paired against other players with identical or as close to identical records as possible.
After each round of the tournament the standings are updated with the results of the previous round of matches and new pairings are produced.

tournament.sql contains the SQL database structure for the project
It creates a players table that contains a playerID for each player and each player's name
IT creates a matches table that stores the results of each match, with the playerID of the winner listed first and the playerID of the loser listed second

tournament.py contains the Python code for the project
The function connect() connects to the tournament database
The function deleteMatches() deletes all matches from the matches database
The function deletePlayers deletes all players from the players database
The function countPlayers counts the number of players in the tournament
The function registerPlayer(name) registers a player for the tournament
The function playerStandings() returns the current standings for the tournament ordered by highest number of match wins
The function reportMatch(winner, loser) updates the matches table with a new match result
The function swissPairings() creates the pairings for the next round of the tournament
