# We can import players.py [players.py and test.py must be same folder]

import players
 
# Let's make some people

soldier1 = app.Soldier("John", "Sniper")
worker1 = app.Worker("Garry", "Smith")
monk1 = app.Monk("Sebastian", "Helper")

# Ass you see we designated diffrent health values thanks to super() method

print(soldier1.health)
print(worker1.health)
print(monk1.health)
