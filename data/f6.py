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
        self.game.display.blit(pygame.image.load('data/img/Barra-Di??logo.png'), (0, 0))

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
            if not self.gamimg_layer and self.layers[len(self.layers) - 1] == 90:
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
            self.game.draw_text("Nesta fase voc?? ver?? um pouco sobre a manuten????o de um computador", self.font_size, x_text, self.y_text)
            self.game.draw_text("e como deix??-lo mais seguro.", self.font_size, x_text, self.y_text + 20)
        if layer == 2:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Primeiro, voc?? precisa saber os conceitos de manuten????o.", self.font_size, x_text, self.y_text)
            self.game.draw_text("Existem dois tipos de manuten????o: a preventiva e a corretiva.", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("A manuten????o preventiva consiste em um conjunto de procedimentos ", self.font_size, x_text, self.y_text + 40)
            self.game.draw_text("realizados com o objetivo de manter o computador em um bom estado ", self.font_size, x_text, self.y_text + 60)
            self.game.draw_text("de funcionamento.", self.font_size, x_text, self.y_text + 80)
        if layer == 3:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Algumas das pr??ticas mais comuns da manuten????o preventiva s??o a ", self.font_size, 125, 360)
            self.game.draw_text("limpeza interna e externa do computador, organiza????o de fios internos, ", self.font_size, 125, 415)
            self.game.draw_text("ajustes e troca de pasta t??rmica.", self.font_size, 125, 435)
        if layer == 4:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Quanto ao tempo para se realizar a manuten????o, existem recomenda????es ", self.font_size, x_text, self.y_text)
            self.game.draw_text("diferentes para cada ambiente e usu??rio, mas a recomenda????o ?? que ela ", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("seja frequente. Para fazer uma manuten????o geral com um usu??rio que ", self.font_size, x_text, self.y_text + 40)
            self.game.draw_text("for??a muito o uso do computador, recomenda-se um intervalo de 6 meses.", self.font_size, x_text, self.y_text + 60)
        if layer == 5:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("J?? a manuten????o corretiva ?? o tipo de manuten????o que precisa ser feita ",self.font_size, x_text, self.y_text)
            self.game.draw_text("para recuperar, trocar ou corrigir alguma pe??a danificada da m??quina, ", self.font_size,x_text, self.y_text + 20)
            self.game.draw_text("podendo tamb??m ser necess??rio restaurar os softwares instalados no ", self.font_size,x_text, self.y_text + 40)
            self.game.draw_text("computador.", self.font_size,x_text, self.y_text + 60)
        if layer == 6:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Quanto mais eficiente for a manuten????o preventiva, menor ", self.font_size,251, self.y_text)
            self.game.draw_text("ser?? o risco de fazer a manuten????o corretiva, o que ?? mais ", self.font_size,251, self.y_text + 20)
            self.game.draw_text("econ??mico e menos complicado, uma vez que o custo de  ", self.font_size,251, self.y_text + 40)
            self.game.draw_text("reparos e reposi????es ?? maior do que o custo por limpeza", self.font_size,251, self.y_text + 60)
            self.game.draw_text("e preven????o.", self.font_size,251, self.y_text + 80)
        if layer == 7:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora que voc?? sabe a diferen??a entre manuten????o corretiva e ", 20, x_text, self.y_text)
            self.game.draw_text("preventiva, ?? preciso saber quais s??o as ferramentas utilizadas ", 20, x_text,self.y_text + 20)
            self.game.draw_text("durante o processo de manuten????o.", 20, x_text, self.y_text + 40)
        if layer == 8:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("As ferramentas s??o: chaves para parafusar e desparafusar, podendo ser tanto ", 20, x_text, self.y_text)
            self.game.draw_text("chave Philips quanto de fenda, dependendo do parafuso presente no  ", 20, x_text,self.y_text + 20)
            self.game.draw_text("computador; panos de microfibra e panos umedecidos; pincel antiest??tico; ", 20, x_text, self.y_text + 40)
            self.game.draw_text("ferro de solda; ??lcool isoprop??lico; mult??metro; pasta t??rmica; parafusos", 20, x_text, self.y_text + 60)
            self.game.draw_text("extras.", 20, x_text, self.y_text + 80)
        if layer == 9:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Agora voc?? ver?? como fazer uma das etapas da manuten????o  ", 20, 250, self.y_text)
            self.game.draw_text("preventiva: a limpeza dos perif??ricos e da parte externa do ", 20, 250,self.y_text + 20)
            self.game.draw_text("gabinete. ?? importante ter certeza de que todos os ", 20, 250,self.y_text + 40)
            self.game.draw_text("componentes est??o desconectados do computador e da tomada.", 20, 250,self.y_text + 60)
        if layer == 10:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Primeiro, o mouse.", 19, x_text, self.y_text)
            self.game.draw_text("Deve-se desconect??-lo do gabinete.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Para limp??-lo, deve-se utilizar um pano umedecido em sua carca??a e ", 19, x_text, self.y_text + 40)
            self.game.draw_text("um pano com um pouco de emulsificante (detergente) e ??gua para o cabo.", 19, x_text, self.y_text + 60)
        if layer == 11:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Pode-se utilizar tamb??m algo com ponta macia como uma haste com ponta ", 19,x_text, self.y_text)
            self.game.draw_text("de algod??o para limpar os v??os dos bot??es.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Depois do mouse, ?? a vez do teclado.", 19, x_text,self.y_text + 40)
        if layer == 12:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Com ele j?? desconectado, deve-se vir??-lo de cabe??a para ", 21, 239,self.y_text)
            self.game.draw_text("baixo e chacoalh??-lo (se houver muita sujeira, pode-se ", 21, 239,self.y_text + 20)
            self.game.draw_text("tamb??m dar algumas batidas).", 21, 239, self.y_text + 40)
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
            self.game.draw_text("Quanto ?? limpeza de cada tecla, entre elas pode ser passado uma ", 21, x_text, self.y_text)
            self.game.draw_text("haste com ponta de algod??o com um pouco de ??lcool isoprop??lico ", 21, x_text, self.y_text + 20)
            self.game.draw_text("em suas pontas, o que facilita a limpeza.", 21, x_text, self.y_text + 40)
        if layer == 15:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Ao acabar com o teclado, chega a parte do monitor. Para ", self.font_size, 249, self.y_text)
            self.game.draw_text("limp??-lo n??o ?? recomendado nenhum tipo de l??quido, a ", self.font_size, 249, self.y_text + 20)
            self.game.draw_text("menos que um espec??fico para a limpeza de telas. Ent??o ", self.font_size, 249, self.y_text + 40)
            self.game.draw_text("deve-se passar um pano seco suavemente na tela.", self.font_size, 249, self.y_text + 60)
        if layer == 16:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A carca??a pode ser limpa com um pano umedecido e o cabo, do mesmo ", 20, x_text, self.y_text)
            self.game.draw_text("jeito que o do mouse.", 20, x_text, self.y_text + 20)
            self.game.draw_text("Por fim, h?? a parte externa do gabinete. Para limp??-la pode-se utilizar um ", 20, x_text, self.y_text + 40)
            self.game.draw_text("pano seco e umedecido, al??m do pincel antiest??tico nas entradas do gabinete. ", 20, x_text, self.y_text + 60)
            self.game.draw_text("?? melhor utilizar o pano seco na parte do espelho atr??s do gabinete.", 20, x_text, self.y_text + 80)
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
            self.game.draw_text("Depois de ter limpado a parte externa do computador, agora ?? preciso ", 21, x_text,self.y_text)
            self.game.draw_text("limpar a parte interna.", 21, x_text,self.y_text + 20)
        if layer == 22:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para fazer isso, primeiro ?? preciso abrir o gabinete. Alguns gabinetes ", 21, x_text,self.y_text)
            self.game.draw_text("possuem uma fechadura por travas e outros por parafuso. Nos gabinetes ", 21, x_text,self.y_text + 20)
            self.game.draw_text("fechados com parafuso ?? preciso tirar os parafusos, pelo menos os da", 21, x_text,self.y_text + 40)
            self.game.draw_text("parte que d?? acesso aos fans e ?? placa-m??e de", 21, x_text,self.y_text + 60)
            self.game.draw_text("maneira mais f??cil.", 21, x_text,self.y_text + 80)
        if layer == 23:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para que n??o haja problema, ?? recomendado colocar o gabinete com o ", 21, x_text,self.y_text)
            self.game.draw_text("lado de maior ??rea em contato com a superf??cie de apoio (deix??-lo deitado).", 21, x_text,self.y_text + 20)
            self.game.draw_text("Existem ordens diferentes de limpeza, ent??o vamos escolher uma, mas ", 21, x_text,self.y_text + 40)
            self.game.draw_text("n??o a tome como a ??nica.", 21, x_text,self.y_text + 60)
        if layer == 24:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Com o gabinete aberto, se o gabinete possuir muito tempo sem ", 19, 247,self.y_text)
            self.game.draw_text("limpeza, ?? bom utilizar um soprador com velocidade baixa para ", 19, 247,self.y_text + 20)
            self.game.draw_text("tirar o excesso da poeira.", 19, 247,self.y_text + 40)
        if layer == 25:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Algumas pessoas recomendam utilizar um secador de cabelo, mas ele  ", 21, x_text,self.y_text)
            self.game.draw_text("pode trazer muito perigo, pois, caso esteja no modo quente, pode ", 21, x_text,self.y_text + 20)
            self.game.draw_text("danificar os componentes internos, derretendo-os.", 21, x_text,self.y_text + 40)
            self.game.draw_text("Ent??o, se for utilizar o secador, ele deve ser colocado no modo ", 21, x_text,self.y_text + 60)
            self.game.draw_text("frio ou outra op????o que n??o seja a quente.", 21, x_text,self.y_text + 80)
        if layer == 26:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Caso n??o haja muita sujeira, um pincel antiest??tico serve. Esse tipo ", 21, x_text,self.y_text )
            self.game.draw_text("de pincel ?? necess??rio porque, caso seja feito de outros materiais, ", 21, x_text,self.y_text + 20)
            self.game.draw_text("pode gerar eletricidade est??tica com o atrito de sua ponta com os ", 21, x_text,self.y_text + 40)
            self.game.draw_text("componentes, podendo causar um curto circuito com algum componente", 21, x_text,self.y_text + 60)
            self.game.draw_text("da placa-m??e, por exemplo.", 21, x_text,self.y_text + 80)
        if layer == 27:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Para uma melhor limpeza, retire o dispositivo de armazenamento, ", 20, 247,self.y_text)
            self.game.draw_text("placa de v??deo e as RAMs de dentro do gabinete com um pouco de ", 20, 247,self.y_text + 20)
            self.game.draw_text("??lcool isoprop??lico. Deve-se ter cuidado para n??o arranhar os ???dentes??? dos  ", 20, 140,self.y_text + 50)
            self.game.draw_text("pentes de RAM e da placa de v??deo.", 20, 140,self.y_text + 70)
        if layer == 28:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para limpar o cooler da CPU, ele pode ser retirado e limpado separadamente, ou ", 19, x_text, self.y_text)
            self.game.draw_text("ainda internamente (mais uma vez, dependendo da quantidade de sujeira).", 19, x_text, self.y_text + 20)
            self.game.draw_text("Para limp??-lo, pode ser utilizado um pincel e um pano de microfibra para retirar ", 19, x_text, self.y_text + 40)
            self.game.draw_text("a poeira das p??s. Ser?? mais f??cil se elas estiverem travadas, ou com os dedos da ", 19, x_text, self.y_text + 60)
            self.game.draw_text("m??o, ou com algum suporte.", 19, x_text, self.y_text + 80)
        if layer == 29:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois, deve-se retirar os fans do gabinete, se poss??vel, e fazer a ", 19, x_text, self.y_text)
            self.game.draw_text("mesma limpeza do cooler. Para uma limpeza mais simples, pode ser ", 19, x_text, self.y_text + 20)
            self.game.draw_text("utilizado apenas o pincel e um pano de microfibra.", 19, x_text, self.y_text + 40)
            self.game.draw_text("A mesma forma se aplica aos fans da placa de v??deo, mas sem retir??-los dela.", 19, x_text, self.y_text + 60)
            self.game.draw_text("", 19, x_text, self.y_text + 80)
        if layer == 30:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A fonte tamb??m precisa ser limpa, pelo menos superficialmente. ?? mais ", 19, x_text, self.y_text)
            self.game.draw_text("complicado limp??-la internamente, ent??o, desde que o local onde ela ", 19, x_text, self.y_text + 20)
            self.game.draw_text("esteja fique limpo, n??o ser?? preciso abri-la. O processo de limpeza ?? ", 19, x_text, self.y_text + 40)
            self.game.draw_text("o mesmo: pincel antiest??tico e pano de microfibra.", 19, x_text, self.y_text + 60)
            self.game.draw_text("Durante todo o processo ?? preciso ter cuidado para n??o danificar as entradas dos ", 19, x_text, self.y_text + 80)
            self.game.draw_text("hardwares. ?? mais simples utilizar um soprador para tirar a maior parte da sujeira.", 19, x_text, self.y_text + 100)
        if layer == 31:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ao t??rmino da limpeza, os hardwares desconectados devem voltar para", 19, x_text, self.y_text)
            self.game.draw_text("onde estavam, do jeito que estavam e o gabinete deve ser fechado e ", 19, x_text, self.y_text + 20)
            self.game.draw_text("seus parafusos devem ser repostos.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Assim, est?? terminada a limpeza do computador. Ela ?? extremamente ", 19, x_text, self.y_text + 60)
            self.game.draw_text("necess??ria, pois nenhum local ?? livre de poeira por muito tempo e", 19, x_text, self.y_text + 80)
            self.game.draw_text("essa, por ser muito pequena, acaba entrando ou grudando no computador.", 19, x_text, self.y_text + 100)
        if layer == 32:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Mas a manuten????o preventiva n??o se trata apenas de limpeza. Ela ", 19, x_text, self.y_text)
            self.game.draw_text("se trata tamb??m de seguran??a.", 19, x_text, self.y_text + 20)
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
            self.game.draw_text("Vamos dar continuidade ?? manuten????o preventiva. Como dito ", 19, x_text,self.y_text)
            self.game.draw_text("anteriormente, ela n??o se trata somente de limpeza, mas tamb??m ", 19, x_text,self.y_text + 20)
            self.game.draw_text("de reposi????o e seguran??a. Uma das reposi????es feitas em uma manuten????o", 19, x_text,self.y_text + 40)
            self.game.draw_text("preventiva ?? a da pasta t??rmica. Mas voc?? deve estar se perguntando: ", 19, x_text,self.y_text + 60)
            self.game.draw_text("o que ?? pasta t??rmica? Ela ?? um componente muito importante para o ", 19, x_text,self.y_text + 80)
            self.game.draw_text("computador, pois ajuda a manter a temperatura da CPU baixa (da GPU tamb??m).", 19, x_text,self.y_text + 100)
        if layer == 36:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Ela possui uma textura pastosa e pode ser encontrada na cor branca ", 19, 250,self.y_text)
            self.game.draw_text("e prateada. A sua aplica????o ?? diretamente na parte de cima do ", 19, 250,self.y_text + 20)
            self.game.draw_text("processador.", 19, 250,self.y_text + 40)
        if layer == 37:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ela ?? aplicada uma vez e o cooler ?? colocado por cima, com a parte de ", 19, x_text,self.y_text)
            self.game.draw_text("cobre fazendo contato com a pasta, pressionando-a. Com a pasta t??rmica, ", 19, x_text,self.y_text + 20)
            self.game.draw_text("a condu????o do calor produzido pelo processador ?? mais rapidamente levado ", 19, x_text,self.y_text + 40)
            self.game.draw_text("para o cooler, que transfere o calor para fora do gabinete.", 19, x_text,self.y_text + 60)
        if layer == 38:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Essa transfer??ncia de calor pode ser tanto alta quanto baixa. Vai depender ", 19, x_text,self.y_text)
            self.game.draw_text("do valor da condutividade t??rmica de cada pasta, ou seja, do material que a ", 19, x_text,self.y_text + 20)
            self.game.draw_text("pasta ?? feita.", 19, x_text,self.y_text + 40)
        if layer == 39:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("As unidades de condutividade t??rmica mais utilizadas no mercado ", 19, 255,self.y_text)
            self.game.draw_text("s??o W/mK (Watt por metro Kelvin), W/m??K (Watt por metro quadrado ", 19, 255,self.y_text + 20)
            self.game.draw_text("Kelvin) e W/m??/??C (Watt por metro quadrado por grau Celsius). ", 19, 255,self.y_text + 40)
            self.game.draw_text("Existem pastas t??rmicas com valores de condutividade t??rmica", 19, 255,self.y_text + 60)
            self.game.draw_text("baixos, como 1,46 W/mK, at?? pastas com valores muito altos, ", 19, 255,self.y_text + 80)
            self.game.draw_text("como 73 W/mk.", 19, 255,self.y_text + 100)
        if layer == 40:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Quanto maior a condutividade t??rmica, maior ?? o pre??o da pasta t??rmica e ", 19, x_text,self.y_text)
            self.game.draw_text("menor ?? a sua quantidade. Por exemplo, a pasta de condutividade t??rmica ", 19, x_text,self.y_text + 20)
            self.game.draw_text("de 1,46 W/mK pode ser comprada com um tubo com 38 gramas de pasta. ", 19, x_text,self.y_text + 40)
            self.game.draw_text("J?? na de 73 W/mk, o tubo vem com 1 (um) grama apenas.", 19, x_text,self.y_text + 60)
        if layer == 41:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora ?? que entraremos na manuten????o propriamente dita: essa pasta ", 19, x_text,self.y_text)
            self.game.draw_text("perde a capacidade de transfer??ncia ao longo do tempo, independente ", 19, x_text,self.y_text + 20)
            self.game.draw_text("da condutividade, e por isso ela deve ser trocada em determinados ", 19, x_text,self.y_text + 40)
            self.game.draw_text("intervalos de tempo.", 19, x_text,self.y_text + 60)
        if layer == 42:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Al??m disso, ?? importante saber que todos os processadores geram calor. ", 19, x_text,self.y_text)
            self.game.draw_text("Isso ocorre por causa da energia consumida para realizar os c??lculos", 19, x_text,self.y_text + 20)
            self.game.draw_text("computacionais. Como o rendimento de nenhuma m??quina ?? perfeito, boa ", 19, x_text,self.y_text + 40)
            self.game.draw_text("parte da energia ?? dissipada na forma de calor e concentrada na CPU. ", 19, x_text,self.y_text + 60)
            self.game.draw_text("E quanto maior for o requerimento de pot??ncia computacional, maior", 19, x_text,self.y_text + 80)
            self.game.draw_text("ser?? a produ????o de calor. Da?? entra o papel da pasta t??rmica.", 19, x_text,self.y_text + 100)
        if layer == 43:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Boas pastas t??rmicas n??o precisam de tanta preocupa????o quanto a sua ", 19, x_text,self.y_text)
            self.game.draw_text("troca, sendo necess??ria uma troca a cada 2 anos ou mais. J?? as pastas ", 19, x_text,self.y_text + 20)
            self.game.draw_text("t??rmicas mais modestas, essas precisam de um intervalo de tempo menor ", 19, x_text,self.y_text + 40)
            self.game.draw_text("para serem trocadas, de 1 ano a 6 meses.", 19, x_text,self.y_text + 60)
            self.game.draw_text("Mas voc?? pode estar pensando: ?? poss??vel utilizar o computador sem", 19, x_text,self.y_text + 80)
            self.game.draw_text("pasta t??rmica?", 19, x_text,self.y_text + 100)
        if layer == 44:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A resposta ?? sim, mas n??o por muito tempo. Os processadores possuem ", 19, x_text, self.y_text)
            self.game.draw_text("mecanismos que fazem diminuir o seu clock ao serem submetidos a grandes ", 19, x_text, self.y_text + 20)
            self.game.draw_text("temperaturas, havendo tamb??m uma temperatura m??xima que, caso chegue, o ", 19, x_text,self.y_text + 40)
            self.game.draw_text("computador desliga.", 19, x_text,self.y_text + 60)
        if layer == 45:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Sem a pasta t??rmica, um processador pode facilmente chegar ", 19, 255, self.y_text)
            self.game.draw_text("aos 100 ??C, dependendo da aplica????o, e desligar.", 19, 255, self.y_text + 20)
            self.game.draw_text("Esse desligamento pode causar danos s??rios n??o apenas na CPU, ", 19, 255, self.y_text + 40)
            self.game.draw_text("mas tamb??m em todos os outros componentes, como arquivos ou ", 19, 255, self.y_text + 60)
            self.game.draw_text("um disco de armazenamento inteiro corrompido.", 19, 255, self.y_text + 80)
        if layer == 46:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Voc?? vai ver agora como colocar e trocar uma pasta t??rmica no computador.", 19, x_text, self.y_text)
            self.game.draw_text("O processo de coloca????o e de troca de pasta t??rmica ?? semelhante.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Na primeira vez, com o computador desconectado da tomada e o processador ", 19, x_text, self.y_text + 40)
            self.game.draw_text("j?? encaixado em seu socket, deve-se ter em m??os a pasta (em tubo ou em um pote).", 19, x_text, self.y_text + 60)
        if layer == 47:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Caso a pasta venha em um tubo, o processo de aplica????o ?? mais simples: ", 19, x_text, self.y_text)
            self.game.draw_text("basta colocar uma ??nica e pequena gota no centro do processador.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Depois disso, essa gota pode ser espalhada por toda a superf??cie do ", 19, x_text, self.y_text + 40)
            self.game.draw_text("processador, delicadamente, utilizando uma haste de algod??o, ou ", 19, x_text, self.y_text + 60)
            self.game.draw_text("deix??-la do jeito que est?? para a pr??xima etapa.", 19, x_text, self.y_text + 80)
        if layer == 48:
            #FAZER JOGO
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Nessa parte, o cooler deve ser posto em cima do processador com a ", 19, 250, self.y_text)
            self.game.draw_text("pasta t??rmica a fim de pression??-la, pois quanto maior o contato,", 19, 250, self.y_text + 20)
            self.game.draw_text("melhor a condutividade.", 19, 250, self.y_text + 40)
        if layer == 49:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Contudo, a press??o ser?? feita com o encaixe dos pinos ou com os  ", 19, x_text, self.y_text)
            self.game.draw_text("parafusos do cooler enroscados na placa-m??e. Se o cooler for ", 19, x_text, self.y_text + 20)
            self.game.draw_text("pressionado antes, pode escorregar com a pasta e danificar a ", 19, x_text, self.y_text + 40)
            self.game.draw_text("placa-m??e. Pronto! J?? est?? colocado", 19, x_text, self.y_text + 60)
        if layer == 50:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora, para trocar a pasta t??rmica, algumas etapas s??o adicionadas: ", 19, x_text, self.y_text)
            self.game.draw_text("primeiro, se a placa-m??e j?? estiver dentro do gabinete, deve-se deit??-lo ", 19, x_text, self.y_text + 20)
            self.game.draw_text("para realizar essa opera????o.", 19, x_text, self.y_text + 40)
        if layer == 51:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois, deve-se retirar o cooler da placa-m??e. Com o cooler retirado, ", 19, 250, self.y_text)
            self.game.draw_text("deve-se limpar a pasta t??rmica presente no cooler e no processador, ", 19, 250, self.y_text + 20)
            self.game.draw_text("que provavelmente estar?? dura e seca.", 19, 250, self.y_text + 40)
        if layer == 52:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Nessas partes n??o ?? recomendado utilizar nenhum l??quido. Para tirar ", 19, x_text, self.y_text)
            self.game.draw_text("o excesso da pasta t??rmica anterior pode-se utilizar um papel com ", 19, x_text, self.y_text + 20)
            self.game.draw_text("textura n??o t??o dura, como o de um guardanapo ou papel higi??nico.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Tamb??m pode-se utilizar um pano, mas ser?? mais dif??cil de limp??-lo depois.", 19, x_text, self.y_text + 60)
        if layer == 53:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para limpar a pasta t??rmica do processador da melhor maneira,", 19, x_text, self.y_text)
            self.game.draw_text("?? preciso retir??-lo da placa-m??e. O processo de limpeza ?? o ", 19, x_text, self.y_text + 20)
            self.game.draw_text("mesmo do cooler.", 19, x_text, self.y_text + 40)
        if layer == 54:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Depois, basta realizar os mesmos passos da coloca????o da pasta ", 19, 250, self.y_text)
            self.game.draw_text("t??rmica, vistos agora a pouco.", 19, 250, self.y_text + 20)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 19, 250, self.y_text + 40)
        if layer == 55:
            #FAZER JOGO
            pass
        if layer == 56:
            self.draw_very_good()
        if layer == 57:
            #FAZER JOGO
            pass
        if layer == 58:
            self.draw_very_good()
        if layer == 59:
            #FAZER JOGO
            pass
        if layer == 60:
            self.draw_very_good()
        if layer == 61:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora vamos ver outra parte da manuten????o preventiva. A seguran??a.", 19, x_text, self.y_text)
            self.game.draw_text("Uma das seguran??as que se deve ter ao utilizar o computador ?? a", 19, x_text, self.y_text + 20)
            self.game.draw_text("respeito da fonte de energia. N??o da fonte presente no computador", 19, x_text, self.y_text + 40)
            self.game.draw_text("mas da energia da tomada que ?? ligada ?? ela.", 19, x_text, self.y_text + 60)
        if layer == 62:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Essa energia ligada diretamente no computador pode possuir varia????es,  ", 19, x_text, self.y_text)
            self.game.draw_text("principalmente em per??odos de tempestades ou manuten????es na rede el??trica, ", 19, x_text, self.y_text + 20)
            self.game.draw_text("sem contar na varia????o mais comum, chegando at?? 10% do valor estimado de ", 19, x_text, self.y_text + 40)
            self.game.draw_text("de diferen??a de potencial. Tudo isso agrava a vida ??til da m??quina.", 19, x_text, self.y_text + 60)
        if layer == 63:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Mas n??o apenas problemas a longo prazo podem acontecer, como a ", 19, x_text, self.y_text)
            self.game.draw_text("curto prazo tamb??m. Um computador desligando por causa de uma ", 19, x_text, self.y_text + 20)
            self.game.draw_text("queda de energia ou um pico pode gerar diversos problemas, como ", 19, x_text, self.y_text + 40)
            self.game.draw_text("perda de arquivos ou danifica????o de dispositivos de armazenamento.", 19, x_text, self.y_text + 60)
        if layer == 64:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ent??o, para diminuir as chances de problemas causados pelo pr??prio ", 19, x_text, self.y_text)
            self.game.draw_text("fornecimento de energia, podem ser instalados dispositivos que fazem ", 19, x_text, self.y_text + 20)
            self.game.draw_text("o papel intermedi??rio entre a rede el??trica e o computador.", 19, x_text, self.y_text + 40)
            self.game.draw_text("S??o eles: Estabilizador, filtro de linha e No Break.", 19, x_text, self.y_text + 60)
        if layer == 65:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Tanto o estabilizador quanto filtro de linha fornece alguma seguran??a, ", 19, x_text, self.y_text)
            self.game.draw_text("como a prote????o por oscila????es e prote????o contra interfer??ncias", 19, x_text, self.y_text + 20)
            self.game.draw_text("eletromagn??ticas e surtos de tens??o, por??m, atualmente, n??o s??o mais ", 19, x_text, self.y_text + 40)
            self.game.draw_text("t??o necess??rios. ", 19, x_text, self.y_text + 60)
            self.game.draw_text("  ", 19, x_text, self.y_text + 80)
            self.game.draw_text("", 19, x_text, self.y_text + 100)
        if layer == 66:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Isso ocorre por causa do melhoramento das fontes de computadores e,", 19,250, self.y_text)
            self.game.draw_text("al??m disso, muitos estabilizadores e filtros de linha impedem o ", 19,250, self.y_text + 20)
            self.game.draw_text("funcionamento de alguns computadores atuais, al??m de pararem de ", 19,250, self.y_text + 40)
            self.game.draw_text("funcionar na primeira ???prote????o??? de energia.", 19,250, self.y_text + 60)
        if layer == 67:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Ent??o o melhor dispositivo presente no mercado ?? o No Break, tamb??m ", 19,250, self.y_text)
            self.game.draw_text("chamado de UPS. Ele funciona como um am??lgama das melhores caracter??sticas ", 19,250, self.y_text + 20)
            self.game.draw_text("do filtro de linha e do estabilizador, mas com alguns adicionais.", 19,250, self.y_text + 40)
            self.game.draw_text("estabilizador, mas com alguns adicionais. Ele fornece prote????o contra ", 19,250, self.y_text + 60)
            self.game.draw_text("surtos e quedas de tens??o, prote????o contra queda na energia de todo o ", 19,250, self.y_text + 80)
            self.game.draw_text("local, pois possui uma bateria interna, e prote????o contra oscila????o da frequ??ncia.", 19,250, self.y_text + 100)
        if layer == 68:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Quando h?? uma falta de energia, o no break consegue fornecer, em m??dia,", 19,250, self.y_text)
            self.game.draw_text("15 minutos de energia, dependendo da bateria interna.", 19,250, self.y_text + 20)
            self.game.draw_text("Isso d?? tempo suficiente para desligar o computador corretamente,", 19,250, self.y_text + 40)
            self.game.draw_text("sem perder arquivos.", 19,250, self.y_text + 60)
        if layer == 69:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Ele n??o serve apenas para conectar a fonte do computador, mas tamb??m ", 19,250, self.y_text)
            self.game.draw_text("o monitor. O n??mero de entradas de tomadas tamb??m varia para cada ", 19,250, self.y_text + 20)
            self.game.draw_text("dispositivo e sua instala????o consiste em conectar os cabos da fonte ", 19,250, self.y_text + 40)
            self.game.draw_text("e do monitor nele e o seu cabo na tomada, depois lig??-lo.", 19,250, self.y_text + 60)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos.", 19,250, self.y_text + 80)
        if layer == 70:
            #fazer jogo
            pass
        if layer == 71:
            self.draw_very_good()
        if layer == 72:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Uma ??ltima pr??tica da manuten????o preventiva de seguran??a ?? a realiza????o de ", 19, 255, self.y_text)
            self.game.draw_text("backup e instala????o de softwares de prote????o.", 19, 255, self.y_text + 20)
            self.game.draw_text("O backup ?? uma das formas de seguran??a para os dados presentes no computador. ", 19, 150,self.y_text + 40)
            self.game.draw_text("Ele ?? um processo de c??pia de seguran??a dos arquivos presentes no dispositivo ", 19, 150,self.y_text + 60)
            self.game.draw_text("de armazenamento.", 19, 150,self.y_text + 80)
        if layer == 73:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Realizar backup ?? muito importante, pois, mesmo tendo o melhor hardware do momento, ", 19, x_text, self.y_text)
            self.game.draw_text("ainda assim os dispositivos n??o s??o infal??veis. Al??m disso, alguns possuem mecanismos", 19, x_text, self.y_text + 20)
            self.game.draw_text("de recupera????o, outros n??o (como ?? o caso do SSD caso  haja um problema f??sico)", 19, x_text, self.y_text + 40)
            self.game.draw_text("Existem dois tipos de backups: os de m??dia f??sicos e os na nuvem.", 19, x_text, self.y_text + 40)
        if layer == 74:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os de m??dia f??sica s??o feitos com a c??pia dos arquivos de um dispositivo de", 19, x_text, self.y_text)
            self.game.draw_text("armazenamento para o outro (de um HD para outro ou SSD), ou no mesmo o dispositivo.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Para isso, existem HDs e SSDs externos, capazes de armazenar grandes quantidades ", 19, x_text, self.y_text + 40)
            self.game.draw_text("de arquivos e s??o f??ceis de instalar, pois utilizam geralmente a porta USB, podendo ", 19, x_text, self.y_text + 60)
            self.game.draw_text("ser conectados diretamente no exterior do gabinete.", 19, x_text, self.y_text + 80)
        if layer == 75:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("No caso dos backups no mesmo dispositivo, est??o sujeitos a perdas ", 19, 250, self.y_text)
            self.game.draw_text("caso o dispositivo tenha falha, por??m, a c??pia interna traz mais ", 19, 250, self.y_text + 20)
            self.game.draw_text("praticidade para o usu??rio caso queira acess??-la rapidamente.", 19, 250, self.y_text + 40)
        if layer == 76:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O backup na nuvem consiste na c??pia de arquivos para um sistema de", 19, x_text, self.y_text)
            self.game.draw_text("armazenamento online. Geralmente esses sistemas s??o pagos para  ", 19, x_text, self.y_text + 20)
            self.game.draw_text("grandes capacidades, mas existem vers??es gratuitas para tamanhos ", 19, x_text, self.y_text + 40)
            self.game.draw_text("menores. Atualmente, s??o os mais utilizados, principalmente por ", 19, x_text, self.y_text + 60)
            self.game.draw_text("causa da praticidade.", 19, x_text, self.y_text + 80)
        if layer == 77:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Como compara????o, para acessar um backup em uma m??dia f??sica, ?? preciso ", 19, x_text, self.y_text)
            self.game.draw_text("instal??-la em um dispositivo que possua uma conex??o adequada. J?? os", 19, x_text, self.y_text + 20)
            self.game.draw_text("backups da nuvem podem ser acessados em qualquer dispositivo com acesso", 19, x_text, self.y_text + 40)
            self.game.draw_text("?? internet, desde que o usu??rio contenha as devidas credenciais do ", 19, x_text, self.y_text + 60)
            self.game.draw_text("servi??o de armazenamento adquirido.", 19, x_text, self.y_text + 80)
        if layer == 78:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Os backups ainda possuem n??veis de arquivos, podendo ser feita a ", 19, 255, self.y_text)
            self.game.draw_text("c??pia apenas de arquivos de m??dia audiovisual e documentos, como ", 19, 255, self.y_text + 20)
            self.game.draw_text("tamb??m modifica????es feitas, ou at?? todo o sistema. Este ?? chamado ", 19, 255, self.y_text + 40)
            self.game.draw_text("de backup completo, muito utilizado em empresas e em migra????es", 19, 255, self.y_text + 60)
            self.game.draw_text("de SOs de HDs para SSDs.", 19, 255, self.y_text + 80)
        if layer == 79:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Lembre-se de que se um hardware quebrar ou parar de funcionar, pode ser", 19, x_text, self.y_text)
            self.game.draw_text("substitu??do. Mas se um arquivo de documento, ??udio ou v??deo for perdido,", 19, x_text, self.y_text + 20)
            self.game.draw_text(" n??o h?? como recuper??-lo.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 19, x_text, self.y_text + 60)
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
            self.game.draw_text("Agora voc?? vai ver como instalar a fonte no gabinete. ", 19, x_text, self.y_text)
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
            #FAZER JOGO
            pass
        if layer == 86:
            self.draw_very_good()
        if layer == 87:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Enfim, a ??ltima pr??tica de manuten????o preventiva. A prote????o do ", 19, x_text, self.y_text)
            self.game.draw_text("sistema. Uma das formas para uma pessoa leiga em inform??tica", 19, x_text, self.y_text + 20)
            self.game.draw_text("reduzir as chances de um reparo ou aumentar os intervalos de", 19, x_text, self.y_text + 40)
            self.game.draw_text("manuten????o preventiva ?? o uso de softwares de seguran??a, como os ", 19, x_text, self.y_text + 60)
            self.game.draw_text("antiv??rus e programas de limpeza de arquivos tempor??rios e ", 19, x_text, self.y_text + 80)
            self.game.draw_text("desnecess??rios.", 19, x_text, self.y_text + 100)
        if layer == 88:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Al??m disso, tamb??m ?? importante sempre atualizar os softwares,", 19, x_text, self.y_text)
            self.game.draw_text("sejam as atualiza????es do SO, framework ou programas.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Enfim, voc?? terminou a fase 6. Na pr??xima fase voc?? ver?? um", 19, x_text, self.y_text + 40)
            self.game.draw_text("pouco sobre manuten????o corretiva.", 19, x_text, self.y_text + 60)
        if layer == 89:
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
            