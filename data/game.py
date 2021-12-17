#from menu import Main_Menu
from data.menu import *
from moviepy.editor import *
from data.Ch115.lib.archive import *
from data.f1 import *
from data.f2 import *
from data.f3 import *
from data.f4 import *
from data.f5 import *
from data.f6 import *

class Initiating():

    def __init__(self):
        self.arquivo = 'c:\ProtTech\data\data.txt'
        self.a = open(self.arquivo, 'at')
        self.a2 = open(self.arquivo, 'rt+')

    def play(self):
        pygame.display.set_caption('Hello World!')

        clip = VideoFileClip('data/img/Prot Tech.mp4')
        clip.preview()

    def initiate(self):
        if not arch_Exists(self.arquivo):
            create_Archive(self.arquivo)
            self.a.write('False;\nScore=0;\nFasesWone=True,False,False,False,False,False,False;')
            self.a.close()

        try:
            s = open(self.arquivo, 'r').readlines()[0]
        except:
            self.a.write('False;\nScore=0;\nFasesWone=False,False,False,False,False,False,False;')
            self.a.close()

        s = self.a2.readlines()[0]
        if 'False;' in s:
            self.play()
            self.a2.close()

        a = open(self.arquivo, 'r')
        b = a.read()
        if 'False' in s:
            b = b.replace("False", "True",1)

        a = open(self.arquivo, 'w')
        a.truncate(0)
        a.write(b)
        a.close()


class Game():

    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.SPACE_KEY, self.ESC_KEY, self.RIGHT_KEY, self.LEFT_KEY = False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 957, 510
        self.clicking = 0
        #self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.display = pygame.image.load('data/img/fundo.png')
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        #self.logo = pygame.display.set_mode((400, 400))
        #self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = Main_Menu(self)
        self.options = Options_Menu(self)
        self.credits = Credits_Menu(self)
        self.fases = Fases(self)
        self.fases_1 = World_01(self)
        self.fase1world1 = FaseOneWorldOne(self)
        self.fase2world1 = FaseTwoWorldOne(self)
        self.fase3world1 = FaseThreeWorldOne(self)
        self.fase4world1 = FaseFourWorldOne(self)
        self.fase5world1 = FaseFiveWorldOne(self)
        self.fase6world1 = FaseSixWorldOne(self)
        #self.question = Questions(self)
        #self.fase_one_world_one = FaseOneWorldOne()
        self.current_menu = self.main_menu
        self.mainClock = pygame.time.Clock()
        self.ok_sound = False

    def game_loop(self):
        while self.playing:
            self.run_display = True
            self.check_events()
            if self.SPACE_KEY:
                self.playing = False
            self.display = pygame.image.load('data/img/fundo_2.png')
            #self.display.fill((255, 0, 0))
            #self.draw_text('Vamos ver se funciona', 20, int(self.DISPLAY_W/2), int(self.DISPLAY_H/2))
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.reset_keys()
            self.mainClock.tick(60)

    def check_events(self):
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.current_menu.run_display = False
                #arquivo = arquivo.replace('False', 'True', 1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.SPACE_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESC_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
            if event.type == MOUSEBUTTONDOWN:
                if 593 > mx > 393 and 464 > my > 280:
                    if event.button == 1:
                        self.ok_sound = True
            if event.type == MOUSEBUTTONUP:
                self.ok_sound = False
            #if event.type == MOUSEBUTTONDOWN:
             #   if event.button == 1 and self.clicking == 0:
              #      self.clicking = 1
               # if event.button == 1 and self.clicking == 2:
                #    self.clicking = 0
                #PARA O BOTÃO DIREITO
                #if event.button == 3:
                #    right_clicking = True
           # if event.type == MOUSEBUTTONUP:
            #    if event.button == 1 and clicking == 1:
             #       clicking = 2

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.ESC_KEY, self.SPACE_KEY, self.RIGHT_KEY, self.LEFT_KEY = False, False, False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        #text_rect.center = (x, y)
        text_rect.x = x
        text_rect.y = y
        self.display.blit(text_surface, text_rect)

    def draw_score(self):
        a2 = open('c:\ProtTech\data\data.txt', 'rt+')
        s = a2.readlines()[1]
        c = False
        text = ""
        for i in range(0, len(s)):
            if s.index('=') < i:
                text += s[i]
        kk = ""
        for i in range(0, len(text) -2):
            kk += text[i]
        font = pygame.font.Font('data/font/TECHNOID.TTF', 40)
        if self.current_menu != self.fase1world1 and self.current_menu != self.fase2world1 and self.current_menu !=  self.fase3world1 and self.current_menu !=  self.fase4world1 and self.current_menu !=  self.fase5world1 and self.current_menu !=  self.fase6world1:
            text_surface = font.render(f"Pontuação: {kk}", True, (255, 255, 255))
        else:
            text_surface = font.render(f"{kk}", True, (128, 128, 128))
            c = True
        text_rect = text_surface.get_rect()
        text_rect.x = 545
        text_rect.y = 45
        if c:
            text_rect.x = 860
            text_rect.y = 20
        self.display.blit(text_surface, text_rect)
        a2.close()




