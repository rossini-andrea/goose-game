# The Goose Game

This game was produced as an entry to the contest
**The Goose Game Kata** by [Matteo Vaccari](https://github.com/xpmatteo).

## How to install

Clone this project or download `goose-game.py`.

Additional requirements:

* Python 3

## How to run

Enter the directory where you downloaded `goose-game.py` and run it.

### On Linux

At the command line, type:

```sh
cd goose-game
./goose-game.py
```

Alternatively, run the explicit python interpreter:

```sh
cd goose-game
python goose-game.py
```

### On Windows

```bat
cd goose-game
python goose-game.py
```

Alternatively, the standard Python installer already associates the .py
extension with a file type (Python.File) and gives that file type an
open command that runs the interpreter
(`C:\Program Files\Python\python.exe "%1" %*`). This is enough to make
scripts executable from the command prompt as `goose-game.py`. If you'd
rather be able to execute the script by simple typing `goose-game` with
no extension you need to add .py to the `PATHEXT` environment variable.

## How to play

After launching the game you will interact with a command line.

### Add a player

The `add player` command receives a new player name, and adds it tho the
game. You can add an unlimited number of players!

```
add player John Doe
players: John Doe
add player Rob Smith
players: Rob Smith, John Doe
```

### Play your turn

You can roll a 2d6 and input the result in the game with the main
flavour of the `move` command.

```
move John Doe 4, 5
John Doe rolls 4, 5. John Doe moves from Start to 9, The Goose. John Doe
 moves again and goes to 18, The Goose. John Doe moves again and goes to
 27, The Goose. John Doe moves again and goes to 36
```

You can even let the computer roll for you.

```
move Rob Smith
Rob Smith rolls 1, 6. Rob Smith moves from Start to 7
```

### Getting Help

At the command line, type the `help` command.

```
help

Documented commands (type help <topic>):
========================================
EOF  add  exit  help  move
```

## License

Where not otherwise expressed, everything in this project is released
under the [GNU General Public License version 3](https://www.gnu.org/licenses/gpl-3.0.en.html).
