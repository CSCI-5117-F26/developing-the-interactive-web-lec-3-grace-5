# from halo import Halo
# import time

# spinner = Halo(text='Loading', spinner='dots')
# spinner.start()

# # Run time consuming work here
# time.sleep(10)
# # You can also change properties for spinner as and when you want

# spinner.stop()
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from halo import Halo

spinner = Halo(text='Such Spins', text_color= 'cyan', color='green', spinner='dots')

try:
    spinner.start()
    spinner.text = 'Loading'
    spinner.spinner = 'hearts'
    while True:
        spinner.text_color = 'cyan'
        time.sleep(2)
        spinner.text_color = 'magenta'
        time.sleep(2)
    # spinner.stop_and_persist(symbol='🦄 '.encode('utf-8'), text='Wow!')
except (KeyboardInterrupt, SystemExit):
    spinner.stop()