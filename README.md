# Project-2
Full Stack Nanodegree Project 2
This project contains the files tournament.sql, tournament.py and tournament_test.py
This project is used to run a swiss-style tournament where players are paired against other players with identical or as close to identical records as possible.
After each round of the tournament the standings are updated with the results of the previous round of matches and new pairings are produced.

tournament.sql contains the SQL database structure for the project
It creates a players table that contains a playerID for each player and each player's name
IT creates a matches table that stores the results of each match, with the playerID of the winner listed first and the playerID of the loser listed second
Running the two create table commands in a postgresql database create the tables that can be manipulated using the tournament.py Python module

tournament.py contains the Python code for the project
It contains functions that access and update the tables in the tournament database created by tournament.sql

tournament_test.py contains Python code to test the tournament.py code by running each function in tournament.py with sample data. Tournament_test.py can be run after creating the tables with the commands in tournament.sql

This project operates on a virtual machine run by VirtualBox available at https://www.virtualbox.org/wiki/Downloads.
The virtual machine communicates with a host computer using Vagrant available at https://www.vagrantup.com/downloads.
With those two pieces of software installed, a GitBash terminal should be started and the command 'vagrant up' entered in order to launch the virtual machine.
Once the virtual machine is running, 'vagrant ssh' is entered into the terminal to log in to the virtual machine.
Next, the user should change the directory in the terminal to the directory where the files in this project are stored.
Then, the commands in the tournament.sql file should be run by entering '\i tournament.sql' into the terminal.
Lastly, the tournament_test.py file can be run by entering 'python tournament_test.py'.
