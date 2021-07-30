import numpy as np
import cv2

agent_env = [0, 1, 2]
options = ['rock', 'paper', 'scissors']

def random_agent(env=agent_env):
    return np.random.choice(env)

def get_opp_choice():
    pass
    
opp_choice = str(input('rock, paper, or scissors: ').lower())
agent_choice = random_agent()

def winner(options, agt_choice, opp_choice):
    opp_choice = options.index(opp_choice)
    winner = agt_choice - opp_choice
    # print(agent_choice, opp_choice)
    #print(options[agt_choice], agt_choice, opp_choice)

    if winner == 0:
        return 'it was a tie!'
    elif winner > 0:
        return f'agent picked {options[agt_choice]}, and won!'
    else:
        return f'agent picked {options[agt_choice]}, and lost'
    
winner(options, random_agent, get_opp_choice)
#print(winner(options, agent_choice, opp_choice))

