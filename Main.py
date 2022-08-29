from Environment import Environment
from Agent import Agent

agent = Agent()
env = Environment(10, 9, 0, agent, 0.1)

episodes = 10000
best_score = float('-inf')
best_moves = []
for i in range(episodes):
    print('Episode:', i)
    env.is_episode_finished = False
    while not env.is_episode_finished:
        env.select_action()
    print('Agent Score:', agent.score)
    if agent.score > best_score:
        best_score = agent.score
        best_moves = agent.moves
    # Reset agent
    agent.score = 0
    agent.position_row = 0
    agent.position_col = 0
    agent.moves = []


print('\nBest Score:', best_score)
print('Best Moves:', best_moves)
