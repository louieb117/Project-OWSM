import sys, getopt
import pygame
from interdimensional_story_reader import interdimensional_story_reader


class app():
    def __init__(self):
        self.file_name = ''
        self.number = 1
        self.story = ''
        self.run_state = True
        self.WIDTH = 500
        self.HEIGHT = 500
        self.WINDOW_TITLE = 'Project OWSM'

    def cli_arg(self, argv):
        try:
            opts, args = getopt.getopt(argv,"h:f:",["file="])
        except getopt.GetoptError:
            print ('app.py -f <inputfile>')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print ('app.py -f <inputfile>')
                sys.exit()
            elif opt in ("-f", "--file"):
                self.file_name = arg

    def reader_call(self):


        return self.story.display_text()


    def background_func(self):
        # Displays background assets

    def Board(self):
        # Surface / Textbox

    def Cursor(self):
        # Terminal Cursor Sprite

    def title_screen_loop(self):
        # Displays title assets with text requesting to Press Enter

    def credit_screen_loop(self):
        # Display credits

    def


    def menu_loop(self):
        # Display menu screen with buttons( cedit screen, Story List, exit )


    def Machine_Loop(self):
        pygame.init()
        #Sets mouse cursor visibility
        pygame.mouse.set_visible(False)
        #Sets the screen note: must be after pygame.init()

        window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        window.display.set_caption(self.WINDOW_TITLE)
        color = (0,0,0)
        window.fill(color)
        pygame.display.flip()

        clock = pygame.time.Clock()
        run = self.run_state
        FPS = 60
        self.story = interdimensional_story_reader(self.file_name, self.number)

        all_sprites = pygame.sprite.Group()
        board = interdimensional_story_reader.Board()
        cursor = interdimensional_story_reader.Cursor(board)
        all_sprites.add(cursor, board)

        text = self.story
        cursor.write(text)

        # Init Title Loop
        title_screen_loop()

        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                # Exits program if window is closed
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                # Init Pause Loop
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.story.pause_loop()

            # Init Menu Loop
            menu_loop()





        self.story.end()

if __name__ == "__main__":
    app1 = app()
    app1.cli_arg(sys.argv[1:])

    app1.Machine_Loop()
