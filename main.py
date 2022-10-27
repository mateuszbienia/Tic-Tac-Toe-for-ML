from environment.TicTacToeEnv import TicTacToeEnv
import random


def simulate_game(render=False):
    env = TicTacToeEnv()
    obs, _ = env.reset()
    if render:
        env.render()
    game_over, truncated = False, False
    while not (game_over or truncated):
        action = random.choice(env.get_moves())
        _, _, game_over, truncated, _ = env.step(action)
        if render:
            env.render()


if __name__ == "__main__":
    simulate_game(render=True)
