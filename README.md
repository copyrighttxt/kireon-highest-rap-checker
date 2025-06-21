# Kireon.xyz RAP Checker
Python script that searches all users RAP on Kireon sends it to a discord webhook and pings you.


# Hows it work?
It requests a Kireon API, checks all User IDS, finds inventory_rap, and tells you the value, also pinging you when it finds the new highest RAP.
For example, since @ROBLOX is the first user, and has some RAP, it'll ping you when it finds that RAP.
Each time it finds a RAP bigger than the previous "Highest" RAP, it'll alert you.

https://www.kireon.xyz/public-api/v1/users/
