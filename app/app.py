import sys, getopt
import pygame
from interdimensional_story_reader import Interdimensional_Story_Reader

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

class Text_Cursor(pygame.sprite.Sprite):
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
        self.WIDTH = 1024
        self.HEIGHT = 1024
        self.WINDOW_TITLE = 'Project OWSM'
        self.COLOR_BACKGROUND = (0,0,0)
        self.title_screen = True
        self.menu_screen = False
        self.credit_screen = False
        self.reader_screen = False
        self.pause_screen = False
        self.exit_screen = False
        self.menu_count = 0

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

    def Machine_Loop(self):
        pygame.init()
        #Sets mouse cursor visibility
        pygame.mouse.set_visible(False)
        #Sets the screen note: must be after pygame.init()

        window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.WINDOW_TITLE)
        color = self.COLOR_BACKGROUND
        window.fill(color)

        title_screen_png = pygame.image.load('images/Title_Screen.png')
        title_screen_png = pygame.transform.scale(title_screen_png, (self.WIDTH, self.HEIGHT))
        menu_screen_activate_png = pygame.image.load('images/Menu_Screen_Activate.png')
        menu_screen_activate_png = pygame.transform.scale(menu_screen_activate_png, (self.WIDTH, self.HEIGHT))
        menu_screen_credits_png = pygame.image.load('images/Menu_Screen_Credits.png')
        menu_screen_credits_png = pygame.transform.scale(menu_screen_credits_png, (self.WIDTH, self.HEIGHT))
        menu_screen_exit_png = pygame.image.load('images/Menu_Screen_Exit.png')
        menu_screen_exit_png = pygame.transform.scale(menu_screen_exit_png, (self.WIDTH, self.HEIGHT))
        reader_screen_png = pygame.image.load('images/Test_Screen.png')
        reader_screen_png = pygame.transform.scale(reader_screen_png, (self.WIDTH, self.HEIGHT))
        credits_screen_png = pygame.image.load('images/Test_Screen.png')
        credits_screen_png = pygame.transform.scale(credits_screen_png, (self.WIDTH, self.HEIGHT))
        pause_screen_png = pygame.image.load('images/Pause_Screen.png')
        pause_screen_png = pygame.transform.scale(pause_screen_png, (self.WIDTH, self.HEIGHT))

        clock = pygame.time.Clock()
        run = self.run_state
        FPS = 60
        menu_weight = self.menu_count
        #self.story = Interdimensional_Story_Reader(self.file_name, self.number)

        all_sprites = pygame.sprite.Group()
        board = Board(500, 500)
        text_cursor = Text_Cursor(board)
        #all_sprites.add(text_cursor, board, menu_cursor)
        #all_sprites.add(menu_cursor)

        text = self.story
        text_cursor.write(text)

        while run:
            clock.tick(FPS)
            if FPS%60: print(time.clock())

            for event in pygame.event.get():

                # Exits program if window is closed
                if event.type == pygame.QUIT:
                    print('Program Exit Protocol')
                    run = False
                    pygame.quit()
                    sys.exit('Done')

                # Title Screen Key Handler
                if (self.title_screen and event.type == pygame.KEYDOWN):
                    print('Image Copy')
                    if event.key == pygame.K_RETURN:
                        # Calls Menu screen render event
                        print('Enter key was pressed in the Title Screen')
                        self.title_screen = False
                        self.menu_screen = True
                    break

                # Menu Screen Key Handler
                if (self.menu_screen and event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_DOWN and menu_weight < 2:
                        # Checks to see if Cursor Sprite is on last selection
                        # Calls Sprite to render down 1 selection
                        menu_weight += 1
                        print (menu_weight)
                        print('KeyHandler: Down key was pressed in the menu screen')
                    elif event.key == pygame.K_UP and menu_weight > 0:
                        # Checks to see if Cursor Sprite is on the top selection
                        # Calls Sprite to render up 1 selection
                        menu_weight -= 1
                        print('KeyHandler: Up key was pressed in the menu screen')
                    elif event.key == pygame.K_RETURN:
                        # Checks to see which selection the Cursor Sprite is on
                        # Calls Reader or  Credits or Exits render event
                        if menu_weight == 0:
                            self.reader_screen = True
                            print('Enter key was pressed in the menu screen on Activation')
                        elif menu_weight == 1:
                            self.credit_screen = True
                            print('Enter key was pressed in the menu screen on Credits')
                        elif menu_weight == 2:
                            print('Enter key was pressed in the menu screen on Exit')
                            run = False
                            pygame.quit()
                            sys.exit('Done')
                        self.menu_screen = False

                # Credits Screen Key Handler
                if (self.credit_screen and event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        # Calls menu_screen render event
                        self.credit_screen = False
                        self.menu_screen = True

                # Reader Screen Key Handler
                if (self.reader_screen and event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_ESCAPE:
                        # Calls pause menu render event
                        self.reader_screen = False
                        self.pause_screen = True

                # Pause Screen Key Handler
                if (self.pause_screen and event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_RETURN:
                        #Bug? # Calls reader render event
                        self.pause_screen = False
                        self.reader_screen = True
                    elif event.key == pygame.K_ESCAPE:
                        # Calls menu render event
                        self.pause_screen = False
                        self.menu_screen = True

                # Exit Screen Key Handler
                if (self.exit_screen and event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_RETURN:
                        run = False
                        pygame.quit()
                    elif event.key == pygame.K_ESCAPE:
                        # Calls menu render event
                        self.exit_screen = False
                        self.menu_screen = True

                all_sprites.update()

            if self.title_screen:

                window.blit(title_screen_png,(0,0))

            elif self.menu_screen:
                if menu_weight == 0:
                    window.blit(menu_screen_activate_png, (0,0))
                elif menu_weight == 1:
                    window.blit(menu_screen_credits_png, (0,0))
                elif menu_weight == 2:
                    window.blit(menu_screen_exit_png, (0,0))
            elif self.reader_screen:
                window.blit(reader_screen_png, (0,0))
            elif self.credit_screen:
                window.blit(credits_screen_png, (0,0))
            elif self.pause_screen:
                window.blit(pause_screen_png, (0,0))


            all_sprites.draw(window)
            pygame.display.flip()
            pygame.display.update()


        self.story.end()
        pygame.quit()

# ----------------------------------------------------------------------
# Excutable
# ----------------------------------------------------------------------

if __name__ == "__main__":
    app1 = app()
    app1.cli_arg(sys.argv[1:])

    app1.Machine_Loop()
