import pygame, time
from data.score import *
from pygame.locals import *
from data.questions import *


class Fases3():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 50, 50)
        self.test = 0
        self.margin_left = 41
        self.margin_right = 130
        self.y_text = 366
        self.font_size = 21
        self.ok = False
        self.gamimg_layer = False


class FaseThreeWorldOne(Fases3):
    def __init__(self, game):
        self.i = 1
        self.layers = [1]
        self.not_fading = True
        self.wrong, self.wright = False, False
        self.score = Score()
        self.margin_reg = "right"
        self.area = dict()
        self.state = "1"
        #self.area['1'] = {'x': 53, 'y': 145}
        #self.area['2'] = {'x': 359, 'y': 145}
        #self.area['3'] = {'x': 664, 'y': 145}
        #self.bx, self.by = self.area['1']['x'], self.area['1']['y']
        self.answer = dict()
        self.answer = {'29': 1, '30': 1,'41':1, '47':1, '64':1, '70': 1}
        self.clicking = 0
        self.q = QuestionsThree(0)
        self.right_clicking = False
        self.n, self.count = 0, 0
        self.click_event = False
        self.count_click = 0
        self.sheet_event = [False, False, False]
        self.finish = False
        self.clock = 0
        self.csr = False
        self.font = ""
        self.count_select = [[False, False, False], [False, False, False, False]]
        self.slide = [True,False,False]
        self.mouse_psi = {'4p':[(0,149), False], '16p':[(153,0), False], '24p': [(0,249), False], 'sata':[(-23,-60),False], 'tmd':[(645, 320),False], 'tmd2':[(650, 323),False]}
        self.cabos = {'4p': [(479, 0), False], '16p':[(743, 263),False], '24p':[(909,0),False], 'sata':[(507,373),False], 'tmd':[(645,310), False], 'tmd2':[(645,320), False], 'tmd3': [False,False]}
        self.slide2 = [True,False,False]
        self.q2 = {'placa1': [(136, 348), False], 'placa2':[(590, 356),False], 'placa3':[(226,185),False,False]}
        self.sheet = [False, False, False, False]
        Fases3.__init__(self, game)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

    def draw_bar(self):
        self.game.display.blit(pygame.image.load('data/img/Barra-Diálogo.png'), (0, 0))

    def draw_button(self):
        if self.ok:
            pygame.time.delay(300)
            self.game.display.blit(pygame.image.load('data/img/ok_02.png'), (844, 442))
            self.ok = False
        else:
            self.game.display.blit(pygame.image.load('data/img/ok_01.png'), (844, 442))

    def draw_cursor(self):
        self.game.display.blit(pygame.image.load('data/img/Bar_4.png'), (self.bx, self.by))
        if self.wrong:
            self.game.display.blit(pygame.image.load('data/img/Bar_4_r.png'), (self.bx, self.by))

    def draw_very_good(self):
        self.game.display.blit(pygame.image.load('data/img/Very_good.png'), (0, 0))

    #def check_events(self):
        #for event in pygame.event.get():
        #    pass

    def fade(self, seconds, rng):
        fade = pygame.image.load('data/img/Transp.png')
        for alpha in range(0, rng):
            fade.set_alpha(alpha)
            self.blit_screen()
            self.game.window.blit(fade, (0, 0))
            pygame.time.delay(seconds)

    def move_cursor(self):
        pass

    def draw_logan(self, sprite):
        logan_sprite = ''
        if sprite == 1:
            logan_sprite = 'data/img/Logan/S1.png'
            self.margin_reg = "right"
        elif sprite % 2 == 0 and sprite % 3 != 0 and sprite % 5 != 0 and sprite % 7 != 0:
            logan_sprite = 'data/img/Logan/S1.png'
            self.margin_reg = "right"
        elif sprite % 3 == 0 and sprite % 2 != 0 and sprite % 5 != 0 and sprite % 7 != 0:
            logan_sprite = 'data/img/Logan/S2.png'
            self.margin_reg = "right"
        elif sprite % 5 == 0 and sprite % 2 != 0 and sprite % 3 != 0 and sprite % 7 != 0:
            logan_sprite = 'data/img/Logan/S3.png'
            self.margin_reg = "left"
        elif sprite % 7 == 0 and sprite % 2 != 0 and sprite % 3 != 0 and sprite % 5 != 0:
            logan_sprite = 'data/img/Logan/S4.png'
            self.margin_reg = "left"
        elif sprite % 2 == 0 and sprite % 3 == 0 and sprite % 5 != 0 and sprite % 7 != 0:
            logan_sprite = 'data/img/Logan/S5.png'
            self.margin_reg = "right"
        elif sprite % 2 == 0 and sprite % 3 == 0 and sprite % 5 == 0 and sprite % 7 != 0:
            logan_sprite = 'data/img/Logan/S6.png'
            self.margin_reg = "left"
        elif sprite % 2 == 0 and sprite % 3 == 0 and sprite % 5 == 0 and sprite % 7 == 0:
            logan_sprite = 'data/img/Logan/S7.png'
            self.margin_reg = "right"
        elif sprite % 3 == 0 and sprite % 2 != 0 and sprite % 5 == 0 and sprite % 7 != 0:
            logan_sprite = 'data/img/Logan/S2.png'
            self.margin_reg = " right"
        elif sprite % 3 == 0 and sprite % 2 != 0 and sprite % 5 == 0 and sprite % 7 == 0:
            logan_sprite = 'data/img/Logan/S3.png'
            self.margin_reg = "left"
        elif sprite % 5 == 0 and sprite % 2 != 0 and sprite % 3 != 0 and sprite % 7 == 0:
            logan_sprite = 'data/img/Logan/S4.png'
            self.margin_reg = "left"
        else:
            logan_sprite = 'data/img/Logan/S1.png'
            self.margin_reg = "right"
        self.game.display.blit(pygame.image.load(logan_sprite), (0, 0))

    def check_inputs(self):
        self.move_cursor()
        if self.game.ESC_KEY:
            #if not self.gamimg_layer:
            self.q = QuestionsThree(0)
            self.game.current_menu = self.game.fases_1
            self.run_display = False
            self.gaming_layer = False
            self.game.reset_keys()
            self.state = '1'
            self.layers.clear()
            self.i = 1
            self.layers.append(1)
        if self.game.SPACE_KEY:
            if not self.gamimg_layer and self.layers[len(self.layers) - 1] != 150:
                self.i += 1
                self.layers.append(self.i)
                self.ok = True
                self.clock = 0
            if not self.gamimg_layer and self.layers[len(self.layers) - 1] == 113:
                self.game.current_menu = self.game.fases_1
                self.run_display = False
                self.gaming_layer = False
                self.game.reset_keys()
                self.layers.clear()
                self.i = 1
                self.layers.append(1)
        pygame.display.update()

    def base_layer(self, layer):
        self.draw_bar()
        self.draw_logan(layer)
        if self.not_fading:
            self.fade(1, 10)
            self.not_fading = False
        self.draw_button()

    def first_question(self, font):
        self.game.display = pygame.image.load('data/img/worlds/w1/s1/Fundo.png')
        mx, my = pygame.mouse.get_pos()

        if self.slide[0]:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/ssd.png'), (463,165))
        elif self.slide[1]:
            if not self.mouse_psi['tmd'][1] and not self.cabos['tmd'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/tmd.png'), self.cabos['tmd'][0])
            if not self.mouse_psi['tmd2'][1] and not self.cabos['tmd2'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/tmd2.png'), self.mouse_psi['tmd2'][0])
            if self.cabos['tmd3'][0] and self.cabos['tmd3'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/tmd3.png'), self.mouse_psi['tmd'][0])
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/mesa.png'), (505, 44))
        elif self.slide[2]: 
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/motherboard.png'), (369,1))

        self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/setas.png'), (445,226))

        if self.slide[1]:
            if (687 > mx > 646 and 437 > my > 379) and self.clicking == 1:
                self.cabos['tmd3'][0] = True
        if self.cabos['tmd3'][0]:
            if (691 > mx > 650 and 367 > my > 309) and self.clicking == 1:
                self.cabos['tmd3'][1] = True
                self.mouse_psi['tmd2'][1] = True

        if self.cabos['tmd3'][0] and self.cabos['tmd3'][1] and self.cabos['4p'][1] and self.cabos['16p'][1] and self.cabos['24p'][1] and self.cabos['sata'][1]:
            if (815 > mx > 792 and 287 > my > 261) and self.clicking == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/ligando.png'), (557, 44))
                self.count_click += 1
            if self.count_click == 10:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.i += 1
                self.layers.append(self.i)
                self.gamimg_layer = False
                self.game.reset_keys()
                self.score.count = 0
                self.score.scr = 0
                self.score.alternatives(1, 1)
                self.slide[0], self.slide[1], self.slide[2] = True, False, False

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and self.clicking == 0:
                    self.clicking = 1
                if event.button == 1 and self.clicking == 2:
                    self.clicking = 0
                    if not (512 > mx > 483 and 101 > my > 68):
                        self.mouse_psi['4p'][1] = False
                    if not (957 > mx > 743 and 335 > my > 263):
                        self.mouse_psi['16p'][1] = False
                    if not (944 > mx > 915 and 155 > my > 24):
                        self.mouse_psi['24p'][1] = False
                if event.button == 1 and ((498 > mx > 445 and 273 > my > 226) or (956 > mx > 903 and 273 > my > 226)):
                    if (498 > mx > 445 and 273 > my > 226):
                        self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/seta_e.png'), (445,226))
                        if self.slide[0]:
                            self.slide[0] = False
                            self.slide[2] = True
                        elif self.slide[1]:
                            self.slide[1] = False
                            self.slide[0] = True
                        elif self.slide[2]:
                            self.slide[2] = False
                            self.slide[1] = True
                    if (956 > mx > 903 and 273 > my > 226):
                        self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/seta_d.png'), (903,226))
                        if self.slide[0]:
                            self.slide[0] = False
                            self.slide[1] = True
                        elif self.slide[1]:
                            self.slide[1] = False
                            self.slide[2] = True
                        elif self.slide[2]:
                            self.slide[2] = False
                            self.slide[0] = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1 and self.clicking == 1:
                    self.clicking = 2

        if (948 > mx > 740 and 502 > my > 440) and self.clicking == 1:
            self.csr = False
            self.font = ""
            self.slide[0] = True
            self.slide[1] = False
            self.slide[2] = False
            self.mouse_psi['4p'][1] = False
            self.mouse_psi['16p'][1] = False
            self.mouse_psi['24p'][1] = False
            self.mouse_psi['sata'][1] = False
            self.mouse_psi['tmd'][1] = False
            self.mouse_psi['tmd2'][1] = False
            self.cabos['4p'][1] = False
            self.cabos['16p'][1] = False
            self.cabos['24p'][1] = False
            self.cabos['sata'][1] = False
            self.cabos['tmd'][1] = False
            self.cabos['tmd2'][1] = False
            self.cabos['tmd3'][1] = False
            self.cabos['tmd3'][0] = False

        if font == '300w':
            if not self.mouse_psi['24p'][1] and not self.cabos['24p'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/24pinos.png'), self.mouse_psi['24p'][0])
            if not self.mouse_psi['16p'][1] and not self.cabos['16p'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/16pinos.png'), self.mouse_psi['16p'][0])
            if not self.mouse_psi['4p'][1] and not self.cabos['4p'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/4pinos.png'), self.mouse_psi['4p'][0])
            if not self.mouse_psi['sata'][1] and not self.cabos['sata'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/sta.png'), self.mouse_psi['sata'][0])

            if self.slide[2]:
                #4pinos
                if (233 > mx > 131 and 302 > my > 199) and not self.mouse_psi['4p'][1] and self.clicking == 1:
                    self.mouse_psi['4p'][1] = True
                if self.mouse_psi['4p'][1] and not self.cabos['4p'][1] and not self.mouse_psi['24p'][1] and not self.mouse_psi['16p'][1] :
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/4pinos.png'), (mx - 220,my - 120))
                if (512 > mx > 483 and 101 > my > 68) and self.clicking == 1:
                    self.mouse_psi['4p'][1] = False
                    self.cabos['4p'][1] = True

                #16pinos
                if (420 > mx > 153 and 226 > my > 0) and not self.mouse_psi['16p'][1] and self.clicking == 1:
                    self.mouse_psi['16p'][1] = True
                if self.mouse_psi['16p'][1] and not self.cabos['16p'][1] and not self.mouse_psi['24p'][1] and not self.mouse_psi['4p'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/16pinos.png'), (mx - 190,my - 200))
                if (957 > mx > 743 and 335 > my > 263) and self.clicking == 1:
                    self.mouse_psi['16p'][1] = False
                    self.cabos['16p'][1] = True

                #24pinos
                if (304 > mx > 18 and 497 > my > 332) and not self.mouse_psi['24p'][1] and self.clicking == 1:
                    self.mouse_psi['24p'][1] = True
                if self.mouse_psi['24p'][1] and not self.cabos['24p'][1] and not self.mouse_psi['4p'][1] and not self.mouse_psi['16p'][1] :
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/24pinos.png'), (mx - 190, my - 200))
                if (944 > mx > 915 and 155 > my > 24) and self.clicking == 1:
                    self.mouse_psi['24p'][1] = False
                    self.cabos['24p'][1] = True

                if self.cabos['4p'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/cabo4.png'), self.cabos['4p'][0])
                    self.mouse_psi['4p'][1] = False

                if self.cabos['16p'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/cabo16.png'), self.cabos['16p'][0])
                    self.mouse_psi['16p'][1] = False

                if self.cabos['24p'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/cabo24.png'), self.cabos['24p'][0])
                    self.mouse_psi['24p'][1] = False

            if self.slide[0]:
                # sata
                if (170 > mx > 32 and 106 > my > 64) and not self.mouse_psi['sata'][1] and self.clicking == 1:
                    self.mouse_psi['sata'][1] = True
                if self.mouse_psi['sata'][1] and not self.cabos['sata'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/sta.png'), (mx - 80, my - 140))
                if (709 > mx > 507 and 407 > my > 364) and self.clicking == 1:
                    self.mouse_psi['sata'][1] = False
                    self.cabos['sata'][1] = True

                if self.cabos['sata'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/cabosata.png'), self.cabos['sata'][0])
                    self.mouse_psi['sata'][1] = False

        if font == "400w":
            if not self.mouse_psi['24p'][1] and not self.cabos['24p'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/24pinos.png'), self.mouse_psi['24p'][0])
            if not self.mouse_psi['16p'][1] and not self.cabos['16p'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/12pinos.png'), self.mouse_psi['16p'][0])
            if not self.mouse_psi['4p'][1] and not self.cabos['4p'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/6pinos.png'), self.mouse_psi['4p'][0])
            if not self.mouse_psi['sata'][1] and not self.cabos['sata'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/sta.png'), self.mouse_psi['sata'][0])

            if self.slide[2]:
                # 6pinos
                if (233 > mx > 131 and 302 > my > 199) and not self.mouse_psi['4p'][1] and self.clicking == 1:
                    self.mouse_psi['4p'][1] = True
                if self.mouse_psi['4p'][1] and not self.cabos['4p'][1] and not self.mouse_psi['24p'][1] and not \
                self.mouse_psi['16p'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/6pinos.png'), (mx - 220, my - 120))
                if (512 > mx > 483 and 101 > my > 68) and self.clicking == 1 and font == "300w":
                    self.mouse_psi['4p'][1] = False
                    self.cabos['4p'][1] = True

                # 12pinos
                if (420 > mx > 153 and 226 > my > 0) and not self.mouse_psi['16p'][1] and self.clicking == 1:
                    self.mouse_psi['16p'][1] = True
                if self.mouse_psi['16p'][1] and not self.cabos['16p'][1] and not self.mouse_psi['24p'][1] and not \
                self.mouse_psi['4p'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/12pinos.png'), (mx - 190, my - 200))
                if (957 > mx > 743 and 335 > my > 263) and self.clicking == 1 and font == "300w":
                    self.mouse_psi['16p'][1] = False
                    self.cabos['16p'][1] = True

                # 24pinos
                if (304 > mx > 18 and 497 > my > 332) and not self.mouse_psi['24p'][1] and self.clicking == 1:
                    self.mouse_psi['24p'][1] = True
                if self.mouse_psi['24p'][1] and not self.cabos['24p'][1] and not self.mouse_psi['4p'][1] and not \
                self.mouse_psi['16p'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/24pinos.png'), (mx - 190, my - 200))
                if (944 > mx > 915 and 155 > my > 24) and self.clicking == 1:
                    self.mouse_psi['24p'][1] = False
                    self.cabos['24p'][1] = True
                if font == "300w":
                    if self.cabos['4p'][1]:
                        self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/cabo4.png'), self.cabos['4p'][0])
                        self.mouse_psi['4p'][1] = False

                    if self.cabos['16p'][1]:
                        self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/cabo16.png'), self.cabos['16p'][0])
                        self.mouse_psi['16p'][1] = False

                if self.cabos['24p'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/cabo24.png'), self.cabos['24p'][0])
                    self.mouse_psi['24p'][1] = False

            if self.slide[0]:
                # sata
                if (170 > mx > 32 and 106 > my > 64) and not self.mouse_psi['sata'][1] and self.clicking == 1:
                    self.mouse_psi['sata'][1] = True
                if self.mouse_psi['sata'][1] and not self.cabos['sata'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/sta.png'), (mx - 80, my - 140))
                if (709 > mx > 507 and 407 > my > 364) and self.clicking == 1:
                    self.mouse_psi['sata'][1] = False
                    self.cabos['sata'][1] = True

                if self.cabos['sata'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/cabosata.png'), self.cabos['sata'][0])
                    self.mouse_psi['sata'][1] = False
                    # self.mouse_psi['4p'][1] = True

        self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/voltar.png'), (743,442))

    def selected_question(self):
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and self.clicking == 0:
                    self.clicking = 1
                if event.button == 1 and self.clicking == 2:
                    self.clicking = 0
            if event.type == MOUSEBUTTONUP:
                if event.button == 1 and self.clicking == 1:
                    self.clicking = 2
        for i in range(1, 8):
            if self.q.position[str(i)][1][0] > mx > self.q.position[str(i)][0][0] and self.q.position[str(i)][1][1] > my > self.q.position[str(i)][0][1]:
                if self.clicking == 1:
                    self.q.position[str(i)][2] = True

        for l in range(1, 8):
            if self.q.position[str(l)][2]:
                #if not self.q.position['8'][2]:
                self.game.display.blit(pygame.image.load(self.q.bar), (mx + self.q.offset[0], my + self.q.offset[1]))
                if (self.q.position['8'][1][0] > mx > self.q.position['8'][0][0] and self.q.position['8'][1][1] > my > self.q.position['8'][0][1]) and self.clicking == 1:
                    if self.q.answ[l - 1][1] != 0:
                        #self.q.position['8'][2] = True
                        self.q.position[str(l)][2] = False
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                        pygame.mixer.Channel(1).set_volume(0.04)
                        if self.q.lay == 48:
                            #self.q.position[str(l)][2] = False
                            if (self.q.answ[l - 1][0] == 2) and self.q.answ[l - 1][1] == 8 and not self.count_select[0][0]:
                                self.count_select[0][0] = True
                            if (self.q.answ[l - 1][0] == 4) and self.q.answ[l - 1][1] == 8 and not self.count_select[0][1]:
                                self.count_select[0][1] = True
                            if (self.q.answ[l - 1][0] == 6) and self.q.answ[l - 1][1] == 8 and not self.count_select[0][2]:
                                self.count_select[0][2] = True
                        if self.q.lay == 49:
                            self.q.position[str(l)][2] = False
                            if (self.q.answ[l - 1][0] == 1) and self.q.answ[l - 1][1] == 8 and not self.count_select[1][0]:
                                self.count_select[1][0] = True
                            if (self.q.answ[l - 1][0] == 3) and self.q.answ[l - 1][1] == 8 and not self.count_select[1][1]:
                                self.count_select[1][1] = True
                            if (self.q.answ[l - 1][0] == 5) and self.q.answ[l - 1][1] == 8 and not self.count_select[1][2]:
                                self.count_select[1][2] = True
                            if (self.q.answ[l - 1][0] == 7) and self.q.answ[l - 1][1] == 8 and not self.count_select[1][3]:
                                self.count_select[1][3] = True
                    else:
                        self.q.position[str(l)][2] = False
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/wrong_answer.mp3'))
                        pygame.mixer.Channel(1).set_volume(0.04)
        if self.q.lay == 48:
            if self.q.position['8'][2]:
                for i in range(1, 8):
                    self.game.display.blit(pygame.image.load(self.q.bar), self.q.position['8'][0])
                    self.q.position[str(i)][2] = True

            if self.count_select[0][1] and self.count_select[0][2] and self.count_select[0][0]:
                self.q = QuestionsThree(49)
                for i in range(1, 8):
                    self.q.position[str(i)][2] = False

        if self.count_select[1][1] and self.count_select[1][2] and self.count_select[1][0] and self.count_select[1][3]:
            self.count_select[1][1], self.count_select[1][2], self.count_select[1][0], self.count_select[1][3] = False, False, False, False
            self.i += 1
            self.layers.append(self.i)
            self.gamimg_layer = False
            self.game.reset_keys()
            self.score.count = 0
            self.score.scr = 0
            for i in range(0,3):
                self.score.alternatives(i, 2)

    def selected_question_2(self):
        mx, my = pygame.mouse.get_pos()
        loc = [mx, my]
        if self.clicking != 0:
            self.game.display.blit(pygame.image.load(self.q.bar),
                                   (loc[0] + self.q.offset[0], loc[1] + self.q.offset[1]))
        for j in range(0, len(self.q.feed)):
            if self.q.feed[j][1] != 0 and self.q.feed[j][0] != 0:
                self.game.display.blit(pygame.image.load(self.q.selected_bar),
                                       (self.q.position[str(self.q.feed[j][1])][0][0],
                                        self.q.position[str(self.q.feed[j][1])][0][1]))
        feed_zero = 0
        for i in range(0, len(self.q.feed)):
            if self.q.feed[i][1] != 0:
                feed_zero += 1
        if feed_zero == len(self.q.feed):
            for i in range(0, len(self.q.feed)):
                if self.q.feed[i][1] == self.q.answ[i][1]:
                    self.count += 1
            if self.count != len(self.q.feed):
                self.score.alternatives(1, 2)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/wrong_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.07)
                # self.feed = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
                for i in range(0, len(self.q.feed)):
                    for j in range(0, 2):
                        self.q.feed[i][j] = 0
                self.n, self.count = 0, 0
                pygame.time.wait(1650)
            if self.count == len(self.q.feed):
                for p in range(0, 2):
                    self.score.alternatives(p, 1)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.i += 1
                self.layers.append(self.i)
                self.gamimg_layer = False
                self.game.reset_keys()
                self.state = '1'
                self.score.count = 0
                self.score.scr = 0
            self.count = 0
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                k = 0
                l = 0
                for ds in range(0, len(self.q.feed)):
                    if self.q.feed[ds][0] == 0:
                        l += 1
                for i in range(1, len(self.q.feed) + 1):
                    for j in range(1, len(self.q.feed) + 1):
                        if j != i:
                            if self.q.position[str(j)][2]:
                                k += 1
                    if self.q.position[str(i)][1][0] > mx > self.q.position[str(i)][0][0] and \
                            self.q.position[str(i)][1][1] > my > \
                            self.q.position[str(i)][0][1] and k == 0 and l != 0:
                        self.q.position[str(i)][2] = True
                        if event.button == 1 and self.clicking == 0:
                            self.clicking = 1
                            self.n = i - 1
                            self.q.feed[self.n][0] = i
                for i in range(len(self.q.feed) + 1, len(self.q.position) + 1):
                    k = 0
                    for j in range(0, len(self.q.feed)):
                        if self.q.feed[j][1] == i:
                            k += 1
                    if self.q.position[str(i)][1][0] > mx > self.q.position[str(i)][0][0] and \
                            self.q.position[str(i)][1][1] > my > \
                            self.q.position[str(i)][0][1] and k == 0:
                        if event.button == 1 and self.clicking == 2:
                            self.clicking = 0
                            self.q.feed[self.n][1] = i
                            for j in range(1, len(self.q.feed) + 1):
                                self.q.position[str(j)][2] = False
                            self.n = 0
            if event.type == MOUSEBUTTONUP:
                if event.button == 1 and self.clicking == 1:
                    self.clicking = 2

    def run_layer(self, layer):
        if layer == 1:
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora que você terminou a fase 2, vamos dar continuidade ao ", self.font_size, x_text, self.y_text)
            self.game.draw_text("aprendizado sobre a placa-mãe.", self.font_size, x_text, self.y_text + 20)
        if layer == 2:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/conectores.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os outros conectores importantes para a placa-mãe são os que ", self.font_size, x_text, self.y_text)
            self.game.draw_text("ligam ela à fonte de energia e à unidade de armazenamento.", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("Primeiramente, falaremos sobre a fonte e seu conector.", self.font_size, x_text, self.y_text + 60)
        if layer == 3:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/fonte.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("A fonte de um computador é um componente essencial, pois ela é", self.font_size, 125, 415)
            self.game.draw_text("responsável por passar a energia da tomada direto para a placa-mãe ", self.font_size, 125, 435)
            self.game.draw_text("e outros hardwares ligados à ela. ", self.font_size, 125, 455)
        if layer == 4:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/ligar_diretamente.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Você deve estar se perguntando, por que não podemos ligar um cabo ", self.font_size, x_text, self.y_text)
            self.game.draw_text("direto da placa-mãe para a tomada? ", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("Bom, os dispositivos eletrônicos de um computador são feitos para", self.font_size, x_text, self.y_text + 40)
            self.game.draw_text("funcionarem em corrente contínua e a corrente elétrica que vem ", self.font_size, x_text, self.y_text + 60)
            self.game.draw_text("da tomada de um estabelecimento é alternada.", self.font_size, x_text, self.y_text + 80)
        if layer == 5:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/correntes.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para contornar esse problema, a fonte do computador converte a ",self.font_size, x_text, self.y_text)
            self.game.draw_text("corrente alternada em corrente contínua. ", self.font_size,x_text, self.y_text + 20)
        if layer == 6:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/fonte_ATX.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("As fontes atuais possuem o padrão ATX, sigla para Advanced ", self.font_size,251, self.y_text)
            self.game.draw_text("Technology eXtended. Esse padrão possui diferenças ao seu  ", self.font_size,251, self.y_text + 20)
            self.game.draw_text("antecessor, o AT, como o conector de 24 pinos para a placa-mãe.", self.font_size,251, self.y_text + 40)
        if layer == 7:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/fontes.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Devido à relativa simplicidade das operações de uma fonte, muitas ", 20, x_text, self.y_text)
            self.game.draw_text("vezes esse hardware é fabricado de modo que não possua segurança ", 20, x_text,self.y_text + 20)
            self.game.draw_text("ou suporte para manutenção e consequentemente possui um preço ", 20, x_text, self.y_text + 40)
            self.game.draw_text("menor (duas ou até três vezes menos) do que fontes de boa ", 20, x_text,self.y_text + 60)
            self.game.draw_text("qualidade com a mesma potência.", 20, x_text, self.y_text + 80)
        if layer == 8:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/fontes.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Esse tipo de fonte mais simples é chamada de fonte nominal ou genérica ", 20, x_text, self.y_text)
            self.game.draw_text("e a fonte especializada é chamada de fonte real.", 20, x_text,self.y_text + 20)
            self.game.draw_text("É preciso saber diferenciar uma fonte real de uma fonte nominal.", 20, x_text, self.y_text + 40)
        if layer == 9:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/fontes.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Primeiramente, uma fonte real possui um melhor acabamento  ", 20, 250, self.y_text)
            self.game.draw_text("do que uma fonte nominal. Seus materiais de construção são ", 20, 250,self.y_text + 20)
            self.game.draw_text("melhores e mais resistentes.", 20, 250,self.y_text + 40)
        if layer == 10:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/chaves_fonte.png'), (275, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Além disso, as fontes reais possuem chaves de liga e desliga e chave seletora ", 19, x_text, self.y_text)
            self.game.draw_text("de tensão. A maioria das fontes nominais não possuem essas duas chaves de vez,", 19, x_text, self.y_text + 20)
            self.game.draw_text("apenas a chave seletora de tensão.", 19, x_text, self.y_text + 40)
        if layer == 11:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/info_fonte.png'), (275, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Outra característica é que há adesivado ou escrito na fonte a potência a qual ela ", 19,x_text, self.y_text)
            self.game.draw_text("pode fornecer. As fontes nominais não fornecem a potência marcada no rótulo, já as", 19, x_text, self.y_text + 20)
            self.game.draw_text("fontes reais, sim. Então se uma fonte nominal com uma potência x for utilizada para", 19, x_text,self.y_text + 40)
            self.game.draw_text("um computador que requer minimamente essa potência x, ele não funcionará de  ", 19, x_text,self.y_text + 60)
            self.game.draw_text("maneira eficiente ou pode até não ligar.", 19, x_text,self.y_text + 80)
        if layer == 12:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/fogo.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Uma fonte nominal ainda possui o risco de queimar os ", 21, 239,self.y_text)
            self.game.draw_text("componentes ligados a ela caso haja algum problema, podendo ", 21, 239,self.y_text + 20)
            self.game.draw_text("ser um iniciador de incêndio.", 21, 239, self.y_text + 40)
            self.game.draw_text("Agora você vai ver como conectar uma fonte na placa-mãe e nos", 21, 239, self.y_text + 60)
            self.game.draw_text("outros componentes.", 21, 239, self.y_text + 80)
        if layer == 13:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/fontes_p.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Primeiro, deve-se ter o conhecimento de qual será o consumo de energia ", 21, x_text, self.y_text)
            self.game.draw_text("que o computador requer para se ter uma fonte que cumpra a demanda.", 21, x_text, self.y_text + 20)
            self.game.draw_text("Ao escolher a fonte adequada, realize a instalação dos cabos dela fora ", 21, x_text, self.y_text + 40)
            self.game.draw_text("da tomada.", 21, x_text, self.y_text + 60)
        if layer == 14:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/24_pinos.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois, deve-se identificar o cabo de ligação com a placa-mãe de 24 pinos. ", 21, x_text, self.y_text)
            self.game.draw_text("Algumas fontes possuem o cabo dividido em 20 pinos e outro fio de 4", 21, x_text, self.y_text + 20)
            self.game.draw_text("pinos, pois assim mantém compatibilidade com placas-mãe do padrão AT.", 21, x_text, self.y_text + 40)
            self.game.draw_text("Essas fontes de um cabo com 20 pinos e outro de 4 possuem os ", 21, x_text, self.y_text + 60)
            self.game.draw_text("fios próximos para facilitar a identificação durante a conexão.", 21, x_text, self.y_text + 80)
        if layer == 15:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/conector.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Para encontrar o conector na placa-mãe, ele fica na região ", self.font_size, 249, self.y_text)
            self.game.draw_text("onde está escrito ATX Power 1 (ou ATXPWR1).", self.font_size, 249, self.y_text + 20)
        if layer == 16:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/conexao.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A conexão dos pinos possui apenas um meio de serem encaixados. Então, antes ", 20, x_text, self.y_text)
            self.game.draw_text("de encaixar o cabo, verifique se o formato do primeiro pino da extremidade ", 20, x_text, self.y_text + 20)
            self.game.draw_text("do conector da placa-mãe condiz com o pino da fonte. Se estiverem corretos, ", 20, x_text, self.y_text + 40)
            self.game.draw_text("basta conectar o cabo.", 20, x_text, self.y_text + 60)
        if layer == 17:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/conexao.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O conector de 8/4 pinos da CPU fica próximo ao soquete na placa-mãe.", 21, x_text, self.y_text)
            self.game.draw_text("Você também pode encontrá-lo como ATX CPU ou ATX 12V. O processo de ", 21, x_text, self.y_text + 20)
            self.game.draw_text("conexão é o mesmo que o de 24 pinos.", 21, x_text, self.y_text + 40)
        if layer == 18:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/fonte.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Mesmo com a fonte já conectada à placa-mãe, o computador ", 21, 249,self.y_text)
            self.game.draw_text("não iniciaria, pois, como dito anteriormente, alguns", 21, 249,self.y_text + 20)
            self.game.draw_text("componentes precisam de uma condução de energia direta.", 21, 249,self.y_text + 40)
            self.game.draw_text("É o caso do dispositivo de armazenamento de memória,", 21, 249,self.y_text + 60)
            self.game.draw_text("placa de vídeo e fans do computador.", 21, 249,self.y_text + 80)
        if layer == 19:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/sata.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para conectar a fonte ao dispositivo de armazenamento de memória, utiliza-se o ", 19,x_text, self.y_text)
            self.game.draw_text("conector SATA, sigla para Serial Advanced Technology Attachment . Ele é o", 19,x_text, self.y_text + 20)
            self.game.draw_text("mais fácil de diferenciar dos outros conectores, pois não utiliza pinos,", 19, x_text,self.y_text + 40)
            self.game.draw_text("mas uma entrada em formato de L.", 19, x_text,self.y_text + 60)
        if layer == 20:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/conexao_sata.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para conectar o cabo é preciso escolher um dispositivo de armazenamento ", 21, x_text, self.y_text)
            self.game.draw_text("(HD ou SSD) que possua conexão SATA e encaixá-lo direto no cabo.", 21, x_text, self.y_text + 20)
        if layer == 21:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/8_pinos.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Algumas placas de vídeo e outros dispositivos conectados ao PCI Express ", 19, x_text, self.y_text)
            self.game.draw_text("também precisam dessa conexão direta com a fonte. O conector para elas é o de ", 19, x_text, self.y_text + 20)
            self.game.draw_text("8 pinos PCI-E. Dependendo da placa de vídeo os pinos da fonte podem ser ", 19, x_text, self.y_text + 40)
            self.game.draw_text("divididos em uma parte de 6 pinos e uma de dois como você pode ver na imagem. ", 19, x_text, self.y_text + 60)
            self.game.draw_text("O modo de conexão é o mesmo para os conectores de pinos da placa-mãe.", 19, x_text, self.y_text + 80)
        if layer == 22:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/molex.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O conector molex também possui uma entrada diferente dos outros ", 21, x_text, self.y_text)
            self.game.draw_text("cabos da fonte. Ele possui pinos mais finos, mas na parte de ", 21, x_text, self.y_text + 20)
            self.game.draw_text("conexão dos fans. O cabo da fonte é que possui as entradas. ", 21, x_text, self.y_text + 40)
            self.game.draw_text("O modo de conexão consiste no simples encaixe dos cabos. ", 21, x_text, self.y_text + 60)
        if layer == 23:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/tomada.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois de ter todos os cabos instalados, conecte o cabo de energia", 21, x_text,self.y_text)
            self.game.draw_text("da fonte na tomada.", 21, x_text,self.y_text + 20)
            self.game.draw_text("Vamos conectar seus conhecimentos adquiridos...", 21, x_text,self.y_text + 40)
        if layer == 24:
            self.gamimg_layer = True
            if not self.csr:
                mx, my = pygame.mouse.get_pos()
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/escolha_fonte.png'), (0, 0))
                if 503 > mx > 264 and 502 > my > 264 :
                    self.game.display.blit(pygame.image.load('data/img/Bar_4.png'), (264,264))
                if 249 > mx > 10 and 502 > my > 264 :
                    self.game.display.blit(pygame.image.load('data/img/Bar_4.png'), (10,264))
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1 and ((503 > mx > 264 and 502 > my > 264) or (249 > mx > 10 and 502 > my > 264)):
                            if 503 > mx > 264 and 502 > my > 264:
                                self.font = "400w"
                            elif 249 > mx > 10 and 502 > my > 264:
                                self.font = "300w"
                            self.csr = True
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
                self.game.draw_text("Escolha a fonte adequada para a placa-mãe, conecte ", 20, 220, 25)
                self.game.draw_text("os cabos e veja se o computador liga", 19, 290, 45)
                self.game.draw_text("(Troque de fonte se os cabos não servirem)", 19, 268, 65)
            if self.csr:
                self.first_question(self.font)
        if layer == 25:
            self.count_click = 0
            self.draw_very_good()
        if layer == 26:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/pcis.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Uma das outras entradas da placa-mãe são os slots PCI e PCI-Express. ", 21, x_text, self.y_text)
        if layer == 27:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/not_pci.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Atualmente, o slot PCI (Peripherical Component Interconnect) ", 21, 247,self.y_text)
            self.game.draw_text("está em desuso devido a baixa velocidade de transmissão de ", 21, 247,self.y_text + 20)
            self.game.draw_text("dados. Ele foi substituído pelo PCI-Express, um slot cuja", 21, 247,self.y_text + 40)
            self.game.draw_text("velocidade e capacidade de transferência é maior e com ", 21, 247,self.y_text + 60)
            self.game.draw_text("tecnologia de implementação em série, o que significa  ", 21, 247,self.y_text + 80)
            self.game.draw_text("que a informação é trafegada por mais de um caminho. ", 21, 247,self.y_text + 100)
        if layer == 28:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/lanes.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Esses caminhos são chamados de lanes e a quantidade de lanes vai diferenciar", 19, x_text, self.y_text)
            self.game.draw_text("de acordo com a aplicação. ", 19, x_text, self.y_text + 20)
            self.game.draw_text("Em um slot PCI-E para transferência de dados a partir de uma placa de rede, por ", 19, x_text, self.y_text + 40)
            self.game.draw_text("exemplo, pode ser utilizada uma lane.", 19, x_text, self.y_text + 60)
            self.game.draw_text("Mas para uma transferência de um grande volume de dados de uma placa ", 19, x_text, self.y_text + 80)
            self.game.draw_text("de vídeo dedicada, pode ser necessário um PCI-Express com 16 lanes.", 19, x_text, self.y_text + 100)
        if layer == 29:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/lanes.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("De acordo com o número de lanes, o tamanho do slot PCI-E varia", 19, x_text, self.y_text)
            self.game.draw_text("proporcionalmente e de maneira direta.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Veja os slots de alguns PCI-Es e a seu tamanhos de acordo com a quantidade de", 19, x_text, self.y_text + 40)
            self.game.draw_text("lanes.", 19, x_text, self.y_text + 60)
        if layer == 30:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/lanes.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Além da quantidade de lanes, a velocidade de transferência também  ", 19, x_text, self.y_text)
            self.game.draw_text("possui variação, mas em relação à versão do PCI-Express. A versão ", 19, x_text, self.y_text + 20)
            self.game.draw_text("mais atual do PCI-Express é a 5.0 que consta com uma capacidade ", 19, x_text, self.y_text + 40)
            self.game.draw_text("teórica máxima de transferência de 128 GB/s. Para comparar, o PCI-E ", 19, x_text, self.y_text + 60)
            self.game.draw_text("versão 1.0 possuía uma velocidade de transferência máxima de 8 GB/s.", 19, x_text, self.y_text + 80)
        if layer == 31:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/lanes.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("De acordo com o número de lanes, o tamanho do slot PCI-E varia", 19, x_text, self.y_text)
            self.game.draw_text("proporcionalmente e de maneira direta.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Veja os slots de alguns PCI-Es e a seu tamanhos de acordo com a quantidade de", 19, x_text, self.y_text + 40)
            self.game.draw_text("lanes.", 19, x_text, self.y_text + 60)
        if layer == 32:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/placa.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora você vai ver como instalar um hardware com entrada PCI-E na placa-mãe", 19, x_text, self.y_text)
            self.game.draw_text("Primeiro, deve-se verificar qual hardware foi escolhido e qual o número ", 19, x_text, self.y_text + 20)
            self.game.draw_text("de lanes que ele requer.", 19, x_text, self.y_text + 40)
        if layer == 33:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/pci_nome.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Depois, deve-se identificar o slot adequado para o encaixe com", 19, 243, self.y_text)
            self.game.draw_text("o hardware escolhido. Para encontrar o slot na placa-mãe, basta ", 19, 243, self.y_text + 20)
            self.game.draw_text("procurar pelo nome PCIE ou PCIExpress.", 19, 243, self.y_text + 40)
        if layer == 34:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/pci-e16xe1x.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Algumas placas-mãe possuem mais de dois PCI-Es, geralmente vindo com", 19, x_text, self.y_text)
            self.game.draw_text("um de 16x e um de 1x.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Caso a instalação seja de um uma placa de vídeo, o slot adequado é o 16x.", 19, x_text, self.y_text + 40)
        if layer == 35:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/entradas.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os hardwares instalados no PCI-E possuem entradas externas e por", 19, x_text, self.y_text)
            self.game.draw_text("isso, na maioria das vezes, são instalados já com a placa-mãe dentro ", 19,x_text, self.y_text + 20)
            self.game.draw_text("do gabinete.", 19,x_text, self.y_text + 40)
        if layer == 36:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/slot.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Ao instalar uma placa de vídeo, por exemplo, deve-se retirar ", 19,243, self.y_text)
            self.game.draw_text("a tampa do gabinete em perpendicular ao slot na placa-mãe", 19, 243,self.y_text + 20)
            self.game.draw_text("desparafusando-o.", 19, 243,self.y_text + 40)
        if layer == 37:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/ar.png'), (275, 17))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/1.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/2.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/3.png'), (215, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/4.png'), (215, 17))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/5.png'), (215, 17))
            if self.clock == 5:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/6.png'), (215, 17))
            if self.clock == 6:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/7.png'), (215, 17))
            if self.clock == 7:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/8.png'), (215, 17))
            if self.clock == 8:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/9.png'), (215, 17))
            if self.clock == 9:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/9.png'), (215, 17))
            if self.clock == 10:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/9.png'), (215, 17))
            pygame.time.wait(70)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/bordas.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois, encaixe a placa de vídeo no slot da região em que a tampa do", 19, 139, self.y_text)
            self.game.draw_text("gabinete foi retirada. O encaixe é semelhante ao da memória RAM, pois ", 19, 139, self.y_text + 20)
            self.game.draw_text("há uma parte divisão no encaixe com uma das partes maior do que a outra", 19, 139, self.y_text + 40)
            self.game.draw_text("e por isso não há como errar o sentido.", 19, 139, self.y_text + 60)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 10:
                self.clock = 0
        if layer == 38:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/ar.png'), (275, 17))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/10.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/11.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/12.png'), (215, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/13.png'), (215, 17))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/anim/gpu/14.png'), (215, 17))
            pygame.time.wait(90)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/bordas.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Após pressionar para baixo a placa de vídeo, coloque os conectores da fonte.", 19, 139, self.y_text)
            self.game.draw_text("Depois disso, parafuse o espelho da placa de vídeo no gabinete.", 19, 139, self.y_text + 20)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 5:
                self.clock = 0    
        if layer == 39:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/placa_de_rede.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("O processo de instalação para outros componentes é o mesmo, ", 19,275, self.y_text)
            self.game.draw_text("com algumas exceções como a não conexão direta com a fonte.",19, 275, self.y_text + 20)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...",19, 275, self.y_text + 80)
            self.mouse_psi['16p'][1] = False
            self.cabos['16p'][1] = False
        if layer == 40:
            self.gamimg_layer = True

            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1 and self.clicking == 0:
                        self.clicking = 1
                    if self.clicking == 2:
                        self.clicking = 0
                    if self.slide[2]:
                        if not (944 > mx > 915 and 155 > my > 24):
                            self.mouse_psi['24p'][1] = False
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1 and self.clicking == 1:
                        self.clicking = 2

            if self.clicking == 0:
                self.q2['placa1'][1] = False
            if self.clicking == 1:
                if 376 > mx > 136 and 397 > my > 348:
                    self.q2['placa1'][1] = True
            if self.clicking == 0:
                if 830 > mx > 590 and 405 > my > 356:
                    self.q2['placa1'][1] = True
                    self.q2['placa2'][1] = True

            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Instale o hardware no PCI-Express", 20, 300, 45)
            if self.count_click >= 15:
                if self.slide[0]:
                    self.q2['placa1'][1] = False
                    self.q2['placa2'][1] = False
                    self.slide[0] = False
                    self.slide[1] = True
                    self.count_click = 0
                elif self.slide[1]:
                    self.q2['placa3'][1] = False
                    self.slide[1] = False
                    self.slide[2] = True
                    self.count_click = 0
                elif self.slide[2]:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                    pygame.mixer.Channel(1).set_volume(0.04)
                    self.i += 1
                    self.layers.append(self.i)
                    self.gamimg_layer = False
                    self.game.reset_keys()
                    self.score.count = 0
                    self.score.scr = 0
                    self.score.alternatives(1, 1)
                    self.count_click = 0
            if self.slide[0]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/q2.png'), (0, 0))
                if not self.q2['placa1'][1] and not self.q2['placa2'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/placa_de_video.png'), (136, 348))
                elif self.q2['placa1'][1] and not self.q2['placa2'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/placa_de_video.png'), (mx - 100, my - 30))
                if self.q2['placa2'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/placa_de_video.png'), self.q2['placa2'][0])
                    self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/gabinete.png'), (595, 130))
            if self.slide[1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/q2_2.png'), (0, 0))
                if not self.q2['placa3'][2]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/placa_de_video2.png'), (229, 179))
                if self.clicking == 1:
                    if 541 > mx > 336 and 265 > my > 188:
                        self.q2['placa3'][1] = True
                    if 568 > mx > 254 and 376 > my > 277 and self.q2['placa3'][1]:
                        self.q2['placa3'][2] = True
                if self.q2['placa3'][1] and self.q2['placa3'][2]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/placa_de_video2.png'), self.q2['placa3'][0])
                    self.count_click += 1
                    if self.count_click ==1:
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                        pygame.mixer.Channel(1).set_volume(0.05)
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/slot_pci.png'), (322, 265))
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/gabinete_p.png'), (211, 168))
            if self.slide[2]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/motherboardq2.png'), (369, 128))

                if (420 > mx > 153 and 226 > my > 0) and not self.mouse_psi['16p'][1] and self.clicking == 1:
                    self.mouse_psi['16p'][1] = True
                if self.mouse_psi['16p'][1] and not self.cabos['16p'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/16pinos.png'), (mx - 190, my - 200))
                if (957 > mx > 743 and 335 > my > 263) and self.clicking == 1:
                    self.mouse_psi['16p'][1] = False
                    self.cabos['16p'][1] = True

                if self.cabos['16p'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/cabo16.png'), self.cabos['16p'][0])
                    self.mouse_psi['16p'][1] = False
                    self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/gabineteq2.png'), (353, 128))
                if not self.mouse_psi['16p'][1] and not self.cabos['16p'][1]:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/16pinos.png'), self.mouse_psi['16p'][0])
        if layer == 41:
            self.draw_very_good()
        if layer == 42:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/chipset.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Saindo dos conectores, você vai aprender agora um pouco sobre o chipset.", 19, x_text,self.y_text)
            self.game.draw_text("Um chipset, como o próprio nome já diz, é um chip integrado no circuito da", 19, x_text,self.y_text + 20)
            self.game.draw_text("placa-mãe que tem como função gerenciar a transferência de dados entre os ", 19, x_text,self.y_text + 40)
            self.game.draw_text("componentes conectados à placa-mãe, como processador, periféricos e memórias. ", 19, x_text,self.y_text + 60)
        if layer == 43:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/pontes.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Nas placas-mãe menos recentes o chipset era um componente dividido em duas ", 19, x_text,self.y_text)
            self.game.draw_text("regiões da placa-mãe: ponte norte  (Northbridge) ou mch (Memory Controller Hub)", 19, x_text,self.y_text + 20)
            self.game.draw_text("e ponte sul  (Southbridge) ou ich (i/o Controller Hub).", 19, x_text,self.y_text + 40)
        if layer == 44:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/local_pontes.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A ponte norte é o chip localizado mais próximo ao soquete do processador e  ", 19, x_text, self.y_text)
            self.game.draw_text("comumente possui um dissipador de calor integrado. A função desse chip era ", 19, x_text, self.y_text + 20)
            self.game.draw_text("relacionada ao controle dos barramentos (slots) de memória e PCI Express ", 19, x_text,self.y_text + 40)
            self.game.draw_text("além do controle da capacidade da memória RAM e frequência máxima dela e ", 19, x_text,self.y_text + 60)
            self.game.draw_text("do processador.", 19, x_text,self.y_text + 80)
        if layer == 45:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/local_pontes.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("A ponte sul opera gerenciando regiões da placa-mãe cuja", 19, 275, self.y_text)
            self.game.draw_text(" transferência de dados não é tão grande. ", 19, 275, self.y_text + 20)
            self.game.draw_text("Por isso, as placas-mãe mais recentes transferiram as atividades ", 19, 275, self.y_text + 40)
            self.game.draw_text("da ponte sul para o processador e um único chip, chamado apenas ", 19, 275, self.y_text + 60)
            self.game.draw_text("de chipset.", 19, 275, self.y_text + 80)
        if layer == 46:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/FCH-PCH.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Dependendo da fabricante de processadores, esse circuito", 19, x_text, self.y_text)
            self.game.draw_text("integrado possui uma tecnologia e nome diferente. O termo", 19, x_text, self.y_text + 20)
            self.game.draw_text("dado ao chipset pela Intel é PCH, sigla para Platform ", 19, x_text, self.y_text + 40)
            self.game.draw_text("Controller Hub. Já na AMD, o termo é FCH, sigla para Fusion", 19, x_text, self.y_text + 60)
            self.game.draw_text("Controller Hubs.", 19, x_text, self.y_text + 80)
        if layer == 47:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/novo_chipset.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Com esses novos chips é possível escolher o tipo de gerenciamento de ", 19, x_text, self.y_text)
            self.game.draw_text("acordo com as aplicações do usuário. Para entusiastas de hardware,", 19, x_text, self.y_text + 20)
            self.game.draw_text("existem chipsets com gerenciamento de maior frequência de memória ", 19, x_text, self.y_text + 40)
            self.game.draw_text("e processamento, além de capacidade.", 19, x_text, self.y_text + 60)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 19, x_text, self.y_text + 80)
            self.q = QuestionsThree(48)
        if layer == 48:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load(self.q.image), (0, 0))
            if self.q.lay == 48:
                self.selected_question()
            elif self.q.lay == 49:
                self.selected_question()
            self.game.draw_text("Identifique cada função de acordo com a", 24, 200, 45)
            self.game.draw_text("ponte do chipset", 24, 335, 65)
            if self.q.lay == 48:
                self.game.draw_text("*PONTE NORTE*", 28, 328, 140)
            elif self.q.lay == 49:
                self.game.draw_text("*PONTE Sul*", 28, 348, 140)
            pygame.display.update()
        if layer == 49:
            self.draw_very_good()
        if layer == 50:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/timer_BIOS.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Você já percebeu que quando um computador é desligado e depois ligado,", 19, x_text, self.y_text)
            self.game.draw_text("independente de ter um SO novo ou acesso à internet, o horário mostrado", 19, x_text, self.y_text + 20)
            self.game.draw_text("na BIOS está sempre ativo? ", 19, x_text, self.y_text + 40)
            self.game.draw_text("Bom, isso é uma função que demanda energia. Mas como há energia se o", 19, x_text, self.y_text + 60)
            self.game.draw_text("computador estiver fora da tomada?", 19, x_text, self.y_text + 80)
        if layer == 51:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/bateria_BIOS.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("A resposta para isso é que a placa-mãe possui uma pequena pilha", 19, 275, self.y_text)
            self.game.draw_text("chamada bateria CMOS. Ela é responsável pela alimentação de", 19, 275, self.y_text + 20)
            self.game.draw_text("energia do recurso do relógio.", 19, 275, self.y_text + 40)
            self.game.draw_text("Essa bateria é feita de lítio em um formato de moeda. A carga ", 19, 275, self.y_text + 60)
            self.game.draw_text("presente nela pode ser utilizada por até dez anos,  ", 19, 275, self.y_text + 80)
            self.game.draw_text("dependendo da temperatura em que opera e do ambiente. ", 19, 275, self.y_text + 100)
        if layer == 52:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/codec.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Outro chips importante presente na placa-mãe é o chip integrado de codec ", 19, x_text, self.y_text)
            self.game.draw_text("de áudio. Ele possibilita a transmissão de sinais sonoros convertidos ", 19, x_text, self.y_text + 20)
            self.game.draw_text("tanto no envio quanto no recebimento. Essa placa pode ser integrada no ", 19, x_text, self.y_text + 40)
            self.game.draw_text("barramento PCI-Express ou conectada de maneira externa por uma porta USB.", 19, x_text, self.y_text + 60)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 19, x_text, self.y_text + 80)
            self.q = QuestionsThree(53)
        if layer == 53:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load(self.q.image), (0, 0))
            self.selected_question_2()
            self.game.draw_text("Relacione o nome do chip ou a sua função ", 24, 230, 45)
            self.game.draw_text("de acordo com a imagem", 24, 335, 65)
        if layer == 54:
            self.draw_very_good()
        if layer == 55:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/perifericos.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Por último sobre a placa-mãe, há os conectores periféricos, também", 19, x_text, self.y_text)
            self.game.draw_text("chamadas de portas, que como o próprio nome já diz, servem para conectar ", 19, x_text,self.y_text + 20)
            self.game.draw_text("a placa-mãe aos dispositivos periféricos. ", 19, x_text,self.y_text + 40)
        if layer == 56:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/usb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os principais conectores são: As portas USB, do inglês Universal Serial Bus, que", 19, x_text, self.y_text)
            self.game.draw_text("servem como um padrão universal de conexão para diversos dispositivos como ", 19, x_text,self.y_text + 20)
            self.game.draw_text("mouses, teclados, smartphones, HDs externos, pen drives, leds, entre outros", 19, x_text,self.y_text + 40)
        if layer == 57:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/entradas_video.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("As portas de vídeo mais comuns são VGA, HDMI, DisplayPort e", 19, 260, self.y_text)
            self.game.draw_text("USB C-type.", 19, 260,self.y_text + 20)
        if layer == 58:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/vga.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O padrão VGA, sigla para Video Graphics Array, é o mais antigo. A maioria das  ", 19, x_text, self.y_text)
            self.game.draw_text("placas-mãe mais novas não vêm com ele e é praticamente inexistente nos os ", 19, x_text,self.y_text + 20)
            self.game.draw_text("notebooks atuais. Esse padrão possibilita a transferência apenas de vídeo e em", 19, x_text,self.y_text + 40)
            self.game.draw_text("baixa qualidade e velocidade de transferência se comparado com os padrões mais ", 19, x_text,self.y_text + 60)
            self.game.draw_text("novos.", 19, x_text,self.y_text + 80)
        if layer == 59:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/hdmi.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O padrão HDMI, sigla para High-Definition Multimedia Interface, surgiu como uma", 19, x_text, self.y_text)
            self.game.draw_text("evolução do VGA, pois permite a transferência de áudio e vídeo e o vídeo possui ", 19, x_text,self.y_text + 20)
            self.game.draw_text("melhor qualidade e maior velocidade de transmissão. Além disso, algumas versões ", 19, x_text,self.y_text + 40)
            self.game.draw_text("dos cabos HDMI também podem transmitir sinal de internet.", 19, x_text,self.y_text + 60)
        if layer == 60:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/usb_c.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O padrão USB C-type ou tipo C é uma evolução do USB convencional,", 19, x_text, self.y_text)
            self.game.draw_text("também chamado de A-type, ou tipo A. Ele é mais comum em ", 19, x_text,self.y_text + 20)
            self.game.draw_text("placas-mãe de notebooks mais novos e smartphones e, além de possuir ", 19, x_text,self.y_text + 40)
            self.game.draw_text("as mesmas capacidades do USB tipo A, possui capacidade de transferência", 19, x_text,self.y_text + 60)
            self.game.draw_text("de dados suficiente para transmitir áudio e vídeo. O USB tipo é ligeiramente", 19, x_text,self.y_text + 80)
            self.game.draw_text("menor do que o tipo A e pode ser conectado nos dois sentidos de entrada.", 19, x_text,self.y_text + 100)
            self.q = QuestionsThree(61)
        if layer == 61:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load(self.q.image), (0, 0))
            self.selected_question_2()
            self.game.draw_text("Identifique a entrada e relacione-a com  ", 24, 246, 45)
            self.game.draw_text("a sua função", 24, 385, 65)
        if layer == 62:
            self.draw_very_good()
        if layer == 63:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/intel_amd.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ufa! Você terminou de conhecer um pouco mais sobre a placa-mãe.", 19, x_text, self.y_text)
            self.game.draw_text("Agora verá outros hardwares ainda nesta fase.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Você vai conhecer agora um pouco sobre o principal componente", 19, x_text, self.y_text + 40)
            self.game.draw_text("do computador, o processador.", 19, x_text, self.y_text + 60)
        if layer == 64:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/processador.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Também chamado de CPU. sigla para Central Processing Unit, esse componente ", 19, x_text, self.y_text)
            self.game.draw_text("é responsável pela realização e controle de todas as tarefas operacionais do ", 19, x_text, self.y_text + 20)
            self.game.draw_text("computador. De maneira mais simples, ele realiza as instruções encontradas ", 19, x_text, self.y_text + 40)
            self.game.draw_text("em algumas das memórias do computador.", 19, x_text, self.y_text + 60)
        if layer == 65:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/binario.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O modelo padrão que as informações chegam até o processador é o binário, ", 19, x_text, self.y_text)
            self.game.draw_text("ou seja, apenas informações que representem 0 e 1. ", 19, x_text, self.y_text + 20)
        if layer == 66:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/funcoes_processador.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("As funções específicas de um processador são a realização de  ", 19,265, self.y_text)
            self.game.draw_text("operações lógicas e aritméticas como multiplicações, divisões e ", 19,265, self.y_text + 20)
            self.game.draw_text("comparações de valores numéricos; a realização de transferência de", 19,265, self.y_text + 40)
            self.game.draw_text("dados, movendo-os para locais de armazenamentos diferentes e a ", 19,265, self.y_text + 60)
            self.game.draw_text("transferência direta dos dados contidos em um dispositivo ", 19,265, self.y_text + 80)
            self.game.draw_text("para o processador.", 19,265, self.y_text + 100)
        if layer == 67:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/Programas.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Esses dados presentes no local de armazenamento podem ser informações", 19,x_text, self.y_text)
            self.game.draw_text("a serem processadas ou instruções de processamento. Esta última quando ", 19,x_text, self.y_text + 20)
            self.game.draw_text("ordenada pelo processador forma um programa.", 19,x_text, self.y_text + 40)
        if layer == 68:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/ULA.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Dentro dos processadores mais recentes houve uma mudança de unidades ", 19,x_text, self.y_text)
            self.game.draw_text("internas, mas até esse momento havia as seguintes unidades com papéis ", 19,x_text, self.y_text + 20)
            self.game.draw_text("distintos.", 19,x_text, self.y_text + 40)
            self.game.draw_text("A unidade lógica e aritmética, também conhecida como ULA, é responsável ", 19,x_text, self.y_text + 60)
            self.game.draw_text("pelas atividades que constam no seu nome.", 19,x_text, self.y_text + 80)
        if layer == 69:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/16bits.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Os processadores atuais possuem outra unidade para cálculos, a ", 19, 255, self.y_text)
            self.game.draw_text("Unidade de Ponto Flutuante, que serve para processar dados de ", 19, 255, self.y_text + 20)
            self.game.draw_text("grande tamanho, como de 64 e 128 bits.", 19, 255,self.y_text + 40)
            self.game.draw_text("Outra unidade é a de controle. Ela é específica para decodificar ", 19, 255,self.y_text + 60)
            self.game.draw_text("instruções e controlar execuções de processos e identificar ", 19, 255,self.y_text + 80)
            self.game.draw_text("os processos em operação.", 19, 255,self.y_text + 100)
        if layer == 70:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/registrador.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A outra unidade interna do processador é a dos registradores. Sua ", 19, x_text, self.y_text)
            self.game.draw_text("função é armazenar os dados preparando-os para serem processados.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Por meio da interação desses componentes ocorre o armazenamento, a ", 19, x_text,self.y_text + 40)
            self.game.draw_text("manipulação e o processamento das informações", 19, x_text,self.y_text + 60)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 19, x_text,self.y_text + 80)
            self.q = QuestionsThree(71)
        if layer == 71:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load(self.q.image), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.selected_question_2()
            self.game.draw_text("Relacione a unidade do processador ", 24, 230, 45)
            self.game.draw_text("com a sua função", 24, 355, 65)
        if layer == 72:
            self.draw_very_good()
        if layer == 73:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/nucleos.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Dentro do processador há ainda a unidade de memória e a divisão das ", 19, x_text, self.y_text)
            self.game.draw_text("unidades de processamento em núcleos.", 19, x_text, self.y_text + 20)
        if layer == 74:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/hierarquia.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A memória presente no processador é chamada de cache e possui um grau", 19, x_text, self.y_text)
            self.game.draw_text("de performance maior do que as outras memórias do computador, pois se ", 19, x_text, self.y_text + 20)
            self.game.draw_text("trata de um armazenamento de constante acesso pelas unidades", 19, x_text, self.y_text + 40)
            self.game.draw_text("de processamento. ", 19, x_text, self.y_text + 60)
        if layer == 75:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/hierarquia.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Nessa ordem hierárquica de memórias as mais rápidas também são ", 19, 245, self.y_text)
            self.game.draw_text("as com menor capacidade, principalmente devido a tecnologia ", 19, 245, self.y_text + 20)
            self.game.draw_text("e o seu consequente custo alto.", 19, 245, self.y_text + 40)
            self.game.draw_text("O mesmo acontece com a memória cache. De todas, ela é a que possui ", 19, 245, self.y_text + 60)
            self.game.draw_text("capacidade de armazenamento, na ordem dos MB", 19, 245, self.y_text + 80)
            self.game.draw_text("(Mega Bytes).", 19, 245, self.y_text + 100)
        if layer == 76:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/caches.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A memória cache pode ser classificada de acordo com a posição em relação ao ", 19, x_text, self.y_text)
            self.game.draw_text("processador e com isso existem os níveis l1, l2 e l3. Quanto menor o número,", 19, x_text, self.y_text + 20)
            self.game.draw_text("mais próximo o armazenamento está do processador.", 19, x_text, self.y_text + 40)
        if layer == 77:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/caches.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("É importante saber que quanto mais memória cache disponível, melhor", 19, x_text, self.y_text)
            self.game.draw_text("será o desempenho dos processos do computador, pois a capacidade das ", 19, x_text, self.y_text + 20)
            self.game.draw_text("memórias é mensurada de acordo com o poder de processamento da CPU.", 19, x_text, self.y_text + 40)
        if layer == 78:
            wro,wri = False, False
            x,y = 0, 0
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/q7.png'), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Qual a capacidade de armazenamento", 24, 250, 45)
            self.game.draw_text("da memória cache?", 24, 362, 75)
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 400 > mx > 20 and 266 > my > 198:
                            wro = True
                            x, y = 20, 198
                        elif 400 > mx > 20 and 344 > my > 276:
                            wro = True
                            x, y = 20, 276
                        elif 642 > mx > 262 and 422 > my > 354:
                            wro = True
                            x, y = 262, 354
                        elif 879 > mx > 499 and 346 > my > 278:
                            wro = True
                            x, y = 499, 278
                        elif 879 > mx > 499 and 268 > my > 200:
                            wri = True
                            x, y = 499, 200
            if wro:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/wrong_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/Bar_5_r.png'), (x, y))
                if self.count_click >= 5:
                    wro = False
                    self.count_click = 0
            if wri and not wro:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/Bar_5_g.png'), (x, y))
                if self.count_click >= 1:
                    self.i += 1
                    self.layers.append(self.i)
                    self.gamimg_layer = False
                    self.game.reset_keys()
                    self.score.count = 0
                    self.score.scr = 0
                    for i in range(0,2):
                        self.score.alternatives(i, 1)
                    self.count_click = 0
        if layer == 79:
            self.draw_very_good()
        if layer == 80:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/nucleos.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O núcleo do processador, também chamado de core, pode ficar limitado", 19, x_text, self.y_text)
            self.game.draw_text("para realizar poucas tarefas. Para aumentar o número de tarefas e", 19, x_text, self.y_text + 20)
            self.game.draw_text("executá-las em paralelo, as empresas de processadores criaram CPUs", 19, x_text, self.y_text + 40)
            self.game.draw_text("com mais de um núcleo.", 19, x_text, self.y_text + 60)
        if layer == 81:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/n_nucleos.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Quanto maior a quantidade de núcleos de um processador, maior é ", 19, 250, self.y_text)
            self.game.draw_text("o seu desempenho multitarefas.", 19, 250, self.y_text + 20)
            self.game.draw_text("Existem processadores de 2 núcleo, 4 núcleo, 6 núcleo e até 8 núcleos.", 19, 250, self.y_text + 40)
        if layer == 82:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/clock.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Outra coisa a ser notada é como é medida a velocidade de processamento da CPU. ", 19, x_text, self.y_text)
            self.game.draw_text("Quanto maior o número de dados processados em um menor número de tempo,  ", 19, x_text, self.y_text + 20)
            self.game.draw_text("mais rápido é o processador. Isso se chama clock. Essa grandeza de frequência   ", 19, x_text, self.y_text + 40)
            self.game.draw_text("e por isso é medida em Hertz. Outros hardwares também a utilizam, como a  ", 19, x_text, self.y_text + 60)
            self.game.draw_text("memória RAM (medida em MegaHertz) e monitores (medidos em Hertz).", 19, x_text, self.y_text + 80)
        if layer == 83:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/ghz.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A frequência dos processadores atuais chegam na casa dos Gigahertz, com", 19, x_text, self.y_text)
            self.game.draw_text("os mais comuns com um clock de 2.0 GHz, e os mais robustos que podem ", 19, x_text, self.y_text + 20)
            self.game.draw_text("ultrapassar os 5.0 GHz.", 19, x_text, self.y_text + 40)
        if layer == 84:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/threads.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Além dos núcleos há também a tecnologia dos threads que é uma forma de", 19, x_text, self.y_text)
            self.game.draw_text("escalonamento, ou seja, agendar tarefas alternando os processos de uma maneira", 19, x_text, self.y_text + 20)
            self.game.draw_text("tão rápida que parecem estarem sendo executados por mais de um núcleo. Então", 19, x_text, self.y_text + 40)
            self.game.draw_text("diz-se que os threads são emulações de núcleos, ou divisões de núcleos, podendo", 19, x_text, self.y_text + 60)
            self.game.draw_text("ser chamados também de núcleos lógicos e os reais são chamados de ", 19, x_text, self.y_text + 80)
            self.game.draw_text("núcleos físicos.", 19, x_text, self.y_text + 100)
        if layer == 85:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/threads.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Essa tecnologia está presente em diversos processadores com mais de um ", 19, x_text, self.y_text)
            self.game.draw_text("núcleo e ela possui os mesmos princípios de processadores multicore, ", 19, x_text, self.y_text + 20)
            self.game.draw_text("realização de multitarefas.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 19, x_text, self.y_text + 60)
        if layer == 86:
            wro, wri = False, False
            x, y = 0, 0
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/q8.png'), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Qual dessas tecnologias permite a realização de mais ", 20, 212, 45)
            self.game.draw_text("de uma tarefa ao mesmo tempo no computador?", 20, 228, 75)
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 400 > mx > 20 and 266 > my > 198:
                            wro = True
                            x, y = 20, 198
                        elif 889 > mx > 509 and 267 > my > 198:
                            wro = True
                            x, y = 509, 198
                        elif 642 > mx > 262 and 351 > my > 282:
                            wri = True
                            x, y = 262, 282
            if wro:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/wrong_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/Bar_5_r.png'), (x, y))
                if self.count_click >= 5:
                    wro = False
                    self.count_click = 0
            if wri and not wro:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/Bar_5_g.png'), (x, y))
                if self.count_click >= 1:
                    self.i += 1
                    self.layers.append(self.i)
                    self.gamimg_layer = False
                    self.game.reset_keys()
                    self.score.count = 0
                    self.score.scr = 0
                    for i in range(0, 2):
                        self.score.alternatives(i, 1)
                    self.count_click = 0
        if layer == 87:
            self.draw_very_good()
        if layer == 88:
            wro, wri = False, False
            x, y = 0, 0
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/q9.png'), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Os threads são Núcleos …", 24, 295, 45)
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 400 > mx > 20 and 266 > my > 198:
                            wri = True
                            x, y = 20, 198
                        elif 889 > mx > 509 and 267 > my > 198:
                            wro = True
                            x, y = 509, 198
                        elif 642 > mx > 262 and 351 > my > 282:
                            wro = True
                            x, y = 262, 282
            if wro:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/wrong_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/Bar_5_r.png'), (x, y))
                if self.count_click >= 5:
                    wro = False
                    self.count_click = 0
            if wri and not wro:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/Bar_5_g.png'), (x, y))
                if self.count_click >= 1:
                    self.i += 1
                    self.layers.append(self.i)
                    self.gamimg_layer = False
                    self.game.reset_keys()
                    self.score.count = 0
                    self.score.scr = 0
                    for i in range(0, 2):
                        self.score.alternatives(i, 1)
                    self.count_click = 0
        if layer == 89:
            self.draw_very_good()
            self.q = QuestionsThree(90)
        if layer == 90:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load(self.q.image), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.selected_question_2()
            self.game.draw_text("Ordene a frequência de cada item ", 24, 280, 45)
            self.game.draw_text("abaixo", 24, 445, 65)
        if layer == 91:
            self.draw_very_good()
        if layer == 92:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/intel_amd.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Como foi dito nas fases anteriores, as marcas de processadores para", 19, x_text, self.y_text)
            self.game.draw_text("computadores que dominam o mercado atual são a Intel e a AMD. Vamos tratar ", 19, x_text, self.y_text + 20)
            self.game.draw_text("aqui apenas da Intel. Os processadores da Intel são classificados de acordo ", 19, x_text, self.y_text + 40)
            self.game.draw_text("com as tarefas que o usuário deseja realizar.", 19, x_text, self.y_text + 60)
        if layer == 93:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/intel_celeron.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Para tarefas simples como o uso de internet para consumo audiovisu-", 19, 250, self.y_text)
            self.game.draw_text("al, edição de documentos de texto e apresentação, são recomendados ", 19, 250, self.y_text + 20)
            self.game.draw_text("os processadores da linha Pentium e Celeron. Atualmente, esses rece-", 19, 250, self.y_text + 40)
            self.game.draw_text("beram uma melhoria em seu desempenho devido à miniaturização da ", 19, 250, self.y_text + 60)
            self.game.draw_text("arquitetura, também chamada de litografia, dos processadores.", 19, 250, self.y_text + 80)
        if layer == 94:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/litografia.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Quanto menor o tamanho dos dos componentes do núcleo dos processadores,", 19, x_text, self.y_text)
            self.game.draw_text("menor é o gasto e perda de energia. Atualmente existem processadores para", 19, x_text, self.y_text + 20)
            self.game.draw_text("computadores de grande porte com uma litografia de 10 nanômetros. Geralmente", 19, x_text, self.y_text + 40)
            self.game.draw_text("essas mudanças ocorrem de acordo com a mudança de geração.", 19, x_text, self.y_text + 60)
        if layer == 95:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/core.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para tarefas que requerem um grande nível de processamento, como edição ", 19, x_text, self.y_text)
            self.game.draw_text("de vídeo, manipulação em 3D, jogos e pequenos servidores, são  ", 19, x_text, self.y_text + 20)
            self.game.draw_text("recomendados os processadores da Intel das linhas core i3, i5, i7 e i9.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Quanto maior é o poder de processamento, na maioria das vezes, mais caro", 19, x_text, self.y_text + 60)
            self.game.draw_text("é o processador.", 19, x_text, self.y_text + 80)
        if layer == 96:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/versoes.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Apesar de haver uma evolução de acordo com o lançamento das linhas", 19, 250, self.y_text)
            self.game.draw_text("“i”, nem sempre isso quer dizer que um “core i” de número mais alto ", 19, 250, self.y_text + 20)
            self.game.draw_text("é melhor do que o outro de número mais baixo.", 19, 250, self.y_text + 40)
            self.game.draw_text("Isso ocorre porque existem as classificações de gerações e de ", 19, 250, self.y_text + 60)
            self.game.draw_text("finalidade de processadores.", 19, 250, self.y_text + 80)    
        if layer == 97:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/geracoes.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("As gerações dos processadores são informadas no primeiro número após ", 19, x_text, self.y_text)
            self.game.draw_text("o nome Intel core iX Y. Esse Y é o número da geração.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Atualmente, a Intel está na 11ª geração de processadores e houveram grandes", 19, x_text, self.y_text + 40)
            self.game.draw_text("mudanças das primeiras gerações até 6ª e 7ª geração, como a mudança de ", 19, x_text, self.y_text + 60)
            self.game.draw_text("soquetes, diminuição de litografia, aumento de clock e maior quantidade", 19, x_text, self.y_text + 80)    
            self.game.draw_text("de núcleos. Vamos testar seus conhecimentos adquiridos...", 19, x_text, self.y_text + 100)    
        if layer == 98:
            wro, wri = False, False
            x, y = 0, 0
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/q11.png'), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/up_bar.png'), (0, 0))
            self.game.draw_text("João, seu amigo, quer comprar um processador para o mon-", 19, 195, 30)
            self.game.draw_text("tar o seu  computador de mesa para realizar trabalhos como ", 19, 195, 50)
            self.game.draw_text("planilhas e escrita de documentos, mas não quer gastar   ", 19, 195, 70)
            self.game.draw_text("muito. Além disso, no seu tempo livre, gosta de assistir a  ", 19, 195, 90)
            self.game.draw_text("vídeos na internet. ", 19, 195, 110)
            self.game.draw_text("Qual Processador você indicaria para João?", 19, 195, 130)
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 400 > mx > 20 and 266 > my > 198:
                            wro = True
                            x, y = 20, 198
                        elif 400 > mx > 20 and 344 > my > 276:
                            wro = True
                            x, y = 20, 276
                        elif 879 > mx > 499 and 268 > my > 200:
                            wri = True
                            x, y = 499, 200
                        elif 879 > mx > 499 and 346 > my > 278:
                            wro = True
                            x, y = 499, 278
            if wro:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/wrong_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/Bar_5_r.png'), (x, y))
                if self.count_click >= 5:
                    wro = False
                    self.count_click = 0
            if wri and not wro:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/Bar_5_g.png'), (x, y))
                if self.count_click >= 1:
                    self.i += 1
                    self.layers.append(self.i)
                    self.gamimg_layer = False
                    self.game.reset_keys()
                    self.score.count = 0
                    self.score.scr = 0
                    for i in range(0, 2):
                        self.score.alternatives(i, 1)
                    self.count_click = 0
        if layer == 99:
            self.draw_very_good()
        if layer == 100:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/i3-3225.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Inicialmente, nesse caso específico é possível dizer que o Pentium é o mais", 19, x_text, self.y_text)
            self.game.draw_text("adequado para João, mas deve-se sempre pesquisar as especificações e os preços", 19, x_text, self.y_text + 20)
            self.game.draw_text("no site da fabricante ou em sites de benchmark (avaliação de produtos concorren-", 19, x_text, self.y_text + 40)
            self.game.draw_text("tes). Se você pesquisar as especificações de um processador Intel Core i3-3225, por", 19, x_text, self.y_text + 60)
            self.game.draw_text("exemplo, verá que ele possui um menor clock, e o mesmo número de ", 19, x_text, self.y_text + 80)    
            self.game.draw_text("núcleos e threads do Pentium dessa questão.", 19, x_text, self.y_text + 100) 
        if layer == 101:
            wro, wri = False, False
            x, y = 0, 0
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/q12.png'), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/up_bar.png'), (0, 0))
            self.game.draw_text("Jozé, seu outro amigo, quer comprar um processador para", 19, 195, 30)
            self.game.draw_text("o montar o seu computador de mesa para jogar video games", 19, 195, 50)
            self.game.draw_text("e edição de vídeos daquilo que ele joga e quer pegar", 19, 195, 70)
            self.game.draw_text("um processador de até 2000 reais (todas as opções estão ", 19, 195, 90)
            self.game.draw_text("dentro desse orçamento).", 19, 195, 110)
            self.game.draw_text("Qual destes processadores você indicaria para Jozé?", 19, 195, 130)
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if not self.sheet[0] and not self.sheet[1] and not self.sheet[2] and not self.sheet[3]:
                            if 348 > mx > 20 and 266 > my > 198:
                                wro = True
                                x, y = 20, 198
                            elif 348 > mx > 20 and 344 > my > 276:
                                wri = True
                                x, y = 20, 276
                            elif 827 > mx > 499 and 268 > my > 200:
                                wro = True
                                x, y = 499, 200
                            elif 827 > mx > 499 and 346 > my > 278:
                                wro = True
                                x, y = 499, 278
                            if 411 > mx > 349 and 228 > my > 192:
                                self.sheet[0] = True
                            elif 411 > mx > 349 and 308 > my > 272:
                                self.sheet[1] = True
                            elif 890 > mx > 828 and 225 > my > 189:
                                self.sheet[2] = True
                            elif 890 > mx > 828 and 310 > my > 272:
                                self.sheet[3] = True
                        if (self.sheet[0] or self.sheet[1] or self.sheet[2] or self.sheet[3]) and 740 > mx > 661 and 149 > my > 102:
                            self.sheet[0], self.sheet[1], self.sheet[2], self.sheet[3] = False, False, False, False
            if self.sheet[0]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/corei7-6700K.png'), (176, 60))
            if self.sheet[1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/corei5-10600K.png'), (176, 60))
            if self.sheet[2]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/corei5-9600k.png'), (176, 60))
            if self.sheet[3]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/corei3-10100F.png'), (176, 60))

            if wro:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/wrong_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/Bar_5_r.png'), (x, y))
                if self.count_click >= 5:
                    wro = False
                    self.count_click = 0
            if wri and not wro:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.count_click += 1
                self.game.display.blit(pygame.image.load('data/img/Bar_5_g.png'), (x, y))
                if self.count_click >= 1:
                    self.i += 1
                    self.layers.append(self.i)
                    self.gamimg_layer = False
                    self.game.reset_keys()
                    self.score.count = 0
                    self.score.scr = 0
                    for i in range(0, 2):
                        self.score.alternatives(i, 1)
                    self.count_click = 0
        if layer == 102:
            self.draw_very_good()
        if layer == 103:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/i7-6700K.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("As finalidades dos processadores são informadas na última letra do nome do", 19, x_text, self.y_text)
            self.game.draw_text("processador como, por exemplo, Intel Core i7-6700K.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Esse K indica que o processador tem especificações que a empresa informa como", 19, x_text, self.y_text + 40)
            self.game.draw_text("necessárias para fazer um overclock sem grandes problemas.", 19, x_text, self.y_text + 60)
        if layer == 104:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/overclock.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Overclock é um método de aumentar a frequência do clock do processador ou de", 19, x_text, self.y_text)
            self.game.draw_text("um hardware cujo funcionamento está na base de ciclos, como a memória RAM,", 19, x_text, self.y_text + 20)
            self.game.draw_text("HDs, monitores e processadores.", 19, x_text, self.y_text + 40)
        if layer == 105:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/overclock_2.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Esse método pode ser prejudicial ao hardware pois aumenta o seu desgaste", 19, x_text, self.y_text)
            self.game.draw_text("com um consumo e um uso excessivo da capacidade máxima, além de ", 19, x_text, self.y_text + 20)
            self.game.draw_text("aumentar o calor interno da peça, por isso que muitas empresas não ", 19, x_text, self.y_text + 40)
            self.game.draw_text("recomendam o uso dessa configuração a todo momento.", 19, x_text, self.y_text + 60)
        if layer == 106:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/turbo_boost.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Mas há como utilizá-la quando for necessário. Esse é o caso da tecnologia ", 19, x_text, self.y_text)
            self.game.draw_text("Turbo boosting da Intel que aciona um overclock quando uma aplicação requer ", 19, x_text, self.y_text + 20)
            self.game.draw_text("um maior nível de processamento momentâneo.", 19, x_text, self.y_text + 40)
        if layer == 107:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/linha.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Além da letra K, os processadores da linha “i” possuem especificações “U”, que é", 19, x_text, self.y_text)
            self.game.draw_text("para notebooks, pois utiliza um baixo consumo de energia; a especificação “T” que ", 19, x_text, self.y_text + 20)
            self.game.draw_text("é utilizada para processadores com um baixo consumo de energia, mas para", 19, x_text, self.y_text + 40)
            self.game.draw_text("computadores de mesa (também chamados de desktops); a especificação “Q” que", 19, x_text, self.y_text + 60)
            self.game.draw_text("é utilizada para processadores com 4 núcleos físicos, entre outras letras.", 19, x_text, self.y_text + 80)
        if layer == 108:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/vs_intel.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Depois de ver essas classificações, aqui vai um exemplo da diferença ", 19, 255, self.y_text)
            self.game.draw_text("de gerações em processadores:", 19, 255, self.y_text + 20)
            self.game.draw_text("Um Intel Core i7-7820HK e um Intel Core i5-9400H. ", 19, 255, self.y_text + 40)
            self.game.draw_text("Qual você acha que é melhor?", 19, 255, self.y_text + 60)
        if layer == 109:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/intel_i5.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("De fato esse i5 possui uma especificação melhor do que o i7. Ambos possuem 4", 19, x_text, self.y_text)
            self.game.draw_text("núcleos e 8 threads (tecnologia multi-threading da Intel), mas o clock máximo do i7 é", 19, x_text, self.y_text + 20)
            self.game.draw_text("de 3.90 GHz, enquanto que o do i5 é de 4.30 GHz, além disso, o processador i5 da", 19, x_text, self.y_text + 40)
            self.game.draw_text("nona geração possui uma compatibilidade com frequências de memória RAM mais", 19, x_text, self.y_text + 60)
            self.game.draw_text("altas do que os processadores da 7ª geração, que permitiam uma frequência", 19, x_text, self.y_text + 80)
            self.game.draw_text("máxima para a memória RAM de 2400 MHz.", 19, x_text, self.y_text + 100)
        if layer == 110:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/cpu_placa_de_video.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Outra coisa a ser falada é que, com o avanço da tecnologia, alguns processadores", 19, x_text, self.y_text)
            self.game.draw_text("possuem uma placa de vídeo integrada neles, chamada de placa de vídeo onboard", 19, x_text, self.y_text + 20)
            self.game.draw_text("(também pode vir integrada à placa-mãe). Diferente da placa de vídeo ligada ao slot", 19, x_text, self.y_text + 40)
            self.game.draw_text("PCI-Express, também chamada de placa de vídeo dedicada ou offboard, essa placa", 19, x_text, self.y_text + 60)
            self.game.draw_text("integrada utiliza a própria memória RAM ligada ao slot da placa-mãe como", 19, x_text, self.y_text + 80)
            self.game.draw_text("armazenamento de memória, dividindo espaço com o processador.", 19, x_text, self.y_text + 100)
        if layer == 111:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/hd_graphics.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Esses processadores são uma alternativa de menor custo ", 19, 250, self.y_text)
            self.game.draw_text("financeiro para quem quiser utilizar conteúdo de vídeo, mas, ", 19, 250, self.y_text + 20)
            self.game.draw_text("até agora, não chegam perto da capacidade de uma placa de vídeo dedicada de alto", 19, x_text, self.y_text + 40)
            self.game.draw_text("nível. A Intel HD Graphics é a placa de vídeo integrada da Intel. Ela está presente ", 19, x_text, self.y_text + 60)
            self.game.draw_text("em diversos processadores da linha i, principalmente em notebooks.", 19, x_text, self.y_text + 80)
        if layer == 112:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s3/end.png'), (0, 0))
            text = 'FasesWone='
            a = open('c:\ProtTech\data\data.txt', 'r')
            b = a.read()
            a2 = open('c:\ProtTech\data\data.txt', 'rt+')
            s = a2.readlines()[2]
            a2.close()
            if (text + "True,True,True,False") in s:
                b = b.replace(text + "True,True,True,False", text + "True,True,True,True", 1)
                a = open('c:\ProtTech\data\data.txt', 'w')
                a.write(b)
                a.close()
            pygame.display.update()


    def current_layer(self):
        self.run_layer(self.layers[len(self.layers) - 1])

    def display_m(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_inputs()
            self.game.display = pygame.image.load('data/img/worlds/w1/s1/Fundo.png')
            self.current_layer()
            self.game.draw_score()
            self.blit_screen()
            
