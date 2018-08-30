# -*- coding: utf-8 -*-

# ==============================================================================
# SET THE SCREEN SIZE
#
# default values:
#     SCREEN_WIDTH = 1000
#     SCREEN_SIZE = 600
# ==============================================================================
SCREEN_WIDTH  = 1000
SCREEN_HEIGHT =  600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)


# ==============================================================================
# SET THE BLOCK'S COLOR AND THE COUNTER'S COLOR
#
# BLOCK's name is not used, but do not set the same name.
# You can use your customized color (R, G, B) .
#
# default values:
#     LOWER_BLOCK = {'Name': 'Lower',
#                    'color': BLUE}
#     UPPER_BLOCK = {'Name': 'upper',
#                    'color': RED}
#     COUNT_C       = GREEN
#     LEVEL_C       = GREEN
# ==============================================================================
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

LOWER_BLOCK = {'NAME': 'Lower',
               'COLOR': BLUE}
UPPER_BLOCK = {'NAME': 'upper',
               'COLOR': RED}
COUNT_C       = GREEN
LEVEL_C       = GREEN


# ==============================================================================
# SET THE LEVEL
#
# B_MIN DISTANCE: the minimum distance between blocks
# 'NAME': the name of the level displayed (DO NOT forget ' at each side.)
# 'MOVE_X': set the movement distance par frame
# 'BLOCK_FREQUENCY': set the block frequency [D, D+U, D+U+None] par frame, where D
#                 is 'DOWN_BLOCK', U is 'UPPER_BLOCK, and None is 'NOT_APPEAR'
# LEVEL: list of the LEVELs you use this game
# CH_LEVEL: change the level when the counter of passing blocks reaches
#           that number ((Change LEVEL(i+1) to LEVEL(i+2) when the counter
#           reaches CH_LEVEL[i])) Be sure that CH_LEVEL[i] <= CH_LEVEL[i+1] for
#           all i.
# ** You can change the number of the LEVELs. **
#
# default values:
#    B_MIN_DISTANCE = 100
#    LEVEL1 = {'NAME': 'Level 1',
#              'MOVE_X': -3,
#              'BLOCK_FREQUENCY': [4, 5, 500]}
#    LEVEL2 = {'NAME': 'Level 2',
#              'MOVE_X': -5,
#              'BLOCK_FREQUENCY': [4, 5, 500]}
#    LEVEL3 = {'NAME': 'Level 3',
#              'MOVE_X': -5,
#              'BLOCK_FREQUENCY': [16, 20, 500]}
#    LEVEL4 = {'NAME': 'Level 4',
#              'MOVE_X': -8,
#              'BLOCK_FREQUENCY': [8, 10, 500]}
#    LEVEL5 = {'NAME': 'Level 5',
#              'MOVE_X': -8,
#              'BLOCK_FREQUENCY': [16, 20, 500]}
#    LEVEL = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]
#    CH_LEVEL = [10, 30, 50, 80]
# ==============================================================================

B_MIN_DISTANCE = 100

LEVEL1 = {'NAME': 'Level 1',
          'MOVE_X': -3,
          'BLOCK_FREQUENCY': [4, 5, 500]}
LEVEL2 = {'NAME': 'Level 2',
          'MOVE_X': -5,
          'BLOCK_FREQUENCY': [4, 5, 500]}
LEVEL3 = {'NAME': 'Level 3',
          'MOVE_X': -5,
          'BLOCK_FREQUENCY': [16, 20, 500]}
LEVEL4 = {'NAME': 'Level 4',
          'MOVE_X': -8,
          'BLOCK_FREQUENCY': [8, 10, 500]}
LEVEL5 = {'NAME': 'Level 5',
          'MOVE_X': -8,
          'BLOCK_FREQUENCY': [16, 20, 500]}

LEVEL = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]
CH_LEVEL = [10, 30, 50, 80]


# ==============================================================================
# SET THE MOVEMENT DISTANCE WHEN THE CHARACTER IS JUMPING AND FALLING
#
# MOVE_UP:  when the character jumps up. (a negative number)
# MOVE_DOWN: when the character falls down (a positive number)
# Changing this params is NOT recommended.
#
# default values:
#     MOVE_UP   = -SCREEN_HEIGHT // 30
#     MOVE_DOWN =  SCREEN_HEIGHT // 60
# ==============================================================================
MOVE_UP   = -SCREEN_HEIGHT // 30
MOVE_DOWN =  SCREEN_HEIGHT // 60

