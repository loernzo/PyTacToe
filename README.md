# PyTacToe
Simple CLI multiplayer tictactoe game made in Python.

# How to run?
You probably already know, simply run the script in a shell. You can also use `import pytactoe` in a Python session.

# What is this game?
In case you didn't understand, it's that famous silly little game you used to play with your deskmate when you were desperately bored at school. Yes, the one with crosses and circles

# How does it work?
Marks are stored in 2 matrixes, one for each player. The sub-lists represent a line, so the y coordinates, and the numbers inside them represent the columns, so the x coordinates. The script will automatically recognize and try to fix eventual user input errors

There are four ways to win in tictactoe:
### Horizontal tris
When you manage to do this tris, it means you placed 3 marks in a given line. So 3 x coordinates in a given y coordinate. That  also means the lenght of a given sub-list equals 3.

```python
for i in range(3):
       if len(coordinates[i])==3:
           return winner
       ...
```

### Vertical tris
This is the exact opposite: there are 3 marks in a given column. That means a certain number appears in all the three sub-lists. 

```python
for i in range(3):
       ...
       if i in coordinates[0] and i in coordinates[1] and i in coordinates[2]:
           return winner
       ...
```

### Top-left to bottom-right diagonal tris
When this occurs, it means that 3 coordinates couples have the same value(1-1, 2-2, 3-3)

```python
for i in range(3):
       ...
       if i in coordinates[0] and i in coordinates[1] and i in coordinates[2]:
           return winner
       ...
```

### Top-right to bottom-left diagonal tris
Finally, this tris means that the sum between a given coordinates couple equals 4 for 3 times

```python
for i in range(3):
       ...
       for n in coordinates[i]:
           if n+i+1==4:
               count+=1
           if count==3:
               return winner
       ...
```


# Why would I ever want to play this game?
Because Fun™


# Ok, but why wouldn't I just grab a piece of paper?
I know you know.
