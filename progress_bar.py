#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time

from progressbar import ProgressBar, Bar, BouncingBar, Counter, ETA, Percentage, Timer


counter_total=500
widgets=['Loading ..', Bar(), Counter(), '/{} |'.format(counter_total), Percentage(), ' |', Timer(), ' |', ETA()]
pbar = ProgressBar(widgets=widgets, maxval=counter_total)
for x in pbar(xrange(counter_total)): time.sleep(0.02)


pbar.start()
for x in xrange(counter_total):
        pbar.update(x)
        time.sleep(0.02)
