--The players table keeps track of each player in the tournament

--playerID is a unique ID for each player

--name is the name of a player


CREATE TABLE players	(playerID SERIAL NOT NULL PRIMARY KEY, naame TEXT);

-- The matches table keeps track of all the matches played in the tournament

-- winnerid is the playerID of the winning player

--loserID is the playerID of the losing player

--winnerID and loserID are foreign keys referencing playerID in players table

CREATE TABLE matches	(winnerID INT REFERENCES players(playerID),
			loserID INT REFERENCES players(playerID),
			PRIMARY KEY (winnerID, loserID))
;

--create a view listing the number of wins each player has

CREATE VIEW wins AS SELECT playerID, name, COUNT(winnerID) as numWins
FROM players FULL JOIN matches on playerID=winnerID GROUP BY playerID;

--create a view listing the number of losses each player has

CREATE VIEW losses AS SELECT playerID, COUNT(loserID) as numLosses
FROM players FULL JOIN matches on playerID=loserID GROUP BY playerID;
