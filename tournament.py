#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT COUNT(*) FROM players")
    numPlayers = int(c.fetchone()[0])
    DB.close()
    return numPlayers


def registerPlayer(name):
    """Adds a player to the tournament database.

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their total number of matches won,
    sorted by matches won.

    Returns:
      A list of tuples, each of which contains
      (id, name, wins, losses):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    DB = connect()
    c = DB.cursor()
    """create a view listing the number of wins each player has"""
    c.execute("CREATE VIEW wins AS SELECT playerID, name, COUNT(WINNERID) as numWins \
              FROM players FULL JOIN matches on playerID=winnerID GROUP BY playerID")

    """create a view listing the number of losses each player has"""
    c.execute("CREATE VIEW losses AS SELECT playerID, COUNT(loserID) as numLosses \
              FROM players FULL JOIN matches on playerID=loserID GROUP BY playerID")

    """select the number of wins and matches played for each player from joining the two views"""
    c.execute("SELECT wins.playerID, name, numWins, numWins+numLosses \
              FROM wins FULL JOIN losses on wins.playerID=losses.playerID ORDER BY numWins DESC")

    standings = c.fetchall()
    DB.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id of the winner of the match
      loser:  the id of the loser of the match
    """

    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO matches (winnerID, loserID) VALUES (%s, %s)", (winner, loser))
    DB.commit()
    DB.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    standings = playerStandings()
    pairs = len(standings) / 2
    pairings = []
    for x in range(0, pairs):
        pairings.append((standings[2*x][0], standings[2*x][1], standings[2*x+1][0], standings[2*x+1][1]))

    return pairings

