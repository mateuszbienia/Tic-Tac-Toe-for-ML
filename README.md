# Tic-Tac-Toe-for-ML
This project was created to make a fast tic-tac-toe environment for machine learning. It uses a bitboard to speed up calculation processes. The project works with gym environments for easy adjustment for other machine learning projects.

Game state is represented as list of 9 elements that can be shown on game board as:
```
    0|1|2
    -+-+-
    3|4|5
    -+-+-
    6|7|8
```
## Example of use
For gym environment usage:
```python
import gym
gym.envs.registration.register(
    id='TicTacToeEnv-v0',
    entry_point='[path-to-package]:TicTacToeEnv',
)
env = gym.make('TicTacToeEnv-v0')
```

and then for each game use:
```python
obs, info = env.reset()
game_over, truncated = False, False
while not (game_over or truncated):
    action = random.choice(env.get_moves())
    observation, reward, game_over, truncated, info = env.step(action)
```

