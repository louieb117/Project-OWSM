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


class Menu_Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 10))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.menu_count = 0
        self.event = pygame.K_CLEAR
        self.position_s0_x = 0
        self.position_s0_y = 0
        self.position_s1_x = 0
        self.position_s1_y = 0
        self.position_s2_x = 0
        self.position_s2_y = 0



    def get_event_key(self, EventType):
        self.event = EventType

    def check_selection(self, menu_count):
        return menu_count

    def move_cursor(self, menu_count):
        if menu_count == 0:
            self.rect.move_ip((self.position_s0_x, self.position_s0_y))
        elif menu_count == 1:
            self.rect.move_ip((self.position_s1_x, self.position_s1_y))
        elif menu_count == 2:
            self.rect.move_ip((self.position_s2_x, self.position_s2_y))

    def update(self):
        if not self.event:
            return
        elif (self.event == pygame.K_DOWN and self.menu_count < 2):
            self.menu_count + 1
            move_cursor(self.menu_count)

        elif (self.event == pygame.K_UP and self.menu_count > 0):
            self.menu_count - 1
            move_cursor(self.menu_count)

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

        title_screen_img = pygame.image.load('images/Title_Screen.png')
        title_screen_img = pygame.transform.scale(title_screen_img, (self.WIDTH, self.HEIGHT))
        #menu_screen_img = pygame.image.load('images/test_msi.jpg')
        #menu_screen_img = pygame.transform.scale(menu_screen_img, (self.WIDTH, self.HEIGHT))
        #reader_screen_img = pygame.image.load('images/test_rsi.jpg')
        #reader_screen_img = pygame.transform.scale(reader_screen_img, (self.WIDTH, self.HEIGHT))
        #credits_screen_img = pygame.image.load('images/test_csi.jpg')
        #credits_screen_img = pygame.transform.scale(credits_screen_img, (self.WIDTH, self.HEIGHT))

        #pause_screen_img = pygame.image.load('Images/test_psi.jpg')
        #pause_screen_img = pygame.transform.scale(pause_screen_img, (self.WIDTH, self.HEIGHT))

        clock = pygame.time.Clock()
        run = self.run_state
        FPS = 60
        #self.story = Interdimensional_Story_Reader(self.file_name, self.number)

        all_sprites = pygame.sprite.Group()
        board = Board(500, 500)
        text_cursor = Text_Cursor(board)
        menu_cursor = Menu_Cursor()
        all_sprites.add(text_cursor, board, menu_cursor)

        text = self.story
        text_cursor.write(text)

        while run:
            clock.tick(FPS)
            if FPS%60: print(time.clock())

            for event in pygame.event.get():

                # Exits program if window is closed
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                # Title Screen Key Handler
                if (self.title_screen & event.type == pygame.KEYDOWN):
                    print('Image Copy')
                    if event.key == pygame.K_ENTER:
                        # Calls Menu screen render event
                        print('Enter key was pressed in the Title Screen')
                        self.title_screen = False
                        self.menu_screen = True

                # Menu Screen Key Handler
                if (self.menu_screen & event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_DOWN:
                        # Checks to see if Cursor Sprite is on last selection
                        # Calls Sprite to render down 1 selection
                        menu_cursor.get_event_key(event.key)
                    elif event.key == pygame.K_UP:
                        # Checks to see if Cursor Sprite is on the top selection
                        # Calls Sprite to render up 1 selection
                        menu_cursor.get_event_key(event.key)
                    elif event.key == pygame.K_ENTER:
                        # Checks to see which selection the Cursor Sprite is on
                        # Calls Reader or  Credits or Exits render event
                        if menu_cursor.check_selection() == 0:
                            self.reader_screen = True
                        elif menu_cursor.check_selection() == 1:
                            self.credit_screen = True
                        elif menu_cursor.check_selection() == 2:
                            run = False
                            pygame.quit()
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
                        self.reader_screen = False
                        self.pause_screen = True

                # Pause Screen Key Handler
                if (self.pause_screen & event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_ENTER:
                        #Bug? # Calls reader render event
                        self.pause_screen = False
                        self.reader_screen = True
                    elif event.key == pygame.K_ESCAPE:
                        # Calls menu render event
                        self.pause_screen = False
                        self.menu_screen = True

                # Exit Screen Key Handler
                if (self.exit_screen & event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_ENTER:
                        run = False
                        pygame.quit()
                    elif event.key == pygame.K_ESCAPE:
                        # Calls menu render event
                        self.exit_screen = False
                        self.menu_screen = True

            all_sprites.update()

            if self.title_screen:

                window.blit(title_screen_img,(0,0))

            elif self.menu_screen:
                window.blit(menu_screen_img, (0,0))
            elif self.reader_screen:
                window.blit(reader_screen_img, (0,0))
            elif self.credit_screen:
                window.blit(credits_screen_img, (0,0))
            elif self.pause_screen:
                window.blit(pause_screen_img, (0,0))


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
