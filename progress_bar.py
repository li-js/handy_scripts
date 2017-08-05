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

        
# yet another way of doing it        
from tqdm import tqdm
for _ in tqdm(xrange(counter_total), total=counter_total):
        time.sleep(0.02)
