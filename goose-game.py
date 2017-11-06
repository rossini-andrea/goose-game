#!/usr/bin/python
# -*- coding: utf-8 -*-


# Goose Game Kata
# Copyright (C) 2017 Rossini Andrea
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import cmd
import re
import sys
import random


class GooseGame:
    def __init__(self, view, random_state=None):
        self.players = {}
        self.cells = [str(i) for i in range(64)]
        self.cells[0] = 'Start'
        self.cells[6] = 'The Bridge'

        for i in [5, 9, 14, 18, 23, 27]:
            self.cells[i] = str(i) + ', The Goose'

        self.rnd = random.Random()
        self.rnd.seed(random_state)
        self.view = view

    def add_player(self, name):
        if name in self.players:
            return False

        self.players[name] = 0
        return True

    def move(self, player, dice_roll=None):
        self.view.new_turn(player)

        if dice_roll is None:
            d1, d2 = self.rnd.sample(range(1, 7), 2)
        else:
            d1, d2 = tuple(dice_roll)

        endgame = False
        self.view.roll(player, d1, d2)
        track = [self.players[player]]
        to = self.players[player] + d1 + d2
        trackname = lambda x: self.cells[track[x]]

        if to > 63:
            track += [63]
            to = 63 * 2 - to
            track += [to]
            self.view.move(player, trackname(-3), trackname(-2))
            self.view.bounce(player, trackname(-2), trackname(-1))
        else:
            track += [to]
            self.view.move(player, trackname(-2), trackname(-1))

        if 'Bridge' in self.cells[to]:
            to = 12
            track += [to]
            self.view.jump(player, trackname(-2), trackname(-1))

        while 'Goose' in self.cells[to]:
            to += d1 + d2
            track += [to]
            self.view.move_again(player, trackname(-2), trackname(-1))

        self.players[player] = to

        if to == 63:
            self.view.win(player)
            endgame = True

        self.view.end_turn(player)

        return endgame


class CliView:
    def __init__(self, destination=None):
        if destination is None:
            self.destination = sys.stdout
        else:
            self.destination = destination

    def new_turn(self, player):
        None

    def roll(self, player, d1, d2):
        print('{} rolls {}, {}'.format(player, d1, d2), end='', file=self.destination)

    def move(self, player, start, to):
        print('. {} moves from {} to {}'.format(player, start, to), end='', file=self.destination)

    def move_again(self, player, start, to):
        print('. {} moves again and goes to {}'.format(player, to), end='', file=self.destination)

    def bounce(self, player, start, to):
        print('. {0} bounces! {0} returns to {1}'.format(player, to), end='', file=self.destination)

    def jump(self, player, start, to):
        print('. {} jumps to {}'.format(player, to), end='', file=self.destination)

    def win(self, player):
        print('. {} Wins!!'.format(player), end='', file=self.destination)

    def show_message(self, message):
        print(message, file=self.destination)

    def end_turn(self, player):
        print(file=self.destination)


class GooseCmdLine(cmd.Cmd):
    prompt = ''

    def __init__(self, game, view):
        super(GooseCmdLine, self).__init__()
        self.game = game
        self.view = view

    def do_add(self, line):
        """Adds a new player, syntax: add player <Player Name>"""
        args = line.split(None, maxsplit=1)

        if args[0] == 'player':
            if not self.game.add_player(args[1]):
                self.view.show_message('{}: already existing player'.format(args[1]))
                return

            self.view.show_message('players: ' + ', '.join(self.game.players.keys()))
        else:
            self.view.show_message('Invalid command.')

    def do_move(self, line):
        """Moves player by a dice roll, if the roll is omitted, the game will roll for the player. Syntax: move
        <Player Name> [dice1, dice2] """

        player = max([x for x in self.game.players.keys() if line.startswith(x)],
                     key=len)
        throw = line[len(player):]
        match = re.fullmatch('\s+([1-6])\s*,\s*([1-6])\s*', throw)

        if match is not None:
            return self.game.move(player, [int(match.group(1)), int(match.group(2))])
        elif throw.isspace() or len(throw) == 0:
            return self.game.move(player)
        else:
            self.view.show_message('Invalid command.')
            return

    def do_exit(self, line):
        """Quits the game."""
        return True

    def do_EOF(self, line):
        """Send CTRL+D to instantly close the game."""
        return True

    def default(self, line):
        self.view.show_message('Invalid command.')


def main():
    view = CliView()
    GooseCmdLine(GooseGame(view), view).cmdloop()


if __name__ == "__main__":
    main()
