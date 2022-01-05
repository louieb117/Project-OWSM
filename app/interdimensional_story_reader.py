import sys
from slowprint.slowprint import *

class interdimensional_story_reader():

    def __init__(self, textfile, speed_setting = 1):
        self.textfile = textfile
        self.speed_setting = int(speed_setting)
        self.Story_file = open(textfile,"r")

    def end(self):
        speed = self.speed_setting
        slowprint('\n\n\n\t...ENDING TRANSMISSION',speed)
        self.Story_file.close()

    def display_text(self):
        file_name = self.textfile
        speed = self.speed_setting
        text = self.Story_file.read()
        slowprint(text, speed)
        slowprint('\n\n\n\t...ENDING TRANSMISSION',speed)
        self.Story_file.close()

    def new_display_text(self):


    #def display_image():
