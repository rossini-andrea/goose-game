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


from contextlib import suppress

if __name__ == "__main__":
    with suppress(BrokenPipeError):
        print('add player Foo')
        print('add player Bar')

        print('move Foo 3, 3')
        print('move Bar')
        print('move Foo 2, 5')
        print('move Bar')
        print('move Foo 2, 2')
        print('move Bar')

        while True:
            print('move Foo')
            print('move Bar')
