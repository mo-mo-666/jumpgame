# -*- coding: utf-8 -*-

# ==============================================================================
# set the screen size
#
# default values:
#     SCREEN_WIDTH = 1000
#     SCREEN_SIZE = 600
# Changing this params is NOT recommended if you have trouble with the screen
# size.
# ==============================================================================
SCREEN_WIDTH  = 1000
SCREEN_HEIGHT =  700
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)


# ==============================================================================
# set the block's color and the counter's color
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
# set the difficulty
#
# 'NAME': the name of the level displayed (DO NOT forget '' at each side.)
# 'MOVE_X': set the movement distance par frame
# 'BLOCK_FREQENCY': set the block frequency [D, D+U, D+U+None] par frame, where D
#                 is 'DOWN_BLOCK', U is 'UPPER_BLOCK, and None is 'NOT_APPEAR'
# LEVEL: list of the LEVELs you use this game
# CH_LEVEL: change the level when the counter of passing blocks reaches
#           that number ((Change LEVEL(i+1) to LEVEL(i+2) when the counter
#           reaches CH_LEVEL[i])) Be sure that CH_LEVEL[i] <= CH_LEVEL[i+1] for
#           all i.
# ** You can change the number of the LEVELs. **
#
# default values:
#    LEVEL1 = {'NAME': 'Level 1',
#              'MOVE_X': -3,
#              'BLOCK_FRECENCY': [4, 5, 500]}
#    LEVEL2 = {'NAME': 'Level 2',
#              'MOVE_X': -5,
#              'BLOCK_FRECENCY': [4, 5, 500]}
#    LEVEL3 = {'NAME': 'Level 3',
#              'MOVE_X': -5,
#              'BLOCK_FRECENCY': [16, 20, 500]}
#    LEVEL4 = {'NAME': 'Level 4',
#              'MOVE_X': -8,
#              'BLOCK_FRECENCY': [8, 10, 500]}
#    LEVEL5 = {'NAME': 'Level 5',
#              'MOVE_X': -8,
#              'BLOCK_FRECENCY': [16, 20, 500]}
#
#    LEVEL = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]
#    CH_LEVEL = [10, 30, 50, 80]
# ==============================================================================

LEVEL1 = {'NAME': 'Level 1',
          'MOVE_X': -3,
          'BLOCK_FRECENCY': [4, 5, 500]}
LEVEL2 = {'NAME': 'Level 2',
          'MOVE_X': -5,
          'BLOCK_FRECENCY': [4, 5, 500]}
LEVEL3 = {'NAME': 'Level 3',
          'MOVE_X': -5,
          'BLOCK_FRECENCY': [16, 20, 500]}
LEVEL4 = {'NAME': 'Level 4',
          'MOVE_X': -8,
          'BLOCK_FRECENCY': [8, 10, 500]}
LEVEL5 = {'NAME': 'Level 5',
          'MOVE_X': -8,
          'BLOCK_FRECENCY': [16, 20, 500]}

LEVEL = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]
CH_LEVEL = [10, 30, 50, 80]


# ==============================================================================
# set the movement distance when the character is jumping and falling
#
# MOVE_UP(default = -20): a negative number
# MOVE_DOWN:(default = 10) a positive number
# Changing this params is NOT recommended.
# ==============================================================================
MOVE_UP   = -20
MOVE_DOWN =  10