from PythonClientAPI.libs.Game.Enums import *
from PythonClientAPI.libs.Game.MapOutOfBoundsException import *


class PlayerAI:
    def __init__(self):
        # Initialize any objects or variables you need here.
        self.turret_positions = []
        self.power_up_positions = []
        self.wall_positions = []

    def get_move(self, gameboard, player, opponent):
        # if we haven't already, get the turret positions
        if self.turret_positions == []:
            self.get_turret_positions(gameboard)

        # if we haven't already, get the power up positions
        if self.power_up_positions == []:
            self.get_power_up_positions(gameboard)

        # if we haven't already, get the wall positions
        if self.wall_positions == []:
            self.get_wall_positions(gameboard)

            if player.x < opponent.x:
                if player.direction == Direction.RIGHT:
                    return Move.FORWARD
                else:
                    return Move.FACE_RIGHT
            elif player.x > opponent.x:
                if player.direction == Direction.LEFT:
                    return Move.FORWARD
                else:
                    return Move.FACE_LEFT
            else:
                if player.y > opponent.y:
                    if player.direction == Direction.UP:
                        return Move.SHOOT
                    else:
                        return Move.FACE_UP
                else:
                    if player.direction == Direction.DOWN:
                        return Move.SHOOT
                    else:
                        return Move.FACE_DOWN

    def get_turret_positions(self, gameboard):
        # gets all the turrets present on the board

        for row in range(gameboard.width):

            for col in range(gameboard.height):

                if gameboard.is_turret_at_tile(row, col):
                    # append the position to the turret pos list
                    self.turret_positions.append((col, row))

        # if no turrets are present on the board, set the list to None
        if self.turret_positions == []:
            self.turret_positions = None

    def get_power_up_positions(self, gameboard):
        # gets all the power ups present on the board

        for row in range(gameboard.width):

            for col in range(gameboard.height):

                if gameboard.is_power_up_at_tile(row, col):
                    # append the position to the power ups pos list
                    self.power_up_positions.append((col, row))

        # if not power ups are present on the board, set the list to None
        if self.power_up_positions == []:
            self.power_up_positions = None

    def get_wall_positions(self, gameboard):
        # gets all the wall present on the board

        for row in range(gameboard.width):

            for col in range(gameboard.height):

                if gameboard.is_wall_at_tile(row, col):
                    # append the position to the wall pos list
                    self.wall_positions.append((col, row))

        # if no walls are present on the board, set the list to None
        if self.wall_positions == []:
            self.wall_positions = None