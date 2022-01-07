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

    asyncio def typing_sim(input_text):
        for char in range(len(input_text)):
            await asyncio.sleep(random_input())
            print(input_text[char])
            if (keyboard.is_pressed('esc') or keyboard.is_pressed('space'))
                await pause_loop()

    asyncio def pause_loop():
        await keyboard.wait('esc')
        print('\n\n\t\tPaused\n\n\tEnter esc again to exit the program: ')
        keyboard.wait('esc')

    asyncio def end(self):
        ending_text = '\n\n\n\t...ENDING TRANSMISSION...'
        for char in range(len(ending_text)):
            await asyncio.sleep(random_input())
            print(ending_text[char])
        self.Story_file.close()

    asyncio def new_display_text(self):
        file_name = self.textfile
        text = self.Story_file.read()
        await typing_sim(text)
        print('Machine Loop Complete')
        end()



    #def display_image():
