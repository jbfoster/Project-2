--The players table keeps track of each player in the tournament

--playerID is a unique ID for each player

--name is the name of a player


CREATE TABLE players	(playerID SERIAL NOT NULL PRIMARY KEY, name TEXT);

-- The matches table keeps track of all the matches played in the tournament

-- winnerid is the playerID of the winning player

--loserID is the playerID of the losing player

--winnerID and loserID are foreign keys referencing playerID in players table

CREATE TABLE matches	(winnerID INT REFERENCES players(playerID),
			loserID INT REFERENCES players(playerID),
			PRIMARY KEY (winnerID, loserID));
