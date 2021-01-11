#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 08:30:41 2021

@author: en-cheng chang
"""

# ========================================================================== #
#                                                                            #
#                                                                            #
# ========================================================================== #

from train_q_table import train_q_table
from create_instances import create_dist_matrix
from visualisation import visualise
from conf import conf as cf
import matplotlib.pyplot as plt
import numpy as np

# ========================================================================== #
#                                                                            #
#                                                                            #
# ========================================================================== #

def find_tsp_route(dots_map):

    q_table, route, distance, log = train_q_table(dots_map)

    return q_table, route, distance, log
    
    
    
dots_map = create_dist_matrix(cf.NUM_LOCATION, cf.DISTRIBUTION, cf.SEED)
q_table, route, distance, log = find_tsp_route(dots_map)

draw_log = []
for k in log:
    x = (np.array([dots_map[i][0] for i in k][0:-1]) - np.array([dots_map[i][0] for i in k][1:] ))**2
    y = (np.array([dots_map[i][1] for i in k][0:-1]) - np.array([dots_map[i][1] for i in k][1:] ))**2
    z = np.sqrt(x+y)
    draw_log.append(sum(z))
    #visualise(dots_map, i)

    
plt.plot(draw_log)
plt.show()



visualise(dots_map, log[-1])





