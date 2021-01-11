#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 08:34:24 2021

@author: en-cheng chang
"""

# ========================================================================== #
#                                                                            #
#                                                                            #
# ========================================================================== #

import numpy as np

# ========================================================================== #
#                                                                            #
#                                                                            #
# ========================================================================== #

def create_dist_matrix(num_location, distribution, seed):
    
    assert distribution in ['normal', 'uniform', 'chi'], "distribution should be normal', 'uniform', 'chi'"
    
    set_coordinate = []
    np.random.seed(seed)
    
    if distribution == 'normal':
        for _ in range(num_location):
            coordinate_x = np.random.normal(loc = 50, scale = 10)
            coordinate_y = np.random.normal(loc = 50, scale = 10)
            set_coordinate.append((coordinate_x, coordinate_y))
    elif distribution == 'uniform':
        for _ in range(num_location):
            coordinate_x = int(np.random.rand() * 100)
            coordinate_y = int(np.random.rand() * 100)
            set_coordinate.append((coordinate_x, coordinate_y))        
    elif distribution == 'chi':
        for _ in range(num_location):
            coordinate_x = np.random.chisquare(30,70)
            coordinate_y = np.random.chisquare(30,70)
            set_coordinate.append((coordinate_x, coordinate_y))        
    
    return set_coordinate
    


