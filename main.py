import gymnasium as gym
import numpy as np
import random





states = (food_left, food_right, food_up, food_down)

alpha = 0.9
gamma = 0.95
epsilon = 1 #1 all random 0 no random actions
epsilon_decay = 0.9995
min_epsilon = 0.01
num_episodes = 10000
max_moves = 1000


q_table = np.zeros()