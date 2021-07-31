import numpy as np
import cv2
from Model import RecogJoint
import torch
from video_cap import videoCap

agent_env = [0, 1, 2]
options = ['rock', 'paper', 'scissors']

def random_agent(env=agent_env):
    return np.random.choice(env)

def get_opp_choice(dur=5.):
    return options.index(videoCap(dur))
    
#opp_choice = str(input('rock, paper, or scissors: ').lower())
# opp_choice = get_opp_choice()
# agent_choice = random_agent()

def winner(options, agt_choice, opp_choice):
    winner = agt_choice - opp_choice
    # print(agent_choice, opp_choice)
    #print(options[agt_choice], agt_choice, opp_choice)

    if winner == 0:
        return 'It was a tie!'
    elif winner > 0:
        return f'Agent picked {options[agt_choice]}, and won!'
    else:
        return f'Agent picked {options[agt_choice]}, and lost'
    
#winner(options, agent_choice, opp_choice)
#print(winner(options, agent_choice, opp_choice))

