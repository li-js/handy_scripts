#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time

from progressbar import ProgressBar, Bar, BouncingBar, Counter, ETA, Percentage, Timer

def example():
    total=500
    widgets=['Current: ', Counter(), '/{} |'.format(total), Percentage(), ' |', Timer(), ' |', ETA(), ' |', Bar()]
    pbar = ProgressBar(widgets=widgets, maxval=total)
    for x in pbar(range(total)): time.sleep(0.02)

        
if __name__ == '__main__':
    example()
