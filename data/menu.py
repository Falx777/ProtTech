import pygame


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 50, 50)
        self.offset = -100
        self.bx, self.by = 598, self.mid_h - 204

    def draw_cursor(self):
        #O x do self.cursor_rect.x vem do primeiro zero do pygame.Rect(0, 0, 50, 50)
        #self.game.draw_text('->', 21, self.cursor_rect.x, self.cursor_rect.y)
        self.game.display.blit(pygame.image.load('data/img/Bar.png'), (self.bx, self.by))

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class Main_Menu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "começar"
        self.area = dict()
        #Start:
        self.area['1'] = {'x': 598, 'y': self.mid_h - 204}
        #Option:
        self.area['2'] = {'x': 598, 'y': self.mid_h - 64}
        #credits:
        self.area['3'] = {'x': 598, 'y': self.mid_h + 76}
        self.cursor_rect.midtop = (self.area['1']['x'], self.area['1']['y'])

    def display_m(self):
        self.run_display = True
        #background_song = pygame.mixer.music.load('aud/soundtrack.mp3')
        #pygame.mixer.music.play(loops=-1)
        #pygame.mixer.music.set_volume(0.04)
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display = pygame.image.load('data/img/fundo.png')
            self.game.display.blit(pygame.image.load('data/img/Prot Tech.png'), (30, 40))
            self.game.display.blit(pygame.image.load('data/img/INIC.png'), (600, self.mid_h - 200))
            self.game.display.blit(pygame.image.load('data/img/CONF.png'), (600, self.mid_h - 60))
            self.game.display.blit(pygame.image.load('data/img/SOBR.png'), (600, self.mid_h + 80))
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "começar":
                self.bx, self.by = self.area['2']['x'], self.area['2']['y']
                self.state = "opções"
            elif self.state == "opções":
                self.bx, self.by = self.area['3']['x'], self.area['3']['y']
                self.state = "sobre"
            elif self.state == "sobre":
                self.bx, self.by =self.area['1']['x'], self.area['1']['y']
                self.state = "começar"
        if self.game.UP_KEY:
            if self.state == "começar":
                self.bx, self.by = self.area['3']['x'], self.area['3']['y']
                self.state = "sobre"
            elif self.state == "opções":
                self.bx, self.by =self.area['1']['x'], self.area['1']['y']
                self.state = "começar"
            elif self.state == "sobre":
                self.bx, self.by = self.area['2']['x'], self.area['2']['y']
                self.state = "opções"

    def check_input(self):
        self.move_cursor()
        if self.game.SPACE_KEY:
            if self.state == "começar":
                #self.game.playing = True
                self.game.current_menu = self.game.fases
            elif self.state == "opções":
                self.game.current_menu = self.game.options
            elif self.state == "sobre":
                self.game.current_menu = self.game.credits
            self.run_display = False
        pygame.display.update()


class Options_Menu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        #self.state = 'volume'
        #self.vol_x, self.vol_y = self.mid_w, self.mid_h - 50
        #self.controls_x, self.controls_y = self.mid_w, self.mid_h
        #self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)
        self.state = "primeira"
        self.area = dict()
        self.area['1'] = {'x': 48, 'y': 41}
        self.area['2'] = {'x': 48, 'y': 226}
        self.cursor_rect.midtop = (self.area['1']['x'], self.area['1']['y'])
        self.visual_vol = list()
        self.visual_vol = ['I', 'I', 'I', 'I']
        self.volume = 0.04
        self.up_acc, self.down_acc = 0.00, 0.00

    def draw_cursor(self):
        self.game.display.blit(pygame.image.load('data/img/Bar_2.png'), self.cursor_rect.midtop)

    def move_cursors(self):
        if self.game.ESC_KEY:
            self.game.current_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == "primeira":
                self.state = "segunda"
                self.cursor_rect.midtop = (self.area['2']['x'], self.area['2']['y'])
            elif self.state == "segunda":
                self.state = "primeira"
                self.cursor_rect.midtop = (self.area['1']['x'], self.area['1']['y'])
        #if self.game.SPACE_KEY:
        self.up_acc = 0
        self.down_acc = 0

        if self.state == "primeira":
            if self.game.RIGHT_KEY and len(self.visual_vol) < 10:
                self.up_acc += 0.01
                self.visual_vol.append('I')
            if self.game.LEFT_KEY and (len(self.visual_vol)) >= 1:
                self.down_acc -= 0.01
                self.visual_vol.pop()
            self.volume += self.up_acc + self.down_acc
            vol = ''
            for v in self.visual_vol:
                vol += "   " + v
            self.game.display.blit(pygame.image.load('data/img/VOLUME.png'), (0, 0))
            self.game.draw_text(vol, 40, 50, 140)
            pygame.mixer.Channel(0).set_volume(self.volume)
        if self.state == "segunda":
            self.game.display.blit(pygame.image.load('data/img/CONFIG_2.png'), (0, 0))
            #self.game.display = pygame.image.load('data/img/CONFIG_2.png')

    def check_inputs(self):
        self.move_cursors()
        pygame.display.update()

                #para dar funcionalidade às opções caso sejam selecionadas

    def display_m(self):
        self.run_display = True
        while self.run_display:
            self.game.display = pygame.image.load('data/img/fundo.png')
            self.game.display.blit(pygame.image.load('data/img/CONFIG.png'), (0, 0))
            self.game.check_events()
            self.check_inputs()
            #self.game.draw_text("Opções:", 21, self.mid_w, self.mid_h - 100)
            #self.game.draw_text("Volume", 21, self.vol_x, self.vol_y)
            #self.game.draw_text("Controles", 21, self.controls_x, self.controls_y)
            #self.draw_cursor()
            self.draw_cursor()
            self.game.draw_score()
            self.blit_screen()


