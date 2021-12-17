import pygame, time
from data.score import *
from pygame.locals import *
from data.questions import *


class Fases6():
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


class FaseSixWorldOne(Fases6):
    def __init__(self, game):
        self.i = 44
        self.layers = [44]
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
        self.q = QuestionsTwo(0)
        self.right_clicking = False
        self.n, self.count = 0, 0
        self.click_event = False
        self.count_click = 0
        self.sheet_event = [False, False, False]
        self.socket_event = {'prcssd1':True, 'prcssd2':True, 'prtc':True, 'prtc2':False, 'hst':True, 'hst2':False,'hst3':False,'lkd1':False, 'angle': 0, 'intel':[44,329], 'angle2': 0, 'amd':[28,97], 'lkd2':False}
        self.slide = {'hst': False, 'hst3': False, 'prtc': False}
        self.cooler = {'clr':True,'lkd':False, 'p1':False, 'p2':False, 'p3':False, 'p4':False, 'psi': [70, 250], 'pin': False, 'pn':False, 's1':[0,0,0,0]}
        self.slot = {'psi2': [126, 104], 'psi1': [23, 104], 'ddr3': True, 'ddr4': True, 'lkd':[False, False], 'slt1':[True,False,False,False], 'slt2':[True,False,False,False], 'slt3':[True,False,False,False], 'slt4':[True,False,False,False], 'angle1': 0, 'angle2':0}
        self.slt = {'slt1':[True,False,False,False], 'slt2':[True,False,False,False], 'slt3':[True,False,False,False], 'slt4':[True,False,False,False]}
        self.finish = False
        self.clock = 0
        self.bios = [False, 0]
        Fases6.__init__(self, game)

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
            self.game.current_menu = self.game.fases_1
            self.run_display = False
            self.gaming_layer = False
            self.game.reset_keys()
            self.state = '1'
            self.layers.clear()
            self.i = 1
            self.layers.append(1)
        if self.game.SPACE_KEY and self.layers[len(self.layers) - 1] != 1000:
            if not self.gamimg_layer and self.layers[len(self.layers) - 1] != 150:
                self.i += 1
                self.layers.append(self.i)
                self.ok = True
                self.clock = 0
            """if self.gamimg_layer:
                if self.layers[len(self.layers) - 1] != 18 and self.layers[len(self.layers) - 1] :
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
                            self.score.count = 0
                            self.score.scr = 0
                    else:
                        self.wrong = True
                        if self.wrong:
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/wrong_answer.mp3'))
                            pygame.mixer.Channel(1).set_volume(0.04)"""
            if not self.gamimg_layer and self.layers[len(self.layers) - 1] == 93:
                self.game.current_menu = self.game.fases_1
                self.run_display = False
                self.gaming_layer = False
                self.game.reset_keys()
                #self.state = '1'
                #self.bx, self.by = self.area['1']['x'], self.area['1']['y']
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
            self.game.draw_text("Nesta fase você verá um pouco sobre a manutenção de um computador", self.font_size, x_text, self.y_text)
            self.game.draw_text("e como deixá-lo mais seguro.", self.font_size, x_text, self.y_text + 20)
        if layer == 2:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Primeiro, você precisa saber os conceitos de manutenção.", self.font_size, x_text, self.y_text)
            self.game.draw_text("Existem dois tipos de manutenção: a preventiva e a corretiva.", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("A manutenção preventiva consiste em um conjunto de procedimentos ", self.font_size, x_text, self.y_text + 40)
            self.game.draw_text("realizados com o objetivo de manter o computador em um bom estado ", self.font_size, x_text, self.y_text + 60)
            self.game.draw_text("de funcionamento.", self.font_size, x_text, self.y_text + 80)
        if layer == 3:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Algumas das práticas mais comuns da manutenção preventiva são a ", self.font_size, 125, 360)
            self.game.draw_text("limpeza interna e externa do computador, organização de fios internos, ", self.font_size, 125, 415)
            self.game.draw_text("ajustes e troca de pasta térmica.", self.font_size, 125, 435)
        if layer == 4:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Quanto ao tempo para se realizar a manutenção, existem recomendações ", self.font_size, x_text, self.y_text)
            self.game.draw_text("diferentes para cada ambiente e usuário, mas a recomendação é que ela ", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("seja frequente. Para fazer uma manutenção geral com um usuário que ", self.font_size, x_text, self.y_text + 40)
            self.game.draw_text("força muito o uso do computador, recomenda-se um intervalo de 6 meses.", self.font_size, x_text, self.y_text + 60)
        if layer == 5:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Já a manutenção corretiva é o tipo de manutenção que precisa ser feita ",self.font_size, x_text, self.y_text)
            self.game.draw_text("para recuperar, trocar ou corrigir alguma peça danificada da máquina, ", self.font_size,x_text, self.y_text + 20)
            self.game.draw_text("podendo também ser necessário restaurar os softwares instalados no ", self.font_size,x_text, self.y_text + 40)
            self.game.draw_text("computador.", self.font_size,x_text, self.y_text + 60)
        if layer == 6:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Quanto mais eficiente for a manutenção preventiva, menor ", self.font_size,251, self.y_text)
            self.game.draw_text("será o risco de fazer a manutenção corretiva, o que é mais ", self.font_size,251, self.y_text + 20)
            self.game.draw_text("econômico e menos complicado, uma vez que o custo de  ", self.font_size,251, self.y_text + 40)
            self.game.draw_text("reparos e reposições é maior do que o custo por limpeza", self.font_size,251, self.y_text + 60)
            self.game.draw_text("e prevenção.", self.font_size,251, self.y_text + 80)
        if layer == 7:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora que você sabe a diferença entre manutenção corretiva e ", 20, x_text, self.y_text)
            self.game.draw_text("preventiva, é preciso saber quais são as ferramentas utilizadas ", 20, x_text,self.y_text + 20)
            self.game.draw_text("durante o processo de manutenção.", 20, x_text, self.y_text + 40)
        if layer == 8:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("As ferramentas são: chaves para parafusar e desparafusar, podendo ser tanto ", 20, x_text, self.y_text)
            self.game.draw_text("chave Philips quanto de fenda, dependendo do parafuso presente no  ", 20, x_text,self.y_text + 20)
            self.game.draw_text("computador; panos de microfibra e panos umedecidos; pincel antiestático; ", 20, x_text, self.y_text + 40)
            self.game.draw_text("ferro de solda; álcool isopropílico; multímetro; pasta térmica; parafusos", 20, x_text, self.y_text + 60)
            self.game.draw_text("extras.", 20, x_text, self.y_text + 80)
        if layer == 9:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Agora você verá como fazer uma das etapas da manutenção  ", 20, 250, self.y_text)
            self.game.draw_text("preventiva: a limpeza dos periféricos e da parte externa do ", 20, 250,self.y_text + 20)
            self.game.draw_text("gabinete. É importante ter certeza de que todos os ", 20, 250,self.y_text + 40)
            self.game.draw_text("componentes estão desconectados do computador e da tomada.", 20, 250,self.y_text + 60)
        if layer == 10:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Primeiro, o mouse.", 19, x_text, self.y_text)
            self.game.draw_text("Deve-se desconectá-lo do gabinete.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Para limpá-lo, deve-se utilizar um pano umedecido em sua carcaça e ", 19, x_text, self.y_text + 40)
            self.game.draw_text("um pano com um pouco de emulsificante (detergente) e água para o cabo.", 19, x_text, self.y_text + 60)
        if layer == 11:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Pode-se utilizar também algo com ponta macia como uma haste com ponta ", 19,x_text, self.y_text)
            self.game.draw_text("de algodão para limpar os vãos dos botões.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Depois do mouse, é a vez do teclado.", 19, x_text,self.y_text + 40)
        if layer == 12:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Com ele já desconectado, deve-se virá-lo de cabeça para ", 21, 239,self.y_text)
            self.game.draw_text("baixo e chacoalhá-lo (se houver muita sujeira, pode-se ", 21, 239,self.y_text + 20)
            self.game.draw_text("também dar algumas batidas).", 21, 239, self.y_text + 40)
        if layer == 13:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois, deve-se pegar um pano seco e passar pelo teclado de ", 21, x_text, self.y_text)
            self.game.draw_text("maneira suave por todas as", 21, x_text, self.y_text + 20)
            self.game.draw_text("Para limpar o cabo, pode-se fazer o mesmo que o do mouse.", 21, x_text, self.y_text + 40)
        if layer == 14:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Quanto à limpeza de cada tecla, entre elas pode ser passado uma ", 21, x_text, self.y_text)
            self.game.draw_text("haste com ponta de algodão com um pouco de álcool isopropílico ", 21, x_text, self.y_text + 20)
            self.game.draw_text("em suas pontas, o que facilita a limpeza.", 21, x_text, self.y_text + 40)
        if layer == 15:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Ao acabar com o teclado, chega a parte do monitor. Para ", self.font_size, 249, self.y_text)
            self.game.draw_text("limpá-lo não é recomendado nenhum tipo de líquido, a ", self.font_size, 249, self.y_text + 20)
            self.game.draw_text("menos que um específico para a limpeza de telas. Então ", self.font_size, 249, self.y_text + 40)
            self.game.draw_text("deve-se passar um pano seco suavemente na tela.", self.font_size, 249, self.y_text + 60)
        if layer == 16:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A carcaça pode ser limpa com um pano umedecido e o cabo, do mesmo ", 20, x_text, self.y_text)
            self.game.draw_text("jeito que o do mouse.", 20, x_text, self.y_text + 20)
            self.game.draw_text("Por fim, há a parte externa do gabinete. Para limpá-la pode-se utilizar um ", 20, x_text, self.y_text + 40)
            self.game.draw_text("pano seco e umedecido, além do pincel antiestático nas entradas do gabinete. ", 20, x_text, self.y_text + 60)
            self.game.draw_text("É melhor utilizar o pano seco na parte do espelho atrás do gabinete.", 20, x_text, self.y_text + 80)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 20, x_text, self.y_text + 100)
        if layer == 17:
            #FAZER JOGO
            pass
        if layer == 18:
            self.draw_very_good()
        if layer == 19:
             #FAZER JOGO
            pass
        if layer == 20:
            self.draw_very_good()
        if layer == 21:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois de ter limpado a parte externa do computador, agora é preciso ", 21, x_text,self.y_text)
            self.game.draw_text("limpar a parte interna.", 21, x_text,self.y_text + 20)
        if layer == 22:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para fazer isso, primeiro é preciso abrir o gabinete. Alguns gabinetes ", 21, x_text,self.y_text)
            self.game.draw_text("possuem uma fechadura por travas e outros por parafuso. Nos gabinetes ", 21, x_text,self.y_text + 20)
            self.game.draw_text("fechados com parafuso é preciso tirar os parafusos, pelo menos os da", 21, x_text,self.y_text + 40)
            self.game.draw_text("parte que dê acesso aos fans e à placa-mãe de", 21, x_text,self.y_text + 60)
            self.game.draw_text("maneira mais fácil.", 21, x_text,self.y_text + 80)
        if layer == 23:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para que não haja problema, é recomendado colocar o gabinete com o ", 21, x_text,self.y_text)
            self.game.draw_text("lado de maior área em contato com a superfície de apoio (deixá-lo deitado).", 21, x_text,self.y_text + 20)
            self.game.draw_text("Existem ordens diferentes de limpeza, então vamos escolher uma, mas ", 21, x_text,self.y_text + 40)
            self.game.draw_text("não a tome como a única.", 21, x_text,self.y_text + 60)
        if layer == 24:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Com o gabinete aberto, se o gabinete possuir muito tempo sem ", 19, 247,self.y_text)
            self.game.draw_text("limpeza, é bom utilizar um soprador com velocidade baixa para ", 19, 247,self.y_text + 20)
            self.game.draw_text("tirar o excesso da poeira.", 19, 247,self.y_text + 40)
        if layer == 25:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Algumas pessoas recomendam utilizar um secador de cabelo, mas ele  ", 21, x_text,self.y_text)
            self.game.draw_text("pode trazer muito perigo, pois, caso esteja no modo quente, pode ", 21, x_text,self.y_text + 20)
            self.game.draw_text("danificar os componentes internos, derretendo-os.", 21, x_text,self.y_text + 40)
            self.game.draw_text("Então, se for utilizar o secador, ele deve ser colocado no modo ", 21, x_text,self.y_text + 60)
            self.game.draw_text("frio ou outra opção que não seja a quente.", 21, x_text,self.y_text + 80)
        if layer == 26:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Caso não haja muita sujeira, um pincel antiestático serve. Esse tipo ", 21, x_text,self.y_text )
            self.game.draw_text("de pincel é necessário porque, caso seja feito de outros materiais, ", 21, x_text,self.y_text + 20)
            self.game.draw_text("pode gerar eletricidade estática com o atrito de sua ponta com os ", 21, x_text,self.y_text + 40)
            self.game.draw_text("componentes, podendo causar um curto circuito com algum componente", 21, x_text,self.y_text + 60)
            self.game.draw_text("da placa-mãe, por exemplo.", 21, x_text,self.y_text + 80)
        if layer == 27:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Para uma melhor limpeza, retire o dispositivo de armazenamento, ", 20, 247,self.y_text)
            self.game.draw_text("placa de vídeo e as RAMs de dentro do gabinete com um pouco de ", 20, 247,self.y_text + 20)
            self.game.draw_text("álcool isopropílico. Deve-se ter cuidado para não arranhar os “dentes” dos  ", 20, 140,self.y_text + 50)
            self.game.draw_text("pentes de RAM e da placa de vídeo.", 20, 140,self.y_text + 70)
        if layer == 28:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para limpar o cooler da CPU, ele pode ser retirado e limpado separadamente, ou ", 19, x_text, self.y_text)
            self.game.draw_text("ainda internamente (mais uma vez, dependendo da quantidade de sujeira).", 19, x_text, self.y_text + 20)
            self.game.draw_text("Para limpá-lo, pode ser utilizado um pincel e um pano de microfibra para retirar ", 19, x_text, self.y_text + 40)
            self.game.draw_text("a poeira das pás. Será mais fácil se elas estiverem travadas, ou com os dedos da ", 19, x_text, self.y_text + 60)
            self.game.draw_text("mão, ou com algum suporte.", 19, x_text, self.y_text + 80)
        if layer == 29:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois, deve-se retirar os fans do gabinete, se possível, e fazer a ", 19, x_text, self.y_text)
            self.game.draw_text("mesma limpeza do cooler. Para uma limpeza mais simples, pode ser ", 19, x_text, self.y_text + 20)
            self.game.draw_text("utilizado apenas o pincel e um pano de microfibra.", 19, x_text, self.y_text + 40)
            self.game.draw_text("A mesma forma se aplica aos fans da placa de vídeo, mas sem retirá-los dela.", 19, x_text, self.y_text + 60)
            self.game.draw_text("", 19, x_text, self.y_text + 80)
        if layer == 30:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A fonte também precisa ser limpa, pelo menos superficialmente. É mais ", 19, x_text, self.y_text)
            self.game.draw_text("complicado limpá-la internamente, então, desde que o local onde ela ", 19, x_text, self.y_text + 20)
            self.game.draw_text("esteja fique limpo, não será preciso abri-la. O processo de limpeza é ", 19, x_text, self.y_text + 40)
            self.game.draw_text("o mesmo: pincel antiestático e pano de microfibra.", 19, x_text, self.y_text + 60)
            self.game.draw_text("Durante todo o processo é preciso ter cuidado para não danificar as entradas dos ", 19, x_text, self.y_text + 80)
            self.game.draw_text("hardwares. É mais simples utilizar um soprador para tirar a maior parte da sujeira.", 19, x_text, self.y_text + 100)
        if layer == 31:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ao término da limpeza, os hardwares desconectados devem voltar para", 19, x_text, self.y_text)
            self.game.draw_text("onde estavam, do jeito que estavam e o gabinete deve ser fechado e ", 19, x_text, self.y_text + 20)
            self.game.draw_text("seus parafusos devem ser repostos.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Assim, está terminada a limpeza do computador. Ela é extremamente ", 19, x_text, self.y_text + 60)
            self.game.draw_text("necessária, pois nenhum local é livre de poeira por muito tempo e", 19, x_text, self.y_text + 80)
            self.game.draw_text("essa, por ser muito pequena, acaba entrando ou grudando no computador.", 19, x_text, self.y_text + 100)
        if layer == 32:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Mas a manutenção preventiva não se trata apenas de limpeza. Ela ", 19, x_text, self.y_text)
            self.game.draw_text("se trata também de segurança.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 19, x_text, self.y_text + 40)
        if layer == 33:
            #fazer jogo
            #fazer jogo#fazer jogo#fazer jogo#fazer jogo#fazer jogo
            #fazer jogo#fazer jogo
            #fazer jogo#fazer jogo#fazer jogo#fazer jogo
            pass
        if layer == 34:
            self.draw_very_good()
        if layer == 35:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Vamos dar continuidade à manutenção preventiva. Como dito ", 19, x_text,self.y_text)
            self.game.draw_text("anteriormente, ela não se trata somente de limpeza, mas também ", 19, x_text,self.y_text + 20)
            self.game.draw_text("de reposição e segurança. Uma das reposições feitas em uma manutenção", 19, x_text,self.y_text + 40)
            self.game.draw_text("preventiva é a da pasta térmica. Mas você deve estar se perguntando: ", 19, x_text,self.y_text + 60)
            self.game.draw_text("o que é pasta térmica? Ela é um componente muito importante para o ", 19, x_text,self.y_text + 80)
            self.game.draw_text("computador, pois ajuda a manter a temperatura da CPU baixa (da GPU também).", 19, x_text,self.y_text + 100)
        if layer == 36:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Ela possui uma textura pastosa e pode ser encontrada na cor branca ", 19, 250,self.y_text)
            self.game.draw_text("e prateada. A sua aplicação é diretamente na parte de cima do ", 19, 250,self.y_text + 20)
            self.game.draw_text("processador.", 19, 250,self.y_text + 40)
        if layer == 37:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ela é aplicada uma vez e o cooler é colocado por cima, com a parte de ", 19, x_text,self.y_text)
            self.game.draw_text("cobre fazendo contato com a pasta, pressionando-a. Com a pasta térmica, ", 19, x_text,self.y_text + 20)
            self.game.draw_text("a condução do calor produzido pelo processador é mais rapidamente levado ", 19, x_text,self.y_text + 40)
            self.game.draw_text("para o cooler, que transfere o calor para fora do gabinete.", 19, x_text,self.y_text + 60)
        if layer == 38:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Essa transferência de calor pode ser tanto alta quanto baixa. Vai depender ", 19, x_text,self.y_text)
            self.game.draw_text("do valor da condutividade térmica de cada pasta, ou seja, do material que a ", 19, x_text,self.y_text + 20)
            self.game.draw_text("pasta é feita.", 19, x_text,self.y_text + 40)
        if layer == 39:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("As unidades de condutividade térmica mais utilizadas no mercado ", 19, 255,self.y_text)
            self.game.draw_text("são W/mK (Watt por metro Kelvin), W/m²K (Watt por metro quadrado ", 19, 255,self.y_text + 20)
            self.game.draw_text("Kelvin) e W/m²/ºC (Watt por metro quadrado por grau Celsius). ", 19, 255,self.y_text + 40)
            self.game.draw_text("Existem pastas térmicas com valores de condutividade térmica", 19, 255,self.y_text + 60)
            self.game.draw_text("baixos, como 1,46 W/mK, até pastas com valores muito altos, ", 19, 255,self.y_text + 80)
            self.game.draw_text("como 73 W/mk.", 19, 255,self.y_text + 100)
        if layer == 40:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Quanto maior a condutividade térmica, maior é o preço da pasta térmica e ", 19, x_text,self.y_text)
            self.game.draw_text("menor é a sua quantidade. Por exemplo, a pasta de condutividade térmica ", 19, x_text,self.y_text + 20)
            self.game.draw_text("de 1,46 W/mK pode ser comprada com um tubo com 38 gramas de pasta. ", 19, x_text,self.y_text + 40)
            self.game.draw_text("Já na de 73 W/mk, o tubo vem com 1 (um) grama apenas.", 19, x_text,self.y_text + 60)
        if layer == 41:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora é que entraremos na manutenção propriamente dita: essa pasta ", 19, x_text,self.y_text)
            self.game.draw_text("perde a capacidade de transferência ao longo do tempo, independente ", 19, x_text,self.y_text + 20)
            self.game.draw_text("da condutividade, e por isso ela deve ser trocada em determinados ", 19, x_text,self.y_text + 40)
            self.game.draw_text("intervalos de tempo.", 19, x_text,self.y_text + 60)
        if layer == 42:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Além disso, é importante saber que todos os processadores geram calor. ", 19, x_text,self.y_text)
            self.game.draw_text("Isso ocorre por causa da energia consumida para realizar os cálculos", 19, x_text,self.y_text + 20)
            self.game.draw_text("computacionais. Como o rendimento de nenhuma máquina é perfeito, boa ", 19, x_text,self.y_text + 40)
            self.game.draw_text("parte da energia é dissipada na forma de calor e concentrada na CPU. ", 19, x_text,self.y_text + 60)
            self.game.draw_text("E quanto maior for o requerimento de potência computacional, maior", 19, x_text,self.y_text + 80)
            self.game.draw_text("será a produção de calor. Daí entra o papel da pasta térmica.", 19, x_text,self.y_text + 100)
        if layer == 43:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Boas pastas térmicas não precisam de tanta preocupação quanto a sua ", 19, x_text,self.y_text)
            self.game.draw_text("troca, sendo necessária uma troca a cada 2 anos ou mais. Já as pastas ", 19, x_text,self.y_text + 20)
            self.game.draw_text("térmicas mais modestas, essas precisam de um intervalo de tempo menor ", 19, x_text,self.y_text + 40)
            self.game.draw_text("para serem trocadas, de 1 ano a 6 meses.", 19, x_text,self.y_text + 60)
            self.game.draw_text("Mas você pode estar pensando: é possível utilizar o computador sem", 19, x_text,self.y_text + 80)
            self.game.draw_text("pasta térmica?", 19, x_text,self.y_text + 100)
        if layer == 44:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A resposta é sim, mas não por muito tempo. Os processadores possuem ", 19, x_text, self.y_text)
            self.game.draw_text("mecanismos que fazem diminuir o seu clock ao serem submetidos a grandes ", 19, x_text, self.y_text + 20)
            self.game.draw_text("temperaturas, havendo também uma temperatura máxima que, caso chegue, o ", 19, x_text,self.y_text + 40)
            self.game.draw_text("computador desliga.", 19, x_text,self.y_text + 60)
        if layer == 45:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Sem a pasta térmica, um processador pode facilmente chegar ", 19, 255, self.y_text)
            self.game.draw_text("aos 100 ºC, dependendo da aplicação, e desligar.", 19, 255, self.y_text + 20)
            self.game.draw_text("Esse desligamento pode causar danos sérios não apenas na CPU, ", 19, 255, self.y_text + 40)
            self.game.draw_text("mas também em todos os outros componentes, como arquivos ou ", 19, 255, self.y_text + 60)
            self.game.draw_text("um disco de armazenamento inteiro corrompido.", 19, 255, self.y_text + 80)
        if layer == 46:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Você vai ver agora como colocar e trocar uma pasta térmica no computador.", 19, x_text, self.y_text)
            self.game.draw_text("O processo de colocação e de troca de pasta térmica é semelhante.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Na primeira vez, com o computador desconectado da tomada e o processador ", 19, x_text, self.y_text + 40)
            self.game.draw_text("já encaixado em seu socket, deve-se ter em mãos a pasta (em tubo ou em um pote).", 19, x_text, self.y_text + 60)
        if layer == 47:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Caso a pasta venha em um tubo, o processo de aplicação é mais simples: ", 19, x_text, self.y_text)
            self.game.draw_text("basta colocar uma única e pequena gota no centro do processador.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Depois disso, essa gota pode ser espalhada por toda a superfície do ", 19, x_text, self.y_text + 40)
            self.game.draw_text("processador, delicadamente, utilizando uma haste de algodão, ou ", 19, x_text, self.y_text + 60)
            self.game.draw_text("deixá-la do jeito que está para a próxima etapa.", 19, x_text, self.y_text + 80)
        if layer == 48:
            #PAREI AQUI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            pass
        if layer == 49:
            self.draw_very_good()
        if layer == 50:
            #FAZER JOGO
            pass
        if layer == 51:
            self.draw_very_good()
        if layer == 52:
            #FAZER JOGO
            pass
        if layer == 53:
            self.draw_very_good()
        if layer == 54:
            #FAZER JOGO
            pass
        if layer == 55:
            self.draw_very_good()
        if layer == 56:
            #FAZER JOGO
            pass
        if layer == 57:
            self.draw_very_good()
        if layer == 58:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora vamos falar sobre o gabinete.", 19, x_text, self.y_text)
            self.game.draw_text("O gabinete é a “carcaça” do computador, onde são colocados os componentes ", 19, x_text,self.y_text + 20)
            self.game.draw_text("internos (não periféricos). Muitas vezes alguns leigos chamam o gabinete de ", 19, x_text,self.y_text + 40)
            self.game.draw_text("CPU, mas já vimos que CPU é Unidade Central de Processamento, o processador.", 19, x_text,self.y_text + 60)
        if layer == 59:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O gabinete possui uma divisão de lados. O lado da frente geralmente possui ", 19, x_text, self.y_text)
            self.game.draw_text("conectores de áudio e USB, além do botão de ligar/desligar. Já o lado de trás ", 19, x_text,self.y_text + 20)
            self.game.draw_text("possui o “espelho” onde estão os conectores de força, rede e de periféricos, ", 19, x_text,self.y_text + 40)
            self.game.draw_text("além de espaços para conexão de novos espelhos de hardwares ligados à conexão", 19, x_text,self.y_text + 60)
            self.game.draw_text("PCI-Express, por exemplo.", 19, x_text,self.y_text + 80)
        if layer == 60:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A construção mais comum para os gabinetes é de aço eletro galvanizado, ", 19, x_text, self.y_text)
            self.game.draw_text("alumínio e plástico.", 19, x_text,self.y_text + 20)
            self.game.draw_text("A placa-mãe é instalada na lateral do gabinete por meio de parafusos. A ", 19, x_text,self.y_text + 40)
            self.game.draw_text("fonte é instalada na parte de trás do gabinete, geralmente na parte de cima.", 19, x_text,self.y_text + 60)
        if layer == 61:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os fans são fixados na parte traseira do gabinete a fim de ", 19, x_text, self.y_text)
            self.game.draw_text("facilitar a dissipação de calor por convecção e os dispositivos ", 19, x_text, self.y_text + 20)
            self.game.draw_text("de armazenamento (HDs e SSDs) são alocados em um compartimento ", 19, x_text, self.y_text + 40)
            self.game.draw_text("inferior ou na frente do gabinete chamado. Esses compartimentos ", 19, x_text, self.y_text + 60)
            self.game.draw_text("são chamados de baias.", 19, x_text, self.y_text + 80)
            self.game.draw_text("Vamos ver como instalar a placa-mãe no gabinete.", 19, x_text, self.y_text + 100)
        if layer == 62:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Primeiro, selecione o espelho da placa-mãe e coloque-o na parte traseira do ", 19, x_text, self.y_text)
            self.game.draw_text("gabinete. Geralmente o espelho deve ficar com o sentido dos conectores de ", 19, x_text, self.y_text + 20)
            self.game.draw_text("áudio próximos à fonte, ou no sentido próximo a parte de baixo do gabinete.", 19, x_text, self.y_text + 40)
        if layer == 63:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para colocar o espelho, com o espelho em mãos na parte de dentro ", 19, x_text, self.y_text)
            self.game.draw_text("do gabinete, empurre o espelho no local adequado para o sentido de ", 19, x_text, self.y_text + 20)
            self.game.draw_text("fora do gabinete.", 19, x_text, self.y_text + 40)
        if layer == 64:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois, você deve se atentar aos parafusos para serem colocados entre a ", 19, x_text, self.y_text)
            self.game.draw_text("placa-mãe e o gabinete, chamados de stand-offs. Eles são necessários, ", 19, x_text, self.y_text + 20)
            self.game.draw_text("pois o contato direto da parte metálica do gabinete com a placa-mãe ", 19, x_text, self.y_text + 40)
            self.game.draw_text("pode gerar problemas de curto circuito.", 19, x_text, self.y_text + 60)
        if layer == 65:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para saber onde colocar os stand-offs, veja no manual da placa-mãe e ", 19, x_text, self.y_text)
            self.game.draw_text("do gabinete.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Geralmente, para as placas-mãe no padrão de fonte ATX e micro-ATX, os ", 19, x_text, self.y_text + 40)
            self.game.draw_text("locais dos stand-offs são representados por letras (como AM).", 19, x_text, self.y_text + 60)
            self.game.draw_text("Depois de encontrar os locais adequados para os stand-offs, coloque-", 19, x_text, self.y_text + 80)
            self.game.draw_text("-os com uma chave de fenda.", 19, x_text, self.y_text + 100)
        if layer == 66:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Agora, com a placa-mãe em mãos, coloque-a dentro do gabinete. Use  ", 19,250, self.y_text)
            self.game.draw_text("os conectores de áudio como referenciais para o encaixe com o ", 19,250, self.y_text + 20)
            self.game.draw_text("espelho da placa-mãe e encaixe a placa-mãe no espelho.", 19,250, self.y_text + 40)
            self.game.draw_text("Com a placa-mãe encaixada no espelho, parafuse a placa-mãe no ", 19,250, self.y_text + 60)
            self.game.draw_text("gabinete com os parafusos que vieram com ela.", 19,250, self.y_text + 80)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 19,250, self.y_text + 100)
        if layer == 67:
            #FAZER JOGO
            pass
        if layer == 68:
            self.draw_very_good()
        if layer == 69:
            #FAZER JOGO
            pass
        if layer == 70:
            self.draw_very_good()
        if layer == 71:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Vamos ver agora outra parte importante, os cabos do gabinete.", 19, x_text, self.y_text)
            self.game.draw_text("Esses cabos já vem no gabinete servem para ligar o botão liga/", 19, x_text, self.y_text + 20)
            self.game.draw_text("desliga, os conectores de som, usb e os leds do gabinete na placa-mãe.", 19, x_text,self.y_text + 40)
            self.game.draw_text("Os cabos mais comuns nos computadores mais recentes são: cabo USB 3.0 ", 19, x_text,self.y_text + 60)
            self.game.draw_text("(alguns possuem tanto o 3.0 quanto o 2.0), cabo HD data/audio, cabo power ", 19, x_text,self.y_text + 80)
            self.game.draw_text("sw, cabo led sw, cabo reset sw e HD led.", 19, x_text,self.y_text + 100)
        if layer == 72:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O cabo USB 3.0, como o próprio nome já diz, serve para habilitar as ", 19, 255, self.y_text)
            self.game.draw_text("portas USB do gabinete. Ele possui 19 entradas (20 entradas -1 no ", 19, 255, self.y_text + 20)
            self.game.draw_text("final). Para encontrá-lo na placa-mãe, leia o manual ou, se houver, procure ", 19, 150,self.y_text + 40)
            self.game.draw_text("pelo conector de nome USB3 na placa-mãe. Basta colocar no sentido em que o  ", 19, 150,self.y_text + 60)
            self.game.draw_text("pino faltante se encontre com o espaço em todo o conector e empurrar o", 19, 150,self.y_text + 80)
            self.game.draw_text("cabo no sentido da parte de trás da placa.", 19, 150,self.y_text + 100)
        if layer == 73:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O conector de áudio, como o próprio nome já diz, serve para habilitar as portas de ", 19, x_text, self.y_text)
            self.game.draw_text("áudio do gabinete. Ele possui 9 entradas (10 entradas -1 próxima ao final). Para ", 19, x_text, self.y_text + 20)
            self.game.draw_text("encontrá-lo na placa-mãe, leia o manual ou, se houver, procure pelo conector de ", 19, x_text, self.y_text + 40)
            self.game.draw_text("nome AAFP ou HD data/audio na placa-mãe. O método de encaixe é o mesmo do USB 3.0.", 19, x_text, self.y_text + 60)
        if layer == 74:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O conector power sw serve para habilitar o botão de ligar e desligar do gabinete. ", 19, x_text, self.y_text)
            self.game.draw_text("Ele faz parte da conexão da placa-mãe chamada painel. Para nos guiarmos durante ", 19, x_text, self.y_text + 20)
            self.game.draw_text("a instalação desse conector e dos outros (que também fazem parte do painel), ", 19, x_text, self.y_text + 40)
            self.game.draw_text("vamos dividir apenas nas partes importantes dele que, nessa placa-mãe escolhida,", 19, x_text, self.y_text + 60)
            self.game.draw_text("são os últimos 5 pares de pinos com a sequência de 4 pares de pinos mais  ", 19, x_text, self.y_text + 80)
            self.game.draw_text("ao extremo, seguidos de 1 pino.", 19, x_text, self.y_text + 100)
        if layer == 75:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Depois de encontrar o painel, os pinos onde se deve conectar o ", 19, 250, self.y_text)
            self.game.draw_text("cabo power sw devem ser vistos no manual da placa-mãe ou, se ", 19, 250, self.y_text + 20)
            self.game.draw_text("houver, procure na legenda do painel o nome “pwr_sw”. Na legenda ", 19, 250, self.y_text + 40)
            self.game.draw_text("e no manual haverá também o sentido de negativo e positivo do ", 19, 250, self.y_text + 60)
            self.game.draw_text("cabo para ser conectado.", 19, 250, self.y_text + 80)
        if layer == 76:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois de encontrar o par de encaixe e o sentido dos pólos para ", 19, x_text, self.y_text)
            self.game.draw_text("serem conectados, coloque o cabo no mesmo método dos outros colocados.", 19, x_text, self.y_text + 20)
        if layer == 77:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O conector reset sw serve para habilitar a algumas funções distintas do ", 19, x_text, self.y_text)
            self.game.draw_text("gabinete, como desligamento forçado, controle de velocidade dos fans e ", 19, x_text, self.y_text + 20)
            self.game.draw_text("cor dos leds, caso haja no gabinete. Para conectá-lo, mais uma vez, leia", 19, x_text, self.y_text + 40)
            self.game.draw_text("o manual para encontrar o local correto, ou, se for uma conexão padrão, ", 19, x_text, self.y_text + 60)
            self.game.draw_text("coloque-o abaixo e em paralelo ao conector power sw, mas no mesmo sentido ", 19, x_text, self.y_text + 80)
            self.game.draw_text("dos pólos.", 19, x_text, self.y_text + 100)
        if layer == 78:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Os conectores power led servem para identificar a intensidade  ", 19, 255, self.y_text)
            self.game.draw_text("máxima e mínima dos leds no gabinete. Para conectá-los, mais uma ", 19, 255, self.y_text + 20)
            self.game.draw_text("vez, leia no manual da placa-mãe, mas o caso padrão é ao lado do", 19, 255, self.y_text + 40)
            self.game.draw_text("conector power sw, próximo ao fim da linha de cima dos pares de ", 19, 255, self.y_text + 60)
            self.game.draw_text("pinos, no mesmo sentido dos pólos do power sw, com o cabo  ", 19, 255, self.y_text + 80)
            self.game.draw_text("power led + no pólo positivo e o power led - no polo negativo.", 19, 255, self.y_text + 100)
        if layer == 79:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O último cabo a ser conectado é o HD LED. Ele serve para identificar se o disco  ", 19, x_text, self.y_text)
            self.game.draw_text("rígido está instalado corretamente. Para conectá-lo, pela última vez, veja no  ", 19, x_text, self.y_text + 20)
            self.game.draw_text("manual da placa-mãe, mas no caso convencional, ele deve ser colocado abaixo dos ", 19, x_text, self.y_text + 40)
            self.game.draw_text("conectores power leds, no mesmo sentido dos pólos do power sw.", 19, x_text, self.y_text + 60)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 19, x_text, self.y_text + 80)
        if layer == 80:
            #FAZER JOGO
            pass
        if layer == 81:
            self.draw_very_good()
        if layer == 82:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora você vai ver como instalar a fonte no gabinete. ", 19, x_text, self.y_text)
            self.game.draw_text("Pegue a fonte, coloque o cooler no sentido para baixo do gabinete se ela for ", 19, x_text, self.y_text + 20)
            self.game.draw_text("colocada na parte de baixo dele.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Pegue os parafusos e coloque-os, pelo lado de fora do gabinete, na fonte.", 19, x_text, self.y_text + 60)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 19, x_text, self.y_text + 80)
        if layer == 83:
            #FAZER JOGO
            pass
        if layer == 84:
            self.draw_very_good()
        if layer == 85:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora você vai ver como instalar o HD/SSD SATA no gabinete.", 19, x_text, self.y_text)
            self.game.draw_text("Procure o compartimento do gabinete onde estão as baias e, caso ", 19, x_text, self.y_text + 20)
            self.game.draw_text("sejam removíveis, remova-as e encaixe o HD no sentido correto. Depois", 19, x_text, self.y_text + 40)
            self.game.draw_text("parafuse o HD nas baias pelos lados.", 19, x_text, self.y_text + 60)
        if layer == 86:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Caso as baias não sejam facilmente removíveis, apenas encaixe o HD e ", 19, x_text, self.y_text)
            self.game.draw_text("parafuse as laterais dele nas baias.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Por último, quando tudo estiver instalado, feche o compartimento do ", 19, x_text, self.y_text + 40)
            self.game.draw_text("gabinete (em alguns casos, ele é fechado por pressão, em outros, ", 19, x_text, self.y_text + 60)
            self.game.draw_text("como uma porta) e ligue o PC para testar.", 19, x_text, self.y_text + 80)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 19, x_text, self.y_text + 100)
        if layer == 87:
            #FAZER QUESTÃO  
            pass
        if layer == 88:
            self.draw_very_good()
        if layer == 89:
            #FAZER QUESTÃO  
            pass
        if layer == 90:
            self.draw_very_good()
        if layer == 91:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ufa! Você terminou a fase 5. Agora, depois de aprender um pouco ", 19, x_text, self.y_text)
            self.game.draw_text("sobre o funcionamento das partes de um computador, está na hora ", 19, x_text, self.y_text + 20)
            self.game.draw_text("de aprender sobre a manutenção e segurança dessas partes.", 19, x_text, self.y_text + 40)
        if layer == 92:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s5/end.png'), (0, 0))
            text = 'FasesWone='
            a = open('c:\ProtTech\data\data.txt', 'r')
            b = a.read()
            a2 = open('c:\ProtTech\data\data.txt', 'rt+')
            s = a2.readlines()[2]
            a2.close()
            if (text + "True,True,True,True,True,False") in s:
                b = b.replace(text + "True,True,True,True,True,False", text + "True,True,True,True,True,True", 1)
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
            