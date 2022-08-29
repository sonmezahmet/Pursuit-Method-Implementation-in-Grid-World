# Reinforcement Learning - Pursuit Method Implementation
## State Class
![image](https://user-images.githubusercontent.com/56430166/187244340-3b9e4c4a-ed0e-4f33-8a6c-28b23250d47c.png) <br>
Each state has 4 possible actions which are up, left, down, right. There are two vectors
which represents action preferences and action value estimates. Each dimension on
those vectors corresponds to a possible action. Those values will be updated after each
action which agent take in this state. In addition, there are 4 integer attribute for tracking
which action is selected how many times.
<br>
## Agent Class
![image](https://user-images.githubusercontent.com/56430166/187244657-af1b8ce9-bd34-43a7-bd7b-997becbcbb5f.png) <br>
For representing the agent’s initial position on the grid there are two attributes which are
position_row and position_column. After each action taken by the agent, the environment
responses a reward value. To keep track of those actions and to sum rewards in each
episode, there are two attributes which are score and moves array.
<br>
## Environment Class
![image](https://user-images.githubusercontent.com/56430166/187244827-a87669a8-0f4c-4446-b443-7737741b1ec8.png) <br>
To represent environment, the Environment class creates an (size x size) 2D array and
assigns each cell to a State object. It takes goal state’s position, the agent, and the hyper
parameter beta as parameter. Beside that, to give feedback to the Main class, it has
is_episode_finished attribute. <br>
![image](https://user-images.githubusercontent.com/56430166/187244946-26f2569a-0ce7-4df4-b11c-2520bc681888.png) <br>
To select which action will be taken on the current timestamp, the action preference
vector of the current state is used. For each dimension value in that vector is assigned to
a probability value and according to those probabilities an action is selected.
<br>
![image](https://user-images.githubusercontent.com/56430166/187245007-8a4b58eb-69dc-46c8-a317-aeaf05280fcc.png) <br>
move() function takes 2 arguments which are the current state which agent’s in and the
action taken by the agent. According to the action value, the agent’s position changes.
After a change, the environment gives a response to the agent to say how favorable the
action taken by agent is (If the moved state is goal state then the environment’s response
is +100, otherwise -0.5).
<br>
![image](https://user-images.githubusercontent.com/56430166/187245115-61b7e2d4-c7c6-4c20-8c01-e882dd9574f9.png) <br>
Depending on this response the current state’s action value estimation and action
preferences vectors update.
<br>
![image](https://user-images.githubusercontent.com/56430166/187245186-6aaa2e01-e90c-49d1-b0f7-1a1e5e4bc692.png) <br>
If the given response to the agent is +100, it means that the current episode is finished.
<br>
## Main() Function
![image](https://user-images.githubusercontent.com/56430166/187245346-3fa0024d-feca-44d1-973e-eaf95e5f124d.png) <br>
In main() function I initiated that an agent and an environment object. My environment’s
size is 10x10, the goal state is in (9,0) and the beta value is 0.1. Then I simulated the
agent on the environment as 10000 times. After simulation part, the program prints the
best score and the best moves taken by the agent in an episode.






