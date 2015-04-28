-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players	(playerID SERIAL NOT NULL PRIMARY KEY,
			 name TEXT, wins INT DEFAULT 0, matches INT DEFAULT 0);

CREATE TABLE matches	(winnerID INT, loserID INT)

