import pygame, time
from data.score import *
from pygame.locals import *
from data.questions import *


class Fases01():
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


class FaseOneWorldOne(Fases01):
    def __init__(self, game):
        self.i = 1
        self.layers = [1]
        self.not_fading = True
        self.wrong, self.wright = False, False
        self.score = Score()
        self.margin_reg = "right"
        self.area = dict()
        self.state = "1"
        self.area['1'] = {'x': 53, 'y': 145}
        self.area['2'] = {'x': 359, 'y': 145}
        self.area['3'] = {'x': 664, 'y': 145}
        self.bx, self.by = self.area['1']['x'], self.area['1']['y']
        self.answer = dict()
        self.answer = {'5': 1, '6': 1, '7': 3, '11': 2, '12': 1, '13': 2, '18':1, '25':1, '35':1, '38':1, '39':1, '40':1, '48':1, '49':3, '50':3, '51':1, '52':3, '53':3, '54':1, '55':1}
        self.clicking = 0
        self.q = Questions(0)
        self.right_clicking = False
        self.n, self.count = 0, 0
        self.sound_event = False
        self.sheet_event = [False, False, False]
        self.finish = False
        Fases01.__init__(self, game)

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
        if self.game.RIGHT_KEY:
            self.wright = False
            self.wrong = False
            if self.layers[len(self.layers) -1] < 47:
                if self.state == "1":
                    self.bx, self.by = self.area['2']['x'], self.area['2']['y']
                    self.state = "2"
                elif self.state == "2":
                    self.bx, self.by = self.area['3']['x'], self.area['3']['y']
                    self.state = "3"
                elif self.state == "3":
                    self.bx, self.by = self.area['1']['x'], self.area['1']['y']
                    self.state = "1"
            else:
                if self.state == "1":
                    self.bx, self.by = self.area['3']['x'], self.area['3']['y']
                    self.state = "3"
                elif self.state == "3":
                    self.bx, self.by = self.area['1']['x'], self.area['1']['y']
                    self.state = "1"
        if self.game.LEFT_KEY:
            self.wright = False
            self.wrong = False
            if self.layers[len(self.layers) -1] < 47:
                if self.state == "1":
                    self.bx, self.by = self.area['3']['x'], self.area['3']['y']
                    self.state = "3"
                elif self.state == "2":
                    self.bx, self.by =self.area['1']['x'], self.area['1']['y']
                    self.state = "1"
                elif self.state == "3":
                    self.bx, self.by = self.area['2']['x'], self.area['2']['y']
                    self.state = "2"
            else:
                if self.state == "1":
                    self.bx, self.by = self.area['3']['x'], self.area['3']['y']
                    self.state = "3"
                elif self.state == "3":
                    self.bx, self.by = self.area['1']['x'], self.area['1']['y']
                    self.state = "1"

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
            if not self.gamimg_layer:
                self.q = Questions(0)
                self.game.current_menu = self.game.fases_1
                self.run_display = False
                self.gaming_layer = False
                self.game.reset_keys()
                self.state = '1'
                self.bx, self.by = self.area['1']['x'], self.area['1']['y']
                self.layers.clear()
                self.i = 1
                self.layers.append(1)
        if self.game.SPACE_KEY and self.layers[len(self.layers) - 1] != 18 and self.layers[len(self.layers) - 1] != 25 and self.layers[len(self.layers) - 1] != 35 and self.layers[len(self.layers) - 1] != 38  and self.layers[len(self.layers) - 1] != 39  and self.layers[len(self.layers) - 1] != 40:
            if not self.gamimg_layer and self.layers[len(self.layers) - 1] != 58:
                self.i += 1
                self.layers.append(self.i)
                self.ok = True
            if self.gamimg_layer:
                if self.layers[len(self.layers) - 1] != 18 and self.layers[len(self.layers) - 1] != 25:
                    wri_wro = self.score.alternatives(self.answer[str(self.layers[len(self.layers) - 1])], int(self.state))
                    if wri_wro:
                        self.wright = True
                        if self.wright:
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                            pygame.mixer.Channel(1).set_volume(0.04)
                            self.i += 1
                            self.layers.append(self.i)
                            self.gamimg_layer = False
                            self.game.reset_keys()
                            self.state = '1'
                            self.bx, self.by = self.area['1']['x'], self.area['1']['y']
                            self.score.count = 0
                            self.score.scr = 0
                    else:
                        self.wrong = True
                        if self.wrong:
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/wrong_answer.mp3'))
                            pygame.mixer.Channel(1).set_volume(0.04)
            if not self.gamimg_layer and self.layers[len(self.layers) - 1] == 58:
                self.game.current_menu = self.game.fases_1
                self.run_display = False
                self.gaming_layer = False
                self.game.reset_keys()
                self.state = '1'
                self.bx, self.by = self.area['1']['x'], self.area['1']['y']
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

    def selected_question(self):
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
                self.score.alternatives(self.answer[str(self.layers[len(self.layers) - 1])], 2)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/wrong_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.07)
                # self.feed = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
                for i in range(0, len(self.q.feed)):
                    for j in range(0, 2):
                        self.q.feed[i][j] = 0
                self.n, self.count = 0, 0
                pygame.time.wait(1650)
            if self.count == len(self.q.feed):
                self.score.alternatives(self.answer[str(self.layers[len(self.layers) - 1])], 1)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.i += 1
                self.layers.append(self.i)
                self.gamimg_layer = False
                self.game.reset_keys()
                self.state = '1'
                self.bx, self.by = self.area['1']['x'], self.area['1']['y']
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

    def draw_beep(self, audio, x1, x0, y1, y0, mark,shev):
        mx, my = pygame.mouse.get_pos()
        self.gamimg_layer = True
        self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
        self.game.draw_text("Você terá que identificar a marca da BIOS e a partir", 20, 220, 35)
        self.game.draw_text("daí terá que ver qual foi o problema. Depois, marque", 20, 220, 55)
        self.game.draw_text("qual foi o problema encontrado.", 20, 315, 75)
        self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/ligar_computador.png'), (320, 115))
        if mark == "AWARD":
            self.game.draw_text("AWARD", 8, 390, 150)
        else:
            self.game.draw_text(mark, 8, 473, 273)
        if not self.sound_event and not self.sheet_event[0] and not self.sheet_event[1] and not self.sheet_event[2]:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/logan_ligar_computador.png'), (320, 115))
            self.game.draw_text("-Ligue o computador por aqui.", 17, 585, 130)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if 496 > mx > 473 and 256 > my > 237 and not self.sheet_event[0] and not self.sheet_event[1] and not \
                        self.sheet_event[2]:
                    if event.button == 1:
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(audio))
                        pygame.mixer.Channel(1).set_volume(0.05)
                        self.sound_event = True
                if 240 > mx > 80 and 470 > my > 353 and not self.sheet_event[1] and not self.sheet_event[2]:
                    if event.button == 1:
                        self.sheet_event[0] = True
                if 555 > mx > 395 and 470 > my > 353 and not self.sheet_event[0] and not self.sheet_event[2]:
                    if event.button == 1:
                        self.sheet_event[1] = True
                if 898 > mx > 718 and 470 > my > 353 and not self.sheet_event[0] and not self.sheet_event[1]:
                    if event.button == 1:
                        self.sheet_event[2] = True
                if 768 > mx > 700 and 139 > my > 100:
                    if event.button == 1:
                        for i in range(0, 3):
                            if self.sheet_event:
                                self.sheet_event[i] = False
                if x1 > mx > x0 and y1 > my > y0 and self.sheet_event[shev]:
                    self.score.alternatives(self.answer[str(self.layers[len(self.layers) - 1])], 1)
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                    pygame.mixer.Channel(1).set_volume(0.04)
                    self.i += 1
                    self.layers.append(self.i)
                    self.gamimg_layer = False
                    self.game.reset_keys()
                    self.state = '1'
                    self.bx, self.by = self.area['1']['x'], self.area['1']['y']
                    self.sound_event = False
                    self.score.count = 0
                    self.score.scr = 0
                    for i in range(0, 3):
                        if self.sheet_event:
                            self.sheet_event[i] = False
        self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/sheet_AWARD_i.png'), (80, 353))
        self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/sheet_DELL_i.png'), (395, 353))
        self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/sheet_IBM_i.png'), (718, 353))
        if self.sheet_event[0]:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/sheet_AWARD.png'), (200, 45))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/exit.png'), (700, 100))
        if self.sheet_event[1]:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/sheet_DELL.png'), (200, 45))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/exit.png'), (700, 100))
        if self.sheet_event[2]:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/sheet_IBM.png'), (200, 45))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/exit.png'), (700, 100))

    def run_layer(self, layer):
        if layer == 1:
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Olá, eu sou Logan! Serei seu tutor nesta jornada de aprendizado", self.font_size, x_text, self.y_text)
            self.game.draw_text("de segurança e manutenção de diversas tecnologias. Vamos começar?", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("[PRESSIONE ESPAÇO PARA SEGUIR.]", self.font_size, x_text, self.y_text + 60)
        if layer == 2:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/hardware_vs_software.png'), (169, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Primeiro, você vai aprender um pouco sobre hardware e software e depois ", self.font_size, x_text, self.y_text)
            self.game.draw_text("aprenderá a como protegê-los e cuidá-los.", self.font_size, x_text, self.y_text + 20)
        if layer == 3:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/hardware_conceito_1.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O termo hardware é designado para referenciar qualquer ", self.font_size, 261, self.y_text)
            self.game.draw_text("parte física de um componente de capacidades operacionais", self.font_size, 261, self.y_text + 20)
            self.game.draw_text("computacionais.", self.font_size, 261, self.y_text + 40)
        if layer == 4:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/hardware_conceito_2.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Resumindo, é qualquer componente físico que tenha relação ", self.font_size, x_text, self.y_text)
            self.game.draw_text("com o computador. Vamos testar seu conhecimento prévio no ", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("assunto e com base na definição.", self.font_size, self.margin_left if self.margin_reg == "left" else self.margin_right, self.y_text + 40)
        if layer == 5:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Selecione apenas o que for hardware:", 26, 243, 45)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q1.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 6:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Selecione apenas o que for hardware:", 26, 243, 45)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q2.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 7:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Selecione apenas o que for hardware:", 26, 243, 45)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q3.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 8:
            self.draw_very_good()
        if layer == 9:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/software_conceito.png'), (206, 18))
            self.base_layer(layer)
            self.game.draw_text("Agora vamos ver o segundo conceito essencial para", self.font_size, 261, self.y_text)
            self.game.draw_text("computadores, software. Um software consiste em uma ", self.font_size, 261, self.y_text + 20)
            self.game.draw_text("sequência de instruções lógicas que descrevem tarefas ", self.font_size, 261, self.y_text + 40)
            self.game.draw_text("a serem realizadas por um  computador, por exemplo, a", self.font_size, 261, self.y_text + 60)
            self.game.draw_text("manipulação, redirecionamento ou a modificação", self.font_size, 261, self.y_text + 80)
            self.game.draw_text("de dados.", self.font_size, 261, self.y_text + 100)
        if layer == 10:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/software_conceito_2.png'), (275, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Os componentes de Hardware de um computador são controlados através ", self.font_size, x_text, self.y_text)
            self.game.draw_text("de software. Sem um software, o computador se torna uma peça de", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("metal inoperante. Resumindo, software é a parte operacional lógica do", self.font_size, x_text, self.y_text + 40)
            self.game.draw_text("computador.", self.font_size, x_text, self.y_text + 60)
            self.game.draw_text("Vamos testar seu conhecimento prévio no assunto ", self.font_size, x_text,self.y_text + 80)
            self.game.draw_text("e com base na definição.", self.font_size, x_text, self.y_text + 100)
        if layer == 11:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Selecione apenas o que for software:", 26, 243, 45)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q4.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 12:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Selecione apenas o que for software:", 26, 243, 45)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q5.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 13:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Selecione apenas o que for software:", 26, 243, 45)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q6.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 14:
            self.draw_very_good()
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
        if layer == 15:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/processador.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Os componentes de hardware mais importante de um computa-", self.font_size, 249, self.y_text)
            self.game.draw_text("dor são: O processador, as memórias e os dispositivos de en-", self.font_size, 249, self.y_text + 20)
            self.game.draw_text("trada e saída. O processador é um tipo de microchip e, basica-", self.font_size, 249, self.y_text + 40)
            self.game.draw_text("mente sua função é de executar operações lógicas", self.font_size, 249, self.y_text + 60)
            self.game.draw_text("e aritméticas.", self.font_size, 249, self.y_text + 80)
        if layer == 16:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/memoria_dispositivos_io.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("As memórias são dispositivos que permitem o computador armazenar dados de ", 19, x_text, self.y_text)
            self.game.draw_text("maneira temporária ou permanente. ", 19, x_text, self.y_text + 20)
            self.game.draw_text("Os dispositivos de entrada e saída são qualquer coisa que possibilita a interação ", 19, x_text, self.y_text + 40)
            self.game.draw_text("da máquina com o usuário, como impressoras, teclados, mouses e monitores.", 19, x_text, self.y_text + 60)
            self.game.draw_text("", 19, x_text, self.y_text + 80)
        if layer == 17:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/placa_mae.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Esses componentes são alocados em uma placa-mãe do computador. ", 19, x_text, self.y_text)
            self.game.draw_text("Cada um desses componentes serão melhor explicados ao longo da fase.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Vamos testar seu conhecimento com base nessas definições...", 19, x_text, self.y_text + 80)
            self.q = Questions(18)
        if layer == 18:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Relacione cada função a um componente:", 24, 240, 45)
            self.game.draw_text("[UTILIZE O MOUSE]", 19, 380, 75)
            self.game.display.blit(pygame.image.load(self.q.image), (0, 0))
            self.game.draw_text("Calcular uma operação", 23, 70, 138)
            self.game.draw_text("Ligar vários componentes", 23, 67, 220)
            self.game.draw_text("Guardar um documento", 23, 70, 295)
            self.game.draw_text("Visualizar um aplicativo", 23, 67, 379)
            self.game.draw_text("Scanner de documentos", 23, 70, 455)
            self.game.draw_text("memória", 23, 630, 138)
            self.game.draw_text("processador", 23, 610, 220)
            self.game.draw_text("dispositivo de entrada", 23, 550, 295)
            self.game.draw_text("dispositivo de saída", 23, 564, 379)
            self.game.draw_text("placa mãe", 23, 628, 455)
            self.selected_question()
            pygame.display.update()
        if layer == 19:
            self.draw_very_good()
        if layer == 20:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/software_conceito_2.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os softwares são em essência algoritmos, ou seja, sequências de instruções", 19, x_text, self.y_text)
            self.game.draw_text("lógicas que descrevem tarefas a serem realizadas. Porém essas tarefas devem ", 19, x_text, self.y_text + 20)
            self.game.draw_text("ser realizadas por um computador, como a manipulação, redirecionamento", 19, x_text, self.y_text + 40)
            self.game.draw_text("ou modificação de dados.", 19, x_text, self.y_text + 60)
        if layer == 21:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/linguagens.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Esses algoritmos precisam ser compreendidos para serem executados, atualizados", 19, x_text, self.y_text)
            self.game.draw_text("ou desinstalados e para isso é necessário uma  linguagem de programação.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Os softwares podem ser classificados em três tipos:", 19, x_text, self.y_text + 40)
            self.game.draw_text("firmware, Sistema Operacional e Aplicativo.", 19, x_text, self.y_text + 60)
        if layer == 22:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/BIOS.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O firmware é um software de baixo nível armazenado permanentemente durante a", 19, x_text, self.y_text)
            self.game.draw_text("fabricação de um chip. O firmware mais comum é o Basic Input/Output System ", 19, x_text, self.y_text + 20)
            self.game.draw_text("(bios), e sua função é identificar os componentes de hardware conectados ", 19, x_text, self.y_text + 40)
            self.game.draw_text("ao computador.", 19, x_text, self.y_text + 60)
        if layer == 23:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/SOs.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os sistemas operacionais (SO) são o segundo tipo de software, o tipo intermediário.", 19, x_text, self.y_text)
            self.game.draw_text("Eles funcionam como uma camada localizada entre os componentes físicos e os", 19, x_text, self.y_text + 20)
            self.game.draw_text("programas de aplicativos. Os sistemas operacionais mais comuns para ", 19, x_text, self.y_text + 40)
            self.game.draw_text("computadores desktop são o Windows, Linux e MacOS.", 19, x_text, self.y_text + 60)
        if layer == 24:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/Programas.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Os programas aplicativos consistem em softwares de alto nível.", 19, 261, self.y_text)
            self.game.draw_text("Eles são desenvolvidos para serem utilizados diretamente pelos", 19, 261, self.y_text + 20)
            self.game.draw_text("usuários com a utilização do sistema operacional, como um editor", 19, 261, self.y_text + 40)
            self.game.draw_text("de texto, um navegador Web ou reprodutores de áudio/vídeo.", 19, 261, self.y_text + 60)
        if layer == 24:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/Programas.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Os programas aplicativos consistem em softwares de alto nível.", 19, 261, self.y_text)
            self.game.draw_text("Eles são desenvolvidos para serem utilizados diretamente pelos", 19, 261, self.y_text + 20)
            self.game.draw_text("usuários com a utilização do sistema operacional, como um editor", 19, 261, self.y_text + 40)
            self.game.draw_text("de texto, um navegador Web ou reprodutores de áudio/vídeo.", 19, 261, self.y_text + 60)
            self.game.draw_text("Vamos testar seu conhecimento com base nessas definições:", 19, 261, self.y_text + 80)
            self.q = Questions(25)
        if layer == 25:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Relacione cada função a um componente:", 24, 240, 45)
            self.game.display.blit(pygame.image.load(self.q.image), (0, 0))
            self.game.draw_text("Identifica memória", 23, 173, 182)
            self.game.draw_text("instalado no", 23, 210, 202)
            self.game.draw_text("computado", 23, 217, 222)
            self.game.draw_text("Photoshop", 23, 216, 304)
            self.game.draw_text("(Editor de foto)", 23, 190, 331)
            self.game.draw_text("Kali Linux", 23, 220, 423)
            self.game.draw_text("Firmware", 23, 628, 423)
            self.game.draw_text("Programa", 23, 624, 202)
            self.game.draw_text("Sistema Operacional",23, 560, 316)
            self.selected_question()
            pygame.display.update()
        if layer == 26:
            self.draw_very_good()
        if layer == 27:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/boot.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Agora que você sabe um pouco sobre os conceitos gerais, podemos ", 19, 261, self.y_text)
            self.game.draw_text("mostrar o processo de inicialização de um computador, o processo ", 19, 261, self.y_text + 20)
            self.game.draw_text("de boot.", 19, 261, self.y_text + 40)
            self.game.draw_text("Saber o passo a passo da inicialização de um computador é", 19, 261, self.y_text + 60)
            self.game.draw_text("essencial para a identificação de erros.", 19, 261, self.y_text + 80)
        if layer == 28:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/CMOS.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Primeiro, ao ligar o botão ou a chave do computador, a BIOS acessa a memória", 19, x_text, self.y_text)
            self.game.draw_text("metal-óxido-semicondutor complementar, ou CMOS, onde estão armazenadas as", 19, x_text, self.y_text + 20)
            self.game.draw_text("informações referentes à placa-mãe e seus hardwares interligados.", 19, x_text, self.y_text + 40)
        if layer == 29:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/problema_processador.png'), (215, 17))
            self.game.draw_text("Para essa BIOS da marca AMI, 5 beeps curtos", 19, 285, 68)
            self.game.draw_text("significam problema no processador.", 19, 285, 88)
            self.base_layer(layer)
            if self.game.ok_sound:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/ouvir_01.png'), (393, 280))
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/5beeps.mp3'))
                pygame.mixer.Channel(1).set_volume(0.05)
            else:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/ouvir_02.png'), (393, 280))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois, a BIOS compara os dados para verificar a presença e o bom funcionamento", 19, x_text, self.y_text)
            self.game.draw_text("dos hardwares para então iniciar o SO. Se algum componente não estiver", 19, x_text, self.y_text + 20)
            self.game.draw_text("funcionando adequadamente ou estiver faltando, a BIOS emite beeps ou imprime  ", 19, x_text, self.y_text + 40)
            self.game.draw_text("mensagens na tela do computador para alertar o problema identificado.", 19, x_text, self.y_text + 60)
        if layer == 30:
            self.game.ok_sound = False
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/marcas_BIOS.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os beeps e mensagens variam de acordo com a marca da peça.", 19, x_text, self.y_text)
            self.game.draw_text("Então para verificar o problema, é preciso saber a marca do ", 19, x_text, self.y_text + 20)
            self.game.draw_text("hardware. Aqui estão algumas marcas de BIOS:", 19, x_text, self.y_text + 40)
            self.game.draw_text("AWARD, IBM, MACINTOSH, PHOENIX, AMI, MrBIOS, UNICORE e  TTI.", 19, x_text, self.y_text + 80)
        if layer == 31:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/Armazenamento.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois da verificação do hardware, a BIOS verifica em qual mídia o sistema ", 19, x_text, self.y_text)
            self.game.draw_text("operacional está armazenado para poder ligá-lo, podendo ser uma mídia interna,", 19, x_text, self.y_text + 20)
            self.game.draw_text("como HD, SSD ou uma mídia externa, como um cd/dvd-rom ou o pendrive", 19, x_text, self.y_text + 40)
            self.game.draw_text("(Esses hardwares serão abordados  mais à frente).", 19, x_text, self.y_text + 60)
        if layer == 32:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/MBR.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Se for uma mídia interna, a BIOS lerá o primeiro setor de armazenamento ", 19, x_text, self.y_text)
            self.game.draw_text("(setor zero), chamado mbr (Master Boot Record). Essa área armazena um código ", 19, x_text, self.y_text + 20)
            self.game.draw_text("que ao ser lido, possibilita a inicialização do sistema operacional.", 19, x_text, self.y_text + 40)
            self.game.draw_text("O mbr realiza uma leitura de um arquivo de boot, ou Boot Loader, que tem a", 19, x_text, self.y_text + 70)
            self.game.draw_text("função de descrever as opções de carregamento do sistema.", 19, x_text, self.y_text + 90)
        if layer == 33:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/kernel.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Após o carregamento das opções de inicialização do SO, a BIOS inicia", 19, 243, self.y_text)
            self.game.draw_text("o núcleo do sistema operacional que é chamado de kernel. Ele faz uma", 19, 243, self.y_text + 20)
            self.game.draw_text("ligação direta entre os componentes de hardware e o sistema.", 19, 243, self.y_text + 40)
            self.game.draw_text("O kernel carrega os arquivos principais e informações básicas do sistema", 19, 139, self.y_text + 70)
            self.game.draw_text("operacional e relaciona os componentes de hardware com os seus drives.", 19, 139, self.y_text + 90)
        if layer == 34:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/inicializacao.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Após o carregamento dos arquivos e a linkagem dos componentes com os ", 19, x_text, self.y_text)
            self.game.draw_text("seus drivers, o computador inicia o sistema operacional.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Vamos testar seu conhecimento com base no que foi aprendido sobre boot", 19, x_text, self.y_text + 70)
            self.game.draw_text("de um computador...", 19, x_text, self.y_text + 90)
            self.q = Questions(35)
        if layer == 35:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Ponha na ordem de acontecimento os", 24, 253, 35)
            self.game.draw_text("processos de boot até a inicialização do SO:", 24, 220, 65)
            self.game.display.blit(pygame.image.load(self.q.image), (0, 0))
            self.game.draw_text("Verificação da mídia", 23, 100, 287)
            self.game.draw_text("   onde está o SO", 23, 115, 313)
            self.game.draw_text("Leitura do boot loader", 23, 89, 379)
            self.game.draw_text("Ligação da BIOS e acesso", 23, 70, 445)
            self.game.draw_text("              ao CMOS", 23, 70, 470)
            self.game.draw_text(" Iniciação do kernel", 23, 550, 295)
            self.game.draw_text("Verificação de hardware", 23, 518, 379)
            self.game.draw_text("Leitura do mbr", 23, 580, 455)
            self.selected_question()
            pygame.display.update()
        if layer == 36:
            self.draw_very_good()
        if layer == 37:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/marcas_BIOS.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Agora você terá que identificar o erro de um computador pela BIOS. Cada ", 19, 139,
                                self.y_text)
            self.game.draw_text("fabricante disponibiliza em seu site uma lista da relação entre os beeps e ", 19, 139,
                                self.y_text + 20)
            self.game.draw_text("a falha que ocorreu durante a inicialização do computador.", 19, 139,
                                self.y_text + 40)
        if layer == 38:
            self.draw_beep('data/aud/dell.mp3', 727, 226, 348, 319, "DELL",1)
            pygame.display.update()
        if layer == 39:
            self.draw_beep('data/aud/award.mp3', 766, 228, 399, 326, "AWARD",0)
            pygame.display.update()
        if layer == 40:
            self.draw_beep('data/aud/ibm.mp3',768,230,320,299, 'IBM',2)
            pygame.display.update()
        if layer == 41:
            self.draw_very_good()
        if layer == 42:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/UEFI.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Você acabou de ver o modo de inicialização mais comum dos computadores,", 19, x_text,
                                self.y_text)
            self.game.draw_text("mas atualmente há outra forma de boot além da BIOS, a UEFI.", 19, x_text,
                                self.y_text + 20)
            self.game.draw_text("A UEFI, sigla para Interface Unificada de Firmware Extensível, como o próprio ", 19, x_text,
                                self.y_text + 70)
            self.game.draw_text("nome já diz, é uma interface que possui mais aplicações no firmware.", 19, x_text, self.y_text + 90)
        if layer == 43:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/UEFI.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A sua aplicação mais comum para o usuário é a interface de configuração da", 19, x_text,
                                self.y_text)
            self.game.draw_text("inicialização do computador, mas também possui um caminho diferente de ", 19, x_text,
                                self.y_text + 20)
            self.game.draw_text("inicialização do SO. ", 19, x_text,
                                self.y_text + 40)
        if layer == 44:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/UEFI_vs_Legacy.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Primeiro, um computador no modo UEFI já possui um boot mais rápido do que ", 19, x_text, self.y_text)
            self.game.draw_text("inicializando pelo modo da BIOS, chamado de Legacy. Além disso, o UEFI possui ", 19, x_text, self.y_text + 20)
            self.game.draw_text("maior proteção devido ao recurso de criptografia (que não está presente na BIOS). ", 19, x_text,self.y_text + 40)
        if layer == 45:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/GTP_vs_MBR.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Em um computador com UEFI é possível utilizar outro padrão além do", 19,249, self.y_text)
            self.game.draw_text(" mbr onde está instalado o SO. Esse padrão é o GPT. A sigla significa ", 19, 249, self.y_text + 20)
            self.game.draw_text("Tabela de Partição GUID. O GPT é mais encontrado em sistemas com ", 19, 249, self.y_text + 40)
            self.game.draw_text("Windows 10. Ele funciona como uma atualização do MBR, pois possui ", 19, 249, self.y_text + 60)
            self.game.draw_text("melhores funcionalidades. ", 19, 249, self.y_text + 80)
        if layer == 46:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/GTP_vs_MBR.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Algumas das funcionalidades melhoradas do GPT em comparação como MBR são:", 19,x_text,self.y_text)
            self.game.draw_text("Maior capacidade de partição. No formato mbr o valor máximo de partição é de 2", 19, x_text,self.y_text + 20)
            self.game.draw_text("terabytes. Já o gtp, o valor máximo por partição é de 9.4 bilhões de terabytes.", 19, x_text,self.y_text + 40)
            self.game.draw_text("Maior número de partições primárias. No formato mbr a quantidade máxima de ", 19,x_text,self.y_text + 60)
            self.game.draw_text("partições são 4. Já no gtp, são 128.", 19, x_text, self.y_text + 80)
        if layer == 47:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/UEFI_vs_BIOS.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Um dos motivos do modelo UEFI ser mais rápido que a inicialização via BIOS é a ", 19,x_text,self.y_text)
            self.game.draw_text("leitura do gtp, que possui o boot loader com a extensão própria, sendo essa ", 19, x_text,self.y_text + 20)
            self.game.draw_text("a diferença de inicialização da BIOS para UEFI.", 19, x_text,self.y_text + 40)
            self.game.draw_text("", 19,x_text,self.y_text + 60)
            self.game.draw_text("Vamos testar seu conhecimento com base nessas definições:", 19, x_text, self.y_text + 80)
        if layer == 48:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text(" Relacione as características de UEFI", 26, 243, 30)
            self.game.draw_text("         e da BIOS:", 26, 360, 60)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/bar_10.png'), (289, 406))
            self.game.draw_text("    Realiza o Boot mais rápido", 22, 320, 426)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q10.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 49:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text(" Relacione as características de UEFI", 26, 243, 30)
            self.game.draw_text("         e da BIOS:", 26, 360, 60)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/bar_10.png'), (289, 406))
            self.game.draw_text("     Limite de partição de 2TB", 22, 320, 426)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q10.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 50:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text(" Relacione as características de UEFI", 26, 243, 30)
            self.game.draw_text("         e da BIOS:", 26, 360, 60)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/bar_10.png'), (289, 406))
            self.game.draw_text("     Até 4 partições primárias", 22, 320, 426)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q10.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 51:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text(" Relacione as características de UEFI", 26, 243, 30)
            self.game.draw_text("         e da BIOS:", 26, 360, 60)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/bar_10.png'), (289, 406))
            self.game.draw_text("   Limite de partição de 9.4ZB", 22, 320, 416)
            self.game.draw_text("       (1 zp = 1 bilhão de TB)", 22, 320, 438)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q10.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 52:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text(" Relacione as características de UEFI", 26, 243, 30)
            self.game.draw_text("         e da BIOS:", 26, 360, 60)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/bar_10.png'), (289, 406))
            self.game.draw_text("          Padrão mbr", 22, 360, 426)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q10.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 53:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text(" Relacione as características de UEFI", 26, 243, 30)
            self.game.draw_text("         e da BIOS:", 26, 360, 60)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/bar_10.png'), (289, 406))
            self.game.draw_text("Realiza o Boot mais lento", 22, 340, 426)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q10.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 54:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text(" Relacione as características de UEFI", 26, 243, 30)
            self.game.draw_text("         e da BIOS:", 26, 360, 60)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/bar_10.png'), (289, 406))
            self.game.draw_text("          Padrão gpt", 22, 360, 426)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q10.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 55:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text(" Relacione as características de UEFI", 26, 243, 30)
            self.game.draw_text("         e da BIOS:", 26, 360, 60)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/bar_10.png'), (289, 406))
            self.game.draw_text(" Até 128 partições primárias", 22, 340, 426)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/q10.png'), (0, 0))
            self.draw_cursor()
            pygame.display.update()
        if layer == 56:
            self.draw_very_good()
            pygame.display.update()
        if layer == 57:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/end.png'), (0, 0))
            text = 'FasesWone='
            a = open('c:\ProtTech\data\data.txt', 'r')
            b = a.read()
            a2 = open('c:\ProtTech\data\data.txt', 'rt+')
            s = a2.readlines()[2]
            a2.close()
            if (text + "True,False") in s:
                b = b.replace(text + "True,False", text + "True,True", 1)
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