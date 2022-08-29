class State:
    def __init__(self, number):
        self.number = number
        self.actions = ['UP', 'LEFT', 'DOWN', 'RIGHT']
        self.action_preference_vector = [1, 1, 1, 1]
        self.action_value_estimates = [1, 1, 1, 1]
        self.up_k = 0
        self.left_k = 0
        self.down_k = 0
        self.right_k = 0
