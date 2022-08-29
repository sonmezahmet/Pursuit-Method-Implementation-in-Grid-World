from State import State
import numpy as np


class Environment:
    def __init__(self, size, goal_state_row, goal_state_col, agent, beta):
        self.is_episode_finished = False
        self.size = size
        self.agent = agent
        self.beta = beta
        self.grid = [[0] * self.size for i in range(self.size)]

        # Create grid
        for i in range(size):
            for j in range(size):
                self.grid[i][j] = State(size * i + j)

        self.goal_state = self.grid[goal_state_row][goal_state_col]

    def move(self, state, action):
        self.agent.moves.append(action)

        if action == 'UP':
            if self.agent.position_row != 0:
                self.agent.position_row -= 1
        elif action == 'LEFT':
            if self.agent.position_col != 0:
                self.agent.position_col -= 1
        elif action == 'DOWN':
            if self.agent.position_row != self.size - 1:
                self.agent.position_row += 1
        elif action == 'RIGHT':
            if self.agent.position_col != self.size - 1:
                self.agent.position_col += 1

        response = self.response(self.grid[self.agent.position_row][self.agent.position_col])
        self.agent.score += response

        # Update action value estimate of state
        self.update_action_value_estimate(state, action, response)

        # Determine greedy action
        greedy_action = max(state.action_value_estimates)
        greedy_action_index = state.action_value_estimates.index(greedy_action)

        # Update action preferences
        for index, value in enumerate(state.action_preference_vector):
            if index is greedy_action_index:
                state.action_preference_vector[index] = value + self.beta * (1 - value)
                continue
            state.action_preference_vector[index] = value + self.beta * (0 - value)

        if response == 100:
            self.is_episode_finished = True

    def response(self, state):
        if state == self.goal_state:
            return 100
        else:
            return -0.5

    def select_action(self):
        curr_state = self.grid[self.agent.position_row][self.agent.position_col]

        # Calculate probabilities
        action_preference_vector = curr_state.action_preference_vector
        sum_apv = sum(action_preference_vector)
        probabilities = [0, 0, 0, 0]
        probabilities[0] = (action_preference_vector[0] / sum_apv)
        probabilities[1] = (action_preference_vector[1] / sum_apv)
        probabilities[2] = (action_preference_vector[2] / sum_apv)
        probabilities[3] = (action_preference_vector[3] / sum_apv)

        # Select an action and move
        possible_actions = curr_state.actions
        self.move(curr_state, np.random.choice(possible_actions, 1, p=probabilities)[0])

    def update_action_value_estimate(self, state, action, response):
        if action == 'UP':
            state.up_k += 1
            state.action_value_estimates[0] = state.action_value_estimates[0] + (1 / (state.up_k + 1)) * \
                                              (response - state.action_value_estimates[0])
        elif action == 'LEFT':
            state.left_k += 1
            state.action_value_estimates[1] = state.action_value_estimates[1] + (1 / (state.left_k + 1)) * \
                                              (response - state.action_value_estimates[1])
        elif action == 'DOWN':
            state.down_k += 1
            state.action_value_estimates[2] = state.action_value_estimates[2] + (1 / (state.down_k + 1)) * \
                                              (response - state.action_value_estimates[2])
        elif action == 'RIGHT':
            state.right_k += 1
            state.action_value_estimates[3] = state.action_value_estimates[3] + (1 / (state.right_k + 1)) * \
                                              (response - state.action_value_estimates[3])
        else:
            raise Exception('Not valid action!')