class Credits_Menu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_m(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.SPACE_KEY or self.game.ESC_KEY:
                self.game.current_menu = self.game.main_menu
                self.run_display = False
            self.game.display = pygame.image.load('data/img/fundo.png')
            self.game.draw_text("CREDITOS", 31, self.mid_w - 70, self.mid_h -200)
            #self.game.draw_text("Prot Tech, projeto de conclusão de curso chato para caramba. \nIsso tomou muito do meu tempo, \nentão tenta aproveitar!", 21, 50, self.mid_h)
            self.game.draw_text("Prot Tech", 21, 50, self.mid_h - 75)
            self.game.draw_text("Este programa faz parte de um projeto da disciplina de Projeto de", 21, 50, self.mid_h -25 )
            self.game.draw_text("Conclusão de Curso do Instituto Federal Sertão Pernambucano", 21, 50, self.mid_h)
            self.game.draw_text("Campus Petrolina.", 21, 50, self.mid_h + 25)
            self.game.draw_text("O projeto foi feito com o intuito de criar um programa em python", 21, 50, self.mid_h + 50)
            self.game.draw_text("que possa Ensinar de maneira interativa os princípios e práticas", 21, 50, self.mid_h + 75)
            self.game.draw_text("de manutenção e segurança em diferentes áreas de informática.", 21, 50, self.mid_h + 100)
            self.game.draw_text("Elaborador do projeto: Luiz Filipe de Almeida Xavier.", 21, 50, self.mid_h + 200)


            self.blit_screen()


class Fases(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "primeira"
        self.area = dict()
        self.area['1'] = {'x': 42, 'y': 151}
        self.area['2'] = {'x': 373, 'y': 143}
        self.area['3'] = {'x': 690, 'y': 144}
        self.bx, self.by = self.area['1']['x'], self.area['1']['y']
        #self.cursor_rect.midtop = (self.area['1']['x'], self.area['1']['y'])

    '''def check_input(self):
        self.Menu.move_cursor()
        if self.game.START_KEY:
            if self.state == "começar":
                self.game.playing = True
            elif self.state == "opções":
                self.game.current_menu = self.game.fases
            elif self.state == "sobre":
                self.game.current_menu = self.game.credits
            self.run_display = False
        pygame.display.update()
'''
    def draw_cursor(self):
        self.game.display.blit(pygame.image.load('data/img/Cir.png'), (self.bx, self.by))

    def move_cursor(self):
        if self.game.RIGHT_KEY:
            if self.state == "primeira":
                self.bx, self.by = self.area['2']['x'], self.area['2']['y']
                self.state = "segunda"
            elif self.state == "segunda":
                self.bx, self.by = self.area['3']['x'], self.area['3']['y']
                self.state = "terceira"
            elif self.state == "terceira":
                self.bx, self.by =self.area['1']['x'], self.area['1']['y']
                self.state = "primeira"
        if self.game.LEFT_KEY:
            if self.state == "primeira":
                self.bx, self.by = self.area['3']['x'], self.area['3']['y']
                self.state = "terceira"
            elif self.state == "segunda":
                self.bx, self.by =self.area['1']['x'], self.area['1']['y']
                self.state = "primeira"
            elif self.state == "terceira":
                self.bx, self.by = self.area['2']['x'], self.area['2']['y']
                self.state = "segunda"

    def check_inputs(self):
        self.move_cursor()
        if self.game.SPACE_KEY:
            if self.state == "primeira":
                # self.game.playing = True
                self.game.current_menu = self.game.fases_1
            self.run_display = False
        if self.game.ESC_KEY:
            self.game.current_menu = self.game.main_menu
            self.run_display = False
            self.state = "primeira"
            self.bx, self.by = self.area['1']['x'], self.area['1']['y']
        pygame.display.update()

    def display_m(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_inputs()
            self.game.display = pygame.image.load('data/img/fundo_2.png')
            self.draw_cursor()
            self.blit_screen()


class World_01(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "1"
        self.area = dict()
        self.area['1'] = {'x': 226, 'y': 36}
        self.area['2'] = {'x': 416, 'y': 36}
        self.area['3'] = {'x': 597, 'y': 36}
        self.area['4'] = {'x': 226, 'y': 198}
        self.area['5'] = {'x': 416, 'y': 198}
        self.area['6'] = {'x': 597, 'y': 198}
        self.area['7'] = {'x': 416, 'y': 364}
        self.bx, self.by = self.area['1']['x'], self.area['1']['y']

    def draw_cursor(self):
        self.game.display.blit(pygame.image.load('data/img/Bar_3.png'), (self.bx, self.by))

    def move_cursor(self):
        if self.game.RIGHT_KEY:
            if self.state == "1":
                self.bx, self.by = self.area['2']['x'], self.area['2']['y']
                self.state = "2"
            elif self.state == "2":
                self.bx, self.by = self.area['3']['x'], self.area['3']['y']
                self.state = "3"
            elif self.state == "3":
                self.bx, self.by = self.area['4']['x'], self.area['4']['y']
                self.state = "4"
            elif self.state == "4":
                self.bx, self.by = self.area['5']['x'], self.area['5']['y']
                self.state = "5"
            elif self.state == "5":
                self.bx, self.by = self.area['6']['x'], self.area['6']['y']
                self.state = "6"
            elif self.state == "6":
                self.bx, self.by = self.area['7']['x'], self.area['7']['y']
                self.state = "7"
            elif self.state == "7":
                self.bx, self.by = self.area['1']['x'], self.area['1']['y']
                self.state = "1"
        if self.game.LEFT_KEY:
            if self.state == "1":
                self.bx, self.by = self.area['7']['x'], self.area['7']['y']
                self.state = "7"
            elif self.state == "2":
                self.bx, self.by = self.area['1']['x'], self.area['1']['y']
                self.state = "1"
            elif self.state == "3":
                self.bx, self.by = self.area['2']['x'], self.area['2']['y']
                self.state = "2"
            elif self.state == "4":
                self.bx, self.by = self.area['3']['x'], self.area['3']['y']
                self.state = "3"
            elif self.state == "5":
                self.bx, self.by = self.area['4']['x'], self.area['4']['y']
                self.state = "4"
            elif self.state == "6":
                self.bx, self.by = self.area['5']['x'], self.area['5']['y']
                self.state = "5"
            elif self.state == "7":
                self.bx, self.by = self.area['6']['x'], self.area['6']['y']
                self.state = "6"

    def check_inputs(self):
        self.move_cursor()
        data = open('c:\ProtTech\data\data.txt', 'rt+')
        s = data.readlines()[2]
        text = 'FasesWone='
        if self.game.ESC_KEY:
            self.game.current_menu = self.game.fases
            self.bx, self.by = self.area['1']['x'], self.area['1']['y']
            self.state = '1'
            self.run_display = False
        if self.game.SPACE_KEY:
            if self.state == "1":
                if (text + 'True,') in s:
                #self.fade()
                    self.game.current_menu = self.game.fase1world1
                    self.run_display = False
                    data.close()
                #ENTRANDO NA FASE 1
                #self.game.current_menu = nome da fase
            elif self.state == "2":
                if (text + 'True,True') in s:
                    self.game.current_menu = self.game.fase2world1
                    self.run_display = False
                    data.close()
            elif self.state == "3":
                if (text + 'True,True,True') in s:
                    self.game.current_menu = self.game.fase3world1
                    self.run_display = False
                    data.close()
            elif self.state == "4":
                if (text + 'True,True,True,True') in s:
                    self.game.current_menu = self.game.fase4world1
                    self.run_display = False
                    data.close()
            elif self.state == "5":
                if (text + 'True,True,True,True,True') in s:
                    self.game.current_menu = self.game.fase5world1
                    self.run_display = False
                    data.close()
            elif self.state == "6":
                if (text + 'True,True,True,True,True,True') in s:
                    self.game.current_menu = self.game.fase6world1
                    self.run_display = False
                    data.close()
            elif self.state == "7":
                # ENTRANDO NA FASE 1
                # self.game.current_menu = nome da fase
                pass
        pygame.display.update()

    def display_m(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_inputs()
            self.game.display = pygame.image.load('data/img/MUNDO_1_FASES.png')
            self.draw_cursor()
            self.blit_screen()

