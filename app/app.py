import sys, getopt
import pygame
from interdimensional_story_reader import interdimensional_story_reader

# ----------------------------------------------------------------------
# Sprites
# ----------------------------------------------------------------------

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


# ----------------------------------------------------------------------
# Screen Layouts
# ----------------------------------------------------------------------













# ----------------------------------------------------------------------
# System Logic
# ----------------------------------------------------------------------



class app():
    def __init__(self):
        self.file_name = ''
        self.number = 1
        self.story = ''
        self.run_state = True
        self.WIDTH = 500
        self.HEIGHT = 500
        self.WINDOW_TITLE = 'Project OWSM'
        self.COLOR_BACKGROUND = (0,0,0)
        self.title_screen = True
        self.menu_screen = False
        self.credit_screen = False
        self.reader_screen = False
        self.pause_screen = False
        self.exit_screen = False

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

    def display_title_screen(self):
        # Displays title assets with text requesting to Press Enter

    def credit_screen_loop(self):
        # Display credits


    def dislay_menu_loop(self):
        # Display menu screen with buttons( cedit screen, Story List, exit )

        #

    def Machine_Loop(self):
        pygame.init()
        #Sets mouse cursor visibility
        pygame.mouse.set_visible(False)
        #Sets the screen note: must be after pygame.init()

        window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        window.display.set_caption(self.WINDOW_TITLE)
        color = self.COLOR_BACKGROUND
        window.fill(color)
        pygame.display.flip()

        clock = pygame.time.Clock()
        run = self.run_state
        FPS = 60
        self.story = Interdimensional_Story_Reader(self.file_name, self.number)

        all_sprites = pygame.sprite.Group()
        board = Interdimensional_Story_Reader.Board()
        cursor = Interdimensional_Story_Reader.Cursor(board)
        all_sprites.add(cursor, board)

        text = self.story
        cursor.write(text)

        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                # Exits program if window is closed
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                # Title Screen Key Handler
                if (self.title_screen & event.type == pygame.KEYDOWN):
                    if event.key != pygame.K_ENTER:
                        return
                    # calls Menu screen render event

                    self.title_screen = False
                    self.menu_screen = True
                # Menu Screen Key Handler
                if (self.menu_screen & event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_DOWN:
                        # Checks to see if Cursor Sprite is on last selection
                        # Calls Sprite to render down 1 selection
                    elif event.key == pygame.K_UP:
                        # Checks to see if Cursor Sprite is on the top selection
                        # Calls Sprite to render up 1 selection
                    elif event.key == pygame.K_ENTER:
                        # Checks to see which selection the Cursor Sprite is on
                        # Calls Reader or  Credits or Exits render event
                    self.menu_screen = False
                # Credits Screen Key Handler
                if (self.credit_screen & event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_ENTER:
                        # Calls menu_screen render event
                    self.credit_screen = False
                    self.menu_screen = True
                # Reader Screen Key Handler
                if (self.reader_screen & event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_ESCAPE:
                        # Calls pause menu render event
                        self.story.pause_loop()
                    self.reader_screen = False
                    self.pause_screen = True
                # Pause Screen Key Handler
                if (self.pause_screen & event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_ENTER:
                        # Calls reader render event
                    self.pause_screen = False
                    self.reader_screen = True
                    elif event.key == pygame.K_ESCAPE:
                        # Calls menu render event
                    self.pause_screen = False
                    self.menu_screen = True

                # Exit Screen Key Handler
                if (self.exit_screen & event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_ENTER:
                        pygame.quit()
                    elif event.key == pygame.K_ESCAPE:
                        # Calls menu render event
                    self.exit_screen = False
                    self.menu_screen = True
            display_title_screen()
            if
            # Init Menu Loop
            menu_loop()





        self.story.end()


# ----------------------------------------------------------------------
# Excutable
# ----------------------------------------------------------------------

if __name__ == "__main__":
    app1 = app()
    app1.cli_arg(sys.argv[1:])

    app1.Machine_Loop()
