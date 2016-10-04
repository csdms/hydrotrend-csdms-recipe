#! /usr/bin/env python
from __future__ import print_function

import os

os.mkdir('_testing')
os.chdir('_testing')

from pymt.components import Hydrotrend

ht = Hydrotrend()
for default in ht.defaults:
    print('{name}: {val} {units}'.format(
        name=default[0], val=default[1], units=val[2]))