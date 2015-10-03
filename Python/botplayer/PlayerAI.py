from PythonClientAPI.libs.Game.Enums import *
from PythonClientAPI.libs.Game.MapOutOfBoundsException import *


class PlayerAI:
    def __init__(self):
        # Initialize any objects or variables you need here.
        pass

    def get_move(self, gameboard, player, opponent):
        # Write your AI here.
        return self.shoot()

    def turn_right(self):
        # turns the bot to the face right
        return Move.FACE_RIGHT

    def turn_left(self):
        # turns the bot to the face left
        return Move.FACE_LEFT

    def turn_up(self):
        # turns the bot to the face up
        return Move.FACE_UP

    def turn_down(self):
        # turns the bot to the face down
        return Move.FACE_DOWN

    def move_right(self):
        # moves the bot to the right
        self.turn_right()
        return Move.FORWARD

    def move_left(self):
        # moves the bot to the left
        self.turn_left()
        return Move.FORWARD

    def move_up(self):
        # moves the bot up
        self.turn_up()
        return Move.FORWARD

    def move_down(self):
        # moves the bot down
        self.turn_down()
        return Move.FORWARD

    def move_none(self):
    	# no move
    	return Move.NONE;

    def shoot(self):
    	# shoot a bullet in the direction currently facing
    	return Move.SHOOT;

    def shield(self):
    	# shiled yourself for 5 turns
    	return Move.SHIELD;

    def laser(self):
    	#shoot lasers
    	return Move.LASER;

    def teleport(self, position):
    	# teleport to position
    	if position == 0:
    		return Move.TELEPORT_0;

    	elif position == 1:
    		return Move.TELEPORT_1;
    	
    	elif position == 2:
    		return Move.TELEPORT_2;
    	
    	elif position == 3:
    		return Move.TELEPORT_3;
    	
    	elif position == 4:
    		return Move.TELEPORT_4;
    	
    	elif position == 5:
    		return Move.TELEPORT_5;

    	else:
    		raise TeleportOutOfBoundsError("Teleport position should be between 0 & 5.")