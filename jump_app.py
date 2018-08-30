# -*- coding: utf-8 -*-

import pygame as pg
import random

from set_params import *


class Widget:

    def __init__(self):
        self.state = 'opening'
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.screen.fill(BLACK)
        self.clock = pg.time.Clock()
        self.init2()
        self.update()

    def init2(self):
        self.block = Blocks()
        self.character = Character()
        self.cha, self.cha_rect = self.character.update()
        self.cha_move = None
        self.count = 0
        self.level = LEVEL[0]

    def update(self):
        while self.state == 'opening':
            self.screen.fill(BLACK)
            font = pg.font.Font(None, 100)
            text = font.render('JUMP GAME!', True, RED)
            self.screen.blit(text, ((SCREEN_WIDTH-text.get_width())/2, SCREEN_HEIGHT/3 - text.get_height()/2))
            font2 = pg.font.Font(None, 50)
            text2 = font2.render('Press the Space key!', True, WHITE)
            self.screen.blit(text2, ((SCREEN_WIDTH-text2.get_width())/2,SCREEN_HEIGHT*4/5 - text.get_height()/2))
            pg.display.update()
            self.event_handler()

        while self.state == 'play':
            if self.cha_rect.right > 0:
                self.set_difficulty()
                self.screen.fill(BLACK)
                self.update_blocks()
                self.event_handler()
                self.update_character()
                self.update_counter()
                pg.display.update()
                # flame rate maximum
                self.clock.tick(60)
            else:
                self.state = 'gameover'

        while self.state == 'gameover':
            self.screen.fill(BLACK)
            font = pg.font.Font(None, 200)
            count = self.block.counter
            text = font.render(str(count), True, COUNT_C)
            self.screen.blit(text, ((SCREEN_WIDTH-text.get_width())/2, SCREEN_HEIGHT/3-text.get_height()/2))
            font2 = pg.font.Font(None, 30)
            text2 = font2.render(self.level['NAME'], True, LEVEL_C)
            self.screen.blit(text2, ((SCREEN_WIDTH-text2.get_width())/2, (SCREEN_HEIGHT-text2.get_height())/2))
            font3 = pg.font.Font(None, 50)
            text3 = font3.render('Press the Space key to play again!', True, WHITE)
            self.screen.blit(text3, ((SCREEN_WIDTH-text3.get_width())/2, SCREEN_HEIGHT*4/5-text3.get_height()/2))
            pg.display.update()
            self.event_handler()

        if self.state == 'again':
            self.state = 'play'
            self.init2()
            self.update()

    def update_blocks(self):
        self.blocklist = self.block.update()
        for rect, b_type in self.blocklist:
            pg.draw.rect(self.screen, b_type['COLOR'], rect)

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.state = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if self.state == 'opening':
                        self.state = 'play'
                    elif self.state == 'gameover':
                        self.state = 'again'
                elif event.key == pg.K_ESCAPE:
                    self.state = False
                elif event.key == pg.K_UP:
                    self.cha_move = 'jump'
                elif event.key == pg.K_DOWN:
                    self.cha_move = 'crouch'
            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.cha_move = None
                elif event.key == pg.K_DOWN:
                    self.cha_move = None

    def update_character(self):
        cha_crash = False
        block_height = SCREEN_HEIGHT

        for b_rect, b_type in self.blocklist:
            if b_rect.left <= self.cha_rect.right <= b_rect.right:
                if b_rect.top >= self.cha_rect.bottom:
                    cha_crash = False
                    block_height = b_rect.top
                    break
                elif b_rect.bottom < self.cha_rect.top:
                    cha_crash = False
                    block_height = SCREEN_HEIGHT
                    break
                else:
                    cha_crash = b_type
                    block_height = SCREEN_HEIGHT
                    break
            elif (b_rect.left <= self.cha_rect.left <= b_rect.right) or \
               (self.cha_rect.left <= b_rect.left <= b_rect.right <= self.cha_rect.right):
                cha_crash = False
                if b_rect.top == 0:
                    block_height = SCREEN_HEIGHT
                else:
                    block_height = b_rect.top
                break

        self.cha, self.cha_rect = self.character.update(self.cha_move, cha_crash, block_height)
        self.screen.blit(self.cha, self.cha_rect)

    def update_counter(self):
        font = pg.font.Font(None, 55)
        self.count = self.block.counter
        text = font.render(str(self.count), True, COUNT_C)
        self.screen.blit(text, (SCREEN_WIDTH-100, 30))
        font2 = pg.font.Font(None, 30)
        text2 = font2.render(self.level['NAME'], True, LEVEL_C)
        self.screen.blit(text2, (50, 30))

    def set_difficulty(self):
        for i in range(len(CH_LEVEL)):
            if self.level == LEVEL[i]:
                if self.count >= CH_LEVEL[i]:
                    self.level = LEVEL[i+1]
        self.block.set_param(self.level)
        self.character.set_param(self.level)


