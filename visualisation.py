#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:56:33 2021

@author: en-cheng chang
"""

# ========================================================================== #
#                                                                            #
#                                                                            #
# ========================================================================== #

import matplotlib.pyplot as plt

# ========================================================================== #
#                                                                            #
#                                                                            #
# ========================================================================== #

def visualise(dots_map, route):
    plt.plot([dots_map[i][0] for i in route], [dots_map[i][1] for i in route], 'o', color = 'black')
    plt.plot([dots_map[i][0] for i in route], [dots_map[i][1] for i in route], '-', color = 'red', alpha = 0.4)
    plt.show()