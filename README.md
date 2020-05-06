# PyTacToe
>A simple CLI multiplayer tictactoe game made in Python.

## How to run?
You probably already know, simply run the script in a shell. You can also use `import pytactoe` in a Python session.

## What is this game?
In case you didn't understand, it's that famous silly little game you used to play with your deskmate when you were desperately bored at school. Yes, the one with crosses and circles

## How does it work?

There are four ways to win in tictactoe:
### Horizontal tris
When you manage to do this tris, it means you placed 3 marks in a given line. So 3 x coordinates in a given y coordinate. That  also means the lenght of a given sub-list equals 3.

```python
#Horizontal tris check
for y in range(3):
        if len(coordinates[y])==3:
            return winner
       ...
```

### Vertical tris

```python
#Vertical tris check
for y in range(3):
       ...
       if y in coordinates[0] and y in coordinates[1] and y in coordinates[2]:
           return winner
       ...
```

### Top-left to bottom-right diagonal tris
When this occurs, it means that 3 coordinates couples have the same value(1-1, 2-2, 3-3)

```python
#Top-left bottom-right tris check
for y in range(3):
      ...
       count_1+=1 if y+1 in coordinates[y] else 0
       if count_1==3:
           return winner
```

### Top-right to bottom-left diagonal tris
Finally, this tris means that the sum between a given coordinates couple equals 4 for 3 times

```python
#Top-right bottom-left tris check
for y in range(3):
       ...
       for n in coordinates[y]:
           count_2+=1 if n+y+1==4 else 0
           if count_2==3:
               return winner
       ...
```


## Why would I ever want to play this game?
Because Fun™


## Ok, but why wouldn't I just grab a piece of paper?
You know I know you know.