class Blocks:

    def __init__(self):
        self.blocklist = []
        self.last_x = None
        self.counter = 0

    def set_param(self, level):
        self.move_x = level['MOVE_X']
        self.block_frequency = level['BLOCK_FREQUENCY']

    def update(self):
        if not self.blocklist:
            width = 30
            rect = pg.Rect(SCREEN_WIDTH+200, SCREEN_HEIGHT-100, width, 100)
            self.blocklist.append((rect, LOWER_BLOCK))
            self.last_x = SCREEN_WIDTH+200 + width
        else:
            blocklist = []
            for rect, b_type in self.blocklist:
                if rect.right >= 0:
                    blocklist.append((rect.move(self.move_x, 0), b_type))
                else:
                    self.counter += 1
            self.blocklist = blocklist
            self.last_x += self.move_x

            if self.last_x < SCREEN_WIDTH - B_MIN_DISTANCE:
                boolean = random.choices(['lower', 'upper', False],
                                         cum_weights=self.block_frequency)[0]
                if boolean == 'lower':
                    height = random.randrange(50, int(SCREEN_HEIGHT/2))
                    width = random.randrange(30, 70)
                    rect = pg.Rect(SCREEN_WIDTH, SCREEN_HEIGHT-height, width, height)
                    self.blocklist.append((rect, LOWER_BLOCK))
                    self.last_x = SCREEN_WIDTH + width
                elif boolean == 'upper':
                    width = random.randrange(50, 200)
                    rect = pg.Rect(SCREEN_WIDTH, 0, width, SCREEN_HEIGHT-60)
                    self.blocklist.append((rect, UPPER_BLOCK))
                    self.last_x = SCREEN_WIDTH + width

        return self.blocklist


class Character:

    def __init__(self):
        self.normal = pg.image.load("./images/normal.png").convert_alpha()
        self.crouching = pg.image.load("./images/crouching.png").convert_alpha()
        self.normal_rect = self.normal.get_rect()
        self.crouching_rect = self.crouching.get_rect()
        self.bottom = SCREEN_HEIGHT
        self.right =  SCREEN_WIDTH * 4/5
        self.highjump1 = False
        self.highjump2 = False
        self.jumpheight1 = SCREEN_HEIGHT / 3
        self.jumpheight2 = SCREEN_HEIGHT * 2/3
        self.base_height = SCREEN_HEIGHT
        self.init_height = SCREEN_HEIGHT

    def set_param(self, level):
        self.move_x = level['MOVE_X']

    def update(self, move=None, crash=False, block_height=SCREEN_HEIGHT):
        self.base_height = block_height
        if crash:
            self.right += self.move_x

        if self.bottom == self.base_height:
            if not move or (move == 'jump' and crash == UPPER_BLOCK):
                self.drop()
                self.normal_rect.bottom = self.bottom
                self.normal_rect.right = self.right
                return self.normal, self.normal_rect

            elif move == 'jump':
                self.highjump1 = True
                self.highjump2 = True
                self.init_height = self.base_height
                self.jump()
                self.normal_rect.bottom = self.bottom
                self.normal_rect.right = self.right
                return self.normal, self.normal_rect

            elif move == 'crouch':
                self.drop()
                self.crouching_rect.bottom = self.bottom
                self.crouching_rect.right = self.right
                return self.crouching, self.crouching_rect

        elif self.bottom > self.init_height-self.jumpheight1 and self.highjump1:
            self.jump()
            self.normal_rect.bottom = self.bottom
            self.normal_rect.right = self.right
            return self.normal, self.normal_rect

        elif self.bottom > self.init_height-self.jumpheight2 and self.highjump2:
            self.highjump1 = False
            if move == 'jump':
                self.jump()
                self.normal_rect.bottom = self.bottom
                self.normal_rect.right = self.right
                return self.normal, self.normal_rect

            else:
                self.drop()
                self.normal_rect.bottom = self.bottom
                self.normal_rect.right = self.right
                return self.normal, self.normal_rect

        else:
            self.drop()
            self.normal_rect.bottom = self.bottom
            self.normal_rect.right = self.right
            return self.normal, self.normal_rect

    def drop(self):
        self.highjump1 = False
        self.highjump2 = False
        if self.bottom < self.base_height - MOVE_DOWN:
            self.bottom += MOVE_DOWN
        else:
            self.bottom = self.base_height

    def jump(self):
        self.bottom += MOVE_UP


def main():
    pg.init()
    pg.display.set_caption("Jump!")
    Widget()
    pg.quit()


if __name__ == '__main__':
    main()

