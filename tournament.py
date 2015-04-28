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
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their total match points,
    sorted by match points. If there is a tie, ties are broken by
    opponents' match points.

    Returns:
      A list of tuples, each of which contains
      (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of match the player has won
        matches: the number of matches the player has played
        opponentMatchPoints: match points of opponents, used for tiebreakers
    """

    DB = connect()
    c = DB.cursor()
    c.execute("SELECT playerID, name, wins, matches FROM players ORDER BY wins DESC")
    standings = c.fetchall()
    DB.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id of the winner of the match
      loser:  the id of the loser of the match
    """

    """First update the matches table"""
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO matches VALUES (" + str(winner) + ", " + str(loser) + ")")
    DB.commit()
    
    """Then update the players table"""
    c.execute("SELECT matches FROM players WHERE playerID = " + str(winner))
    m = c.fetchone()[0]
    c.execute("UPDATE players SET matches = " + str(m+1) + " WHERE playerID = " + str(winner))
    
    c.execute("SELECT matches FROM players WHERE playerID = " + str(loser))
    m = c.fetchone()[0]
    c.execute("UPDATE players SET matches = " + str(m+1) + " WHERE playerID = " + str(loser))

    c.execute("SELECT wins FROM players WHERE playerID = " + str(winner))
    m = c.fetchone()[0]
    c.execute("UPDATE players wins SET wins = " + str(m+1) + " WHERE playerID = " + str(winner))

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
    for x in range (0, pairs):
        pairings.append((standings[2*x][0], standings[2*x][1], standings[2*x+1][0], standings[2*x+1][1]))

    return pairings

