#! /usr/bin/python3
# -*- coding: utf-8 -*-
from time import sleep
import lcdlib

# ADDRESS = 0x3f
ADDRESS = 0x27

dimon = lcdlib.lcd(ADDRESS, 2, 16)
#              012345678912345
dimon.ruprintchar("Привет")
