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
import random


class GooseGame(cmd.Cmd):
    prompt = ''
    players = {}
    cells = [str(i) for i in range(64)]
    cells[0] = 'Start'
    cells[6] = 'The Bridge'

    for i in [5, 9, 14, 18, 23, 27]:
        cells[i] = str(i) + ', The Goose'

    random.seed()

    def do_add(self, line):
        """Adds a new player, syntax: add player <Player Name>"""
        args = line.split(None, maxsplit=1)

        if args[0] == 'player':
            if args[1] in self.players:
                print('{}: already existing player'.format(args[1]))
                return

            self.players[args[1]] = 0
            print('players: ' + ', '.join(self.players.keys()))
        else:
            print('Invalid command.')

    def do_move(self, line):
        """Moves player by a dice roll, if the roll is omitted, the game will roll for the player. Syntax: move
        <Player Name> [dice1, dice2] """

        player = max([x for x in self.players.keys() if line.startswith(x)],
                     key=len)
        throw = line[len(player):]
        match = re.fullmatch('\s+([1-6])\s*,\s*([1-6])\s*', throw)

        if match is not None:
            d1 = int(match.group(1))
            d2 = int(match.group(2))
        elif throw.isspace() or len(throw) == 0:
            d1, d2 = random.sample(range(1, 7), 2)
        else:
            print('Invalid command.')
            return

        return self.move(player, d1, d2)

    def do_exit(self, line):
        """Quits the game."""
        return True

    def do_EOF(self, line):
        """Send CTRL+D to instantly close the game."""
        return True

    def default(self, line):
        print('Invalid command.')

    def move(self, player, d1, d2):
        endgame = False
        message = '{} rolls {}, {}'.format(player, d1, d2)
        track = [self.players[player]]
        to = self.players[player] + d1 + d2
        trackname = lambda x: self.cells[track[x]]

        if to > 63:
            track += [63]
            to = 63 * 2 - to
            track += [to]
            message += '. {0} moves from {1} to {2}. {0} bounces! {0} returns to {3}'\
                .format(player, trackname(-3), trackname(-2), trackname(-1))
        else:
            track += [to]
            message += '. {0} moves from {1} to {2}' \
                .format(player, trackname(-2), trackname(-1))

        if 'Bridge' in self.cells[to]:
            to = 12
            track += [to]
            message += '. {} jumps to {}'\
                .format(player, trackname(-1))

        while 'Goose' in self.cells[to]:
            to += d1 + d2
            track += [to]
            message += '. {} moves again and goes to {}'\
                .format(player, trackname(-1))

        self.players[player] = to

        if to == 63:
            message += '. {} Wins!!'.format(player)
            endgame = True

        print(message)

        return endgame


if __name__ == "__main__":
    GooseGame().cmdloop()
