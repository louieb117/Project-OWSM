import sys
import asyncio
import keyboard
import random

class interdimensional_story_reader():

    def __init__(self, textfile):
        self.textfile = textfile
        self.Story_file = open(textfile,"r")

    def random_input():
        return random.randrange(0.5,2.5)

    async def typing_sim(self, input_text):
        for char in range(len(input_text)):
            await asyncio.sleep(random_input())
            print(input_text[char])
            if (keyboard.is_pressed('esc') or keyboard.is_pressed('space')):
                await pause_loop()

    async def pause_loop():
        await keyboard.wait('esc')
        print('\n\n\t\tPaused\n\n\tEnter esc again to exit the program: ')
        keyboard.wait('esc')

    async def end(self):
        ending_text = '\n\n\n\t...ENDING TRANSMISSION...'
        for char in range(len(ending_text)):
            await asyncio.sleep(random_input())
            print(ending_text[char])
        self.Story_file.close()

    async def new_display_text(self):
        file_name = self.textfile
        text = self.Story_file.read()
        await typing_sim(text)
        print('Machine Loop Complete')
        end()



class Board(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill((13,13,13))
        self.image.set_colorkey((13,13,13))
        self.rect = self.image.get_rect()
        self.font = pygame.font.SysFont("monospace", 18)

    def add(self, letter, pos):
        s = self.font.render(letter, 1, (255, 255, 0))
        self.image.blit(s, pos)

class Cursor(pygame.sprite.Sprite):
    def __init__(self, board):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill((0,255,0))
        self.text_height = 17
        self.text_width = 10
        self.rect = self.image.get_rect(topleft=(self.text_width, self.text_height))
        self.board = board
        self.text = ''
        self.cooldown = 0
        self.cooldowns = {'.': 12,
                        '[': 18,
                        ']': 18,
                        ' ': 5,
                        '\n': 30}

    def write(self, text):
        self.text = list(text)

    # This function will give the effect of printing text
    def update(self):
        if not self.cooldown and self.text:
            letter = self.text.pop(0)
            if letter == '\n':
                self.rect.move_ip((0, self.text_height))
                self.rect.x = self.text_width
            else:
                self.board.add(letter, self.rect.topleft)
                self.rect.move_ip((self.text_width, 0))
            self.cooldown = self.cooldowns.get(letter, 8)

        if self.cooldown:
            self.cooldown -= 1




    #def display_image():
