from PythonClientAPI.libs.Game.Enums import *
from PythonClientAPI.libs.Game.MapOutOfBoundsException import *


class PlayerAI:
    def __init__(self):
        # Initialize any objects or variables you need here.
        pass

    def get_move(self, gameboard, player, opponent):
        # Write your AI here.
        return Move.NONE

    def move_right(self):
        Move.FACE_RIGHT
        MOVE.FORWARD

    def move_left(self):
        Move.FACE_LEFT
        Move.FORWARD

    def move_up(self):
        Move.FACE_UP
        Move.FORWARD

    def move_down(self):
        Move.FACE_DOWN
        Move.FORWARD