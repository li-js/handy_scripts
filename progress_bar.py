#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time

from progressbar import ProgressBar, Bar, BouncingBar, Counter, ETA, Percentage, Timer, FileTransferSpeed


# one way of doing it
counter_total=500
widgets=['Loading ..', Bar(), Counter(), '/{} |'.format(counter_total), Percentage(), ' |', Timer(), ' |', ETA(), ' |', FileTransferSpeed()]
pbar = ProgressBar(widgets=widgets, maxval=counter_total)
for x in pbar(xrange(counter_total)): time.sleep(0.02)

# another way of doing it
pbar.start()
for x in xrange(counter_total):
        pbar.update(x)
        time.sleep(0.02)

        
# yet another way of doing it with minimal coding      
from tqdm import tqdm
for _ in tqdm(xrange(counter_total)):
        time.sleep(0.02)
        
        
# tqdm with dynamic information during the progress       
from tqdm import trange, tqdm
from random import random

pbar = tqdm(xrange(100), desc='Train epoch 1')
pbar = trange(100, desc='Train epoch 1')

for i in pbar:
    # pbar.set_description('Train on batch %i' % i)      # Description will be displayed on the left   
    # Postfix will be displayed on the right, and will format automatically based on argument's datatype
    pbar.set_postfix(loss='%0.3f'%random(), acc='%0.3f'%random(), loss2='%0.3f'%random())     
    time.sleep(0.1)        
pbar.close()
