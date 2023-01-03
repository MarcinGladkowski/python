import pickle
import copyreg

class GameState:
    def __init__(self, level=0, lives=4, points=0) -> None:
        self.level = 0
        self.lives = 4
        self.points = 0


state = GameState()
state.level += 1
state.lives -= 1
print(state.__dict__)

state_path = 'game_state.bin'
with open(state_path, 'wb') as f:
    pickle.dump(state, f)

with open(state_path, 'rb') as f:
    state_after = pickle.load(f)

print(state_after.__dict__)


def unpickle_game_state(kwargs):
    return GameState(**kwargs)


def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    return unpickle_game_state, (kwargs,)


copyreg.pickle(GameState, pickle_game_state)


state = GameState()
state.points += 1000
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state.__dict__)