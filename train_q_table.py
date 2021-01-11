#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 09:05:20 2021

@author: en-cheng chang
"""

# ========================================================================== #
#                                                                            #
#                                                                            #
# ========================================================================== #

from conf import conf as cf
from tqdm import tqdm
import numpy as np
import random

# ========================================================================== #
#                                                                            #
#                                                                            #
# ========================================================================== #

def get_action_set(state): 
    return list(set(range(cf.NUM_LOCATION)).difference(set(state)))

def get_best_action(q_table, state):
    index_val = -float('inf'); index = 0; index_tmp = 0
    for val in q_table[state[-1]]:
        if index_tmp not in state:
            if val > index_val: 
                index_val = val
                index = index_tmp
        index_tmp += 1
    return index

def get_action(q_table, action_set, state, epsilon):
    
    if np.random.rand() < epsilon: 
        while True:
            action = random.choice(action_set)
            if action not in state: 
                return random.choice(action_set)
    else: return get_best_action(q_table, state)

def update_qtable(q_table, state, action, reward = 0):
    delayed_reward = q_table[action,:].max()
    q_table[state[-1],action] += cf.LR * (reward + cf.ALPHA * (delayed_reward - q_table[state[-1],action]))
    return q_table

def get_distance(set_coordinate, state, action):
    pos1 = set_coordinate[state[-1]] 
    pos2 = set_coordinate[action] 
    return np.sqrt(sum((np.array(pos1) - np.array(pos2))**2))

def train_q_table(set_coordinate):
    
    q_table = np.random.rand(cf.NUM_LOCATION, cf.NUM_LOCATION)
    init_obj = float('inf')
    epsilon = 1
    log = []
    
    for _ in tqdm(range(cf.TRAIN_ITER)):
        init_index = np.random.randint(cf.NUM_LOCATION)
        state = [init_index] # start point 
        action_set = get_action_set(state)
        route_distance = 0
        
        while action_set: # if action_set != [], seeking the next action
            action = get_action(q_table, action_set, state, epsilon)
            route_tmp = get_distance(set_coordinate, state, action)
            route_distance += route_tmp
            q_table = update_qtable(q_table, state, action, reward = 1/route_tmp)    
            state.append(action)
            action_set = get_action_set(state)
            
        route_tmp = get_distance(set_coordinate, state, init_index)
        route_distance += route_tmp
        
        if route_distance <= init_obj:
            q_table = update_qtable(q_table, state, init_index, reward = 1/route_tmp)
            init_obj = route_distance
        else:
            q_table = update_qtable(q_table, state, init_index, reward = 1/route_tmp)
        
            
        if epsilon > 0.05: epsilon *= cf.EPSILON 
        if _ >= cf.TRAIN_ITER - 2:  epsilon = 0
        if _ % 200 == 0: log.append(state + [init_index])
        
        _ +=1
        
    return q_table, state + [init_index], route_distance, log
            