import pygame, time
from data.score import *
from pygame.locals import *
from data.questions import *


class Fases4():
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


class FaseFourWorldOne(Fases4):
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
        Fases4.__init__(self, game)

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
        if self.game.SPACE_KEY and self.layers[len(self.layers) - 1] != 41:
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
            if not self.gamimg_layer and self.layers[len(self.layers) - 1] == 99:
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
            self.game.draw_text("Voc?? vai aprender agora um pouco sobre os outros hardwares", self.font_size, x_text, self.y_text)
        if layer == 2:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("As mem??rias no computador s??o dispositivos que podem armazenar ", self.font_size, x_text, self.y_text)
            self.game.draw_text("dados de maneira tempor??ria ou permanente. A partir disso elas ", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("s??o classificadas em mem??rias vol??teis e n??o vol??teis.", self.font_size, x_text, self.y_text + 40)
        if layer == 3:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Uma mem??ria vol??til armazena dados apenas na presen??a de energia. ", self.font_size, 125, 360)
            self.game.draw_text("Caso a n??o haja energia, toda a informa????o contida nela ?? perdida ", self.font_size, 125, 415)
            self.game.draw_text("e por isso seu armazenamento ?? tempor??rio. Alguns tipos de  ", self.font_size, 125, 435)
            self.game.draw_text("mem??rias vol??teis s??o a RAM e a mem??ria cache.", self.font_size, 125, 455)
        if layer == 4:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Uma mem??ria n??o vol??til n??o perde os dados escritos na aus??ncia de ", self.font_size, x_text, self.y_text)
            self.game.draw_text("energia, por isso que a informa????o contida nela ?? duradoura. Alguns", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("tipos de mem??rias n??o vol??teis s??o as mem??rias flash, ROM,", self.font_size, x_text, self.y_text + 40)
            self.game.draw_text("a unidade de estado s??lido e o disco r??gido.", self.font_size, x_text, self.y_text + 60)
            self.game.draw_text("Vamos come??ar com a mem??ria RAM.", self.font_size, x_text, self.y_text + 80)
        if layer == 5:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A RAM, sigla cuja tradu????o consiste em mem??ria de acesso rand??mico, ",self.font_size, x_text, self.y_text)
            self.game.draw_text("?? uma mem??ria vol??til importante para o processamento das ", self.font_size,x_text, self.y_text + 20)
            self.game.draw_text("informa????es, por isso ela ?? classificada tamb??m como mem??ria", self.font_size,x_text, self.y_text + 40)
            self.game.draw_text("primeira.", self.font_size,x_text, self.y_text + 60)
        if layer == 6:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O acesso rand??mico faz refer??ncia aos modo como transistores", self.font_size,251, self.y_text)
            self.game.draw_text("e capacitores s??o utilizados para referenciar bits 0 e 1, sendo ", self.font_size,251, self.y_text + 20)
            self.game.draw_text("que s??o selecionados aleatoriamente enquanto houver corrente", self.font_size,251, self.y_text + 40)
            self.game.draw_text("passando por eles.", self.font_size,251, self.y_text + 60)
        if layer == 7:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ao iniciar o computador, as informa????es que o processador necessita", 20, x_text, self.y_text)
            self.game.draw_text("para serem usadas em um curto per??odo de tempo e s??o muito grandes ", 20, x_text,self.y_text + 20)
            self.game.draw_text("erem armazenadas na mem??ria cache ficam armazenadas na RAM. ", 20, x_text, self.y_text + 40)
        if layer == 8:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Inicialmente, as informa????es de inicializa????o ficam armazenadas nas", 20, x_text, self.y_text)
            self.game.draw_text("mem??rias n??o vol??teis e s??o transmitidas para a RAM, que por sua vez ", 20, x_text,self.y_text + 20)
            self.game.draw_text("as transmite para o processador.", 20, x_text, self.y_text + 40)
            self.game.draw_text("O processador ?? quem recorre ao acesso da RAM, fazendo uma c??pia dos", 20, x_text, self.y_text + 60)
            self.game.draw_text("dados necess??rios para a mem??ria cache caso haja um uso desses dados", 20, x_text, self.y_text + 80)
            self.game.draw_text("algum tempo depois.", 20, x_text, self.y_text + 100)
        if layer == 9:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Voc?? deve estar pensando: por que o processador n??o acessa", 20, 250, self.y_text)
            self.game.draw_text("as informa????es diretamente da mem??ria n??o vol??til?", 20, 250,self.y_text + 20)
        if layer == 10:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Atualmente, isso ocorre devido ao tempo de transfer??ncia de dados. Para ", 19, x_text, self.y_text)
            self.game.draw_text("voc?? perceber a diferen??a, dependendo do processador e da mem??ria n??o vol??til,", 19, x_text, self.y_text + 20)
            self.game.draw_text("a velocidade de acesso em compara????o com a RAM ?? 60 mil vezes mais lenta, ou ", 19, x_text, self.y_text + 40)
            self.game.draw_text("seja, n??o vale a pena.", 19, x_text, self.y_text + 60)
        if layer == 11:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Agora veja um exemplo de funcionamento da trajet??ria de uma informa????o ao ", 19,x_text, self.y_text)
            self.game.draw_text("executar um programa:", 19, x_text, self.y_text + 20)
            self.game.draw_text("...abrindo um programa.", 19, x_text,self.y_text + 40)
            self.game.draw_text("HD -> RAM -> CPU.", 19, x_text,self.y_text + 60)
            self.game.draw_text("Note que enquanto o programa estiver rodando no computador, ele estar?? ", 19, x_text,self.y_text + 80)
            self.game.draw_text("tomando espa??o na RAM.", 19, x_text,self.y_text + 100)
        if layer == 12:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Uma fonte nominal ainda possui o risco de queimar os ", 21, 239,self.y_text)
            self.game.draw_text("componentes ligados a ela caso haja algum problema, podendo ", 21, 239,self.y_text + 20)
            self.game.draw_text("ser um iniciador de inc??ndio.", 21, 239, self.y_text + 40)
            self.game.draw_text("Agora voc?? vai ver como conectar uma fonte na placa-m??e e nos", 21, 239, self.y_text + 60)
            self.game.draw_text("outros componentes.", 21, 239, self.y_text + 80)
        if layer == 13:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Durante a evolu????o do hardware de mem??ria de acesso remoto houveram", 21, x_text, self.y_text)
            self.game.draw_text("diversos padr??es de tecnologias com cada uma ditando a capacidade", 21, x_text, self.y_text + 20)
            self.game.draw_text("m??xima da RAM. Alguns dos padr??es de mem??ria s??o simm, dimm, ddr3 ", 21, x_text, self.y_text + 40)
            self.game.draw_text("sdram e ddr4 sdram.", 21, x_text, self.y_text + 60)
        if layer == 14:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O padr??o mais antigo e n??o mais utilizado ?? o simm, sigla para Single", 21, x_text, self.y_text)
            self.game.draw_text("In-Line Memory Module. O substituto para o simm foi o dimm, sigla", 21, x_text, self.y_text + 20)
            self.game.draw_text("para Dual Inline Memory Module, que possu??a o dobro da capacidade e", 21, x_text, self.y_text + 40)
            self.game.draw_text("taxa de transmiss??o.", 21, x_text, self.y_text + 60)
        if layer == 15:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O padr??o DDR, sigla para Double-Data-Rate introduziu a t??cnica ", self.font_size, 249, self.y_text)
            self.game.draw_text("de duplica????o de taxa de transfer??ncia, fazendo com que a ", self.font_size, 249, self.y_text + 20)
            self.game.draw_text("capacidade de transmiss??o aumentasse mais uma vez e assim ", self.font_size, 249, self.y_text + 40)
            self.game.draw_text("ocorreu para os consecutivos Padr??es DDR.", self.font_size, 249, self.y_text + 60)
        if layer == 16:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os padr??es mais comuns, atualmente, de RAM s??o os DDR3 e DDR4.", 20, x_text, self.y_text)
            self.game.draw_text("O padr??o DDR3 permite a cria????o de mem??rias com frequ??ncia de 800 MHz at?? ", 20, x_text, self.y_text + 20)
            self.game.draw_text("2400 MHz e possui uma capacidade de armazenamento de at?? 8 GB por slot. ", 20, x_text, self.y_text + 40)
            self.game.draw_text("Algumas placas-m??e possuem at?? mais de 4 slots de RAM, ent??o pode-se ", 20, x_text, self.y_text + 60)
            self.game.draw_text("aumentar a capacidade mesmo com a limita????o de 8 GB por slot.", 20, x_text, self.y_text + 80)
        if layer == 17:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O padr??o DDR4 ?? o mais recente. Ele permite a cria????o de mem??rias com", 21, x_text, self.y_text)
            self.game.draw_text("frequ??ncia de 2.133 at?? 4.266 MHz e possui uma capacidade de ", 21, x_text, self.y_text + 20)
            self.game.draw_text("armazenamento de at?? 16 GB por slot.", 21, x_text, self.y_text + 40)
        if layer == 18:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("A mesma caracter??stica da placa-m??e DDR3 vale para a DDR4, por??m,", 19, 249,self.y_text)
            self.game.draw_text("n??o ?? poss??vel utilizar uma mem??ria de um padr??o em um slot de outro. ", 19, 249,self.y_text + 20)
            self.game.draw_text("Al??m do encaixe n??o ser poss??vel, h?? o risco de perda ou excesso de ", 19, 249,self.y_text + 40)
            self.game.draw_text("energia, pois a mem??ria DDR3 (1.5V) requer uma tens??o maior do que a ", 19, 249,self.y_text + 60)
            self.game.draw_text("DDR4 (1.2V). Por isso que as placas-m??e precisam ser ", 19, 249,self.y_text + 80)
            self.game.draw_text("compat??veis com o tipo de mem??ria.", 19, 249,self.y_text + 100)
        if layer == 19:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Sobre as marcas, devido ?? relativa simplicidade de cria????o da mem??ria de ", 19,x_text, self.y_text)
            self.game.draw_text("acesso rand??mico, h?? uma quantidade de empresas muito maior do que as de ", 19,x_text, self.y_text + 20)
            self.game.draw_text("processadores.", 19,x_text, self.y_text + 40)
        if layer == 20:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A nomenclatura de uma mem??ria DDR ?? a seguinte: DDR() []/PC() {} ", 19, x_text,self.y_text )
            self.game.draw_text("O par??ntesis indica o tipo de DDR (2, 3, 4 ou 5).", 19, x_text,self.y_text + 20)
            self.game.draw_text("O colchete indica o clock m??ximo da mem??ria.", 19, x_text,self.y_text + 40)
            self.game.draw_text("A chave indica a velocidade m??xima de transfer??ncia de dados, medida em mb/s.", 19, x_text,self.y_text + 60)
            self.game.draw_text("A diferen??a entre frequ??ncia e velocidade de transfer??ncia ?? que a", 19, x_text,self.y_text + 80)
            self.game.draw_text("transfer??ncia de dados ?? feita a cada determinada quantidade de ciclos.", 19, x_text,self.y_text + 100)
        if layer == 21:
            #FAZER JOGO
            pass
        if layer == 22:
            self.draw_very_good()
        if layer == 23:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Outras caracter??sticas que podemos ver sobre a RAM ?? que a sua ", 21, x_text,self.y_text)
            self.game.draw_text("frequ??ncia m??xima ?? premeditada pelo processador instalado.", 21, x_text,self.y_text + 20)
            self.game.draw_text("Processadores da Intel da 6?? e 7?? gera????o, por exemplo, permitem uma", 21, x_text,self.y_text + 40)
            self.game.draw_text("frequ??ncia m??xima de mem??ria de 2.400 MHz, mesmo se a mem??ria for", 21, x_text,self.y_text + 60)
            self.game.draw_text("de 3.200 MHz.", 21, x_text,self.y_text + 80)
        if layer == 24:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Uma parte maior dos processadores da AMD j?? possuem uma libera????o", 19, 247,self.y_text)
            self.game.draw_text("de frequ??ncia mais alta do que os da Intel.", 19, 247,self.y_text + 20)
        if layer == 25:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Al??m disso, ao utilizar mais de uma mem??ria, o recomendado ?? que ", 21, x_text,self.y_text)
            self.game.draw_text("tenham a mesma frequ??ncia, independente da marca, pois com", 21, x_text,self.y_text + 20)
            self.game.draw_text("frequ??ncias diferentes, o processador precisa acess??-las de uma ", 21, x_text,self.y_text + 40)
            self.game.draw_text("mesma maneira, ent??o ele vai igualar a frequ??ncia da RAM baseando-", 21, x_text,self.y_text + 60)
            self.game.draw_text("-se na menor frequ??ncia, ou seja, ocorre uma perda de velocidade.", 21, x_text,self.y_text + 80)
        if layer == 26:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Um canal de mem??ria apenas pode n??o ser suficiente para acompanhar ", 21, x_text, self.y_text)
            self.game.draw_text("a velocidade dos processadores. A partir disso surgiu a pr??tica", 21, x_text, self.y_text + 20)
            self.game.draw_text("de dual-channel, que nada mais ?? do que utilizar mem??rias em", 21, x_text, self.y_text + 40)
            self.game.draw_text("uma configura????o que dobre a capacidade de transfer??ncia e leitura", 21, x_text, self.y_text + 60)
            self.game.draw_text("de informa????es para o processador.", 21, x_text, self.y_text + 80)
        if layer == 27:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Esse tipo de configura????o depende da especifica????o da placa-", 20, 247,self.y_text)
            self.game.draw_text("-m??e do processador. Atualmente, ele ?? t??o comum que j?? est?? ", 20, 247,self.y_text + 20)
            self.game.draw_text("presente na maioria dos computadores. A recomenda????o para", 20, 247,self.y_text + 40)
            self.game.draw_text("o uso do dual-channel ?? que se utilize pentes de mem??rias com ", 20, 247,self.y_text + 60)
            self.game.draw_text("a mesma capacidade de armazenamento e frequ??ncia e que ", 20, 247,self.y_text + 80)
            self.game.draw_text("seja mais de um pente e em n??mero par de quantidade.", 20, 247,self.y_text + 100)
        if layer == 28:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Perceba que se utilizar apenas um pente de RAM DDR4 de 8 GB e dois pentes de ", 19, x_text, self.y_text)
            self.game.draw_text("RAM DDR4 de 4 GB cada, a segunda op????o acaba sendo mais r??pida do que a", 19, x_text, self.y_text + 20)
            self.game.draw_text("rimeira, mesmo com a mesma capacidade.", 19, x_text, self.y_text + 40)
            self.game.draw_text("O modo de como as RAMs foram instaladas por voc?? durante a pr??tica anterior", 19, x_text, self.y_text + 60)
            self.game.draw_text("?? em dual-channel.", 19, x_text, self.y_text + 80)
        if layer == 29:
            #FAZER JOGO
            pass
        if layer == 30:
            self.draw_very_good()
        if layer == 31:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A ROM, sigla para Ready-Only Memory, ?? uma mem??ria n??o vol??til.", 19, x_text, self.y_text)
            self.game.draw_text("Ela armazena uma informa????o feita pelo fabricante uma ??nica", 19, x_text, self.y_text + 20)
            self.game.draw_text("vez e que, depois disso, s?? pode ser lida, ou seja, n??o ?? poss??vel", 19, x_text, self.y_text + 40)
            self.game.draw_text("alterar ou remover a informa????o. Da?? o seu nome: mem??ria somente de", 19, x_text, self.y_text + 60)
            self.game.draw_text("leitura.", 19, x_text, self.y_text + 80)
        if layer == 32:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O termo ROM ?? utilizado para identificar v??rios tipos de mem??ria, como a ", 19, x_text, self.y_text)
            self.game.draw_text("mem??ria prom, eprom, eeprom e mem??ria flash.", 19, x_text, self.y_text + 20)
        if layer == 33:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("A mem??ria prom, sigla para Programmable Read-Only Memory, ?? ", 19, 243, self.y_text)
            self.game.draw_text("utilizada para programar informa????es de dispositivos especiais e ", 19, 243, self.y_text + 20)
            self.game.draw_text("armazen??-las nessa mem??ria para depois ser utilizada apenas como ", 19, 243, self.y_text + 40)
            self.game.draw_text("leitura.", 19, 243, self.y_text + 60)
        if layer == 34:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A eprom, sigla para Erasable Programmable Read-Only Memory, ?? um tipo de ", 19, x_text, self.y_text)
            self.game.draw_text("mem??ria cujos dados podem ser apagados por meio de radia????o ultravioleta.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Apenas com isso ?? poss??vel reutiliz??-la.", 19, x_text, self.y_text + 40)
            self.game.draw_text("H?? ainda outras formas de apagar as informa????es da ROM, depende do seu tipo.", 19, x_text, self.y_text + 60)
        if layer == 35:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os hardwares instalados no PCI-E possuem entradas externas e por", 19, x_text, self.y_text)
            self.game.draw_text("isso, na maioria das vezes, s??o instalados j?? com a placa-m??e dentro ", 19,x_text, self.y_text + 20)
            self.game.draw_text("do gabinete.", 19,x_text, self.y_text + 40)
        if layer == 36:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Por exemplo, a eeprom, sigla para Electrically Erasable Programmable ", 19,243, self.y_text)
            self.game.draw_text("Read-Only Memory, pode ser apagada ou alterada por meio de descarga ", 19, 243,self.y_text + 20)
            self.game.draw_text("el??trica.", 19, 243,self.y_text + 40)
        if layer == 37:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A mem??ria flash possui o mesmo m??todo da eeprom, por??m, se diferencia ", 19, 139, self.y_text)
            self.game.draw_text("na maior velocidade e menor custo.", 19, 139, self.y_text + 20)
            self.game.draw_text("A ROM mais conhecida e mais utilizada ?? a BIOS e como foi dito nas fases", 19, 139, self.y_text + 40)
            self.game.draw_text("anteriores, o software presente nessa mem??ria ?? chamado de firmware.", 19, 139, self.y_text + 60)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos.", 19, 139, self.y_text + 80)
        if layer == 38:
            #FAZER JOGO
            pass
        if layer == 39:
            self.draw_very_good()
        if layer == 40:
        #FAZER MECANICA JOGO    
            pass
        if layer == 41:
            self.draw_very_good()
        if layer == 42:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora voc?? vai ver outro tipo de mem??ria n??o vol??til, a presente no disco r??gido.", 19, x_text,self.y_text)
            self.game.draw_text("O disco r??gido, tamb??m chamado de HD, ?? o hardware respons??vel pelo ", 19, x_text,self.y_text + 20)
            self.game.draw_text("armazenamento dos dados a longo prazo como os softwares (programas e SO) e as ", 19, x_text,self.y_text + 40)
            self.game.draw_text("informa????es salvas dos usu??rios.", 19, x_text,self.y_text + 60)
        if layer == 43:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Uma outra fun????o do HD se refere ?? transmiss??o de seus dados para", 19, x_text,self.y_text)
            self.game.draw_text("processamento. Normalmente, o HD utiliza a RAM como ponte de transfer??ncia ", 19, x_text,self.y_text + 20)
            self.game.draw_text("de informa????o, mas  ?? poss??vel emular essa RAM no HD, aumentando a ", 19, x_text,self.y_text + 40)
            self.game.draw_text("capacidade total de RAM.", 19, x_text,self.y_text + 60)
        if layer == 44:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A capacidade de armazenamento de dados do HD ?? medida em Gigabytes e ", 19, x_text, self.y_text)
            self.game.draw_text("Terabytes. J?? a sua velocidade de transfer??ncia ?? medida em MB/s.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Os HDs mais comuns no mercado s??o os de capacidade acima de 500 GB at?? ", 19, x_text,self.y_text + 40)
            self.game.draw_text("2 TB.", 19, x_text,self.y_text + 60)
        if layer == 45:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O funcionamento do HD ?? mec??nico. Ele consiste no uso de um  ", 19, 275, self.y_text)
            self.game.draw_text("disco interno capaz de girar em torno de si, pr??ximo a uma bobina  ", 19, 275, self.y_text + 20)
            self.game.draw_text("em forma de pin??a que propaga impulsos magn??ticos no disco.", 19, 275, self.y_text + 40)
            self.game.draw_text("Esses impulsos interagem com o disco gravando dados. ", 19, 275, self.y_text + 60)
        if layer == 46:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("?? importante saber que a bobina n??o encosta no ", 19, x_text, self.y_text)
            self.game.draw_text("disco.  Caso isso ocorra, principalmente se o HD estiver ligado,", 19, x_text, self.y_text + 20)
            self.game.draw_text("pode causar s??rios danos como travamentos, perda de ", 19, x_text, self.y_text + 40)
            self.game.draw_text("arquivos ou o n??o funcionamento completo do HD.", 19, x_text, self.y_text + 60)
        if layer == 47:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Por isso ?? recomendado ter cuidado ao manusear o HD enquanto estiver ", 19, x_text, self.y_text)
            self.game.draw_text("em uso, pois qualquer choque pode causar s??rios problemas.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Esse problema ocorre com mais frequ??ncia com notebook, pois, devido ", 19, x_text, self.y_text + 40)
            self.game.draw_text("?? sua portabilidade, tamb??m s??o mais pass??veis de quedas e choques.", 19, x_text, self.y_text + 60)
        if layer == 48:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Outra caracter??stica interessante a ser notada ?? que, como ", 19, 255, self.y_text)
            self.game.draw_text("a grava????o ocorre por impulsos magn??ticos, o uso de ??m??s  ", 19, 255, self.y_text + 20)
            self.game.draw_text("pr??ximos ao HD tamb??m pode causar danos, mas isso ocorre ", 19, 255, self.y_text + 40)
            self.game.draw_text("apenas com ??m??s fortes se o HD estiver desligado. Isso ", 19, 255, self.y_text + 60)
            self.game.draw_text("ocorre  porque os ??m??s desestabilizam o campo magn??tico do", 19, 255, self.y_text + 80)
            self.game.draw_text("disco, podendo apagar as informa????es.", 19, 255, self.y_text + 100)
        if layer == 49:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ent??o, por motivos de seguran??a, nunca deixe um HD pr??ximo a um im??.", 19, x_text, self.y_text)
            self.game.draw_text("Outra parte importante do HD ?? o conector de energia, que fornece ", 19, x_text, self.y_text + 20)
            self.game.draw_text("energia para o hardware, e o conector de transfer??ncia de dados. ", 19, x_text, self.y_text + 40)
            self.game.draw_text("Antigamente, utilizava-se o padr??o IDE, por??m, os HDs de hoje possuem ", 19, x_text, self.y_text + 60)
            self.game.draw_text("o conector que permite uma transfer??ncia de dados mais r??pida, o SATA.", 19, x_text, self.y_text + 80)
        if layer == 50:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("?? importante saber que existem dois conectores SATA no HD. Um para se conectar ", 19, x_text, self.y_text)
            self.game.draw_text("?? fonte, que ?? o que foi visto nas fases anteriores, e outro para se conectar ?? ", 19, x_text, self.y_text + 20)
            self.game.draw_text("placa-m??e. Este  ?? mais simples de se identificar, pois ?? o menor conector SATA.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Para conectar o HD ?? placa-m??e basta pegar um cabo SATA e conect??-lo na entrada ", 19, x_text, self.y_text + 60)
            self.game.draw_text("SATA (em forma de L) da placa m??e. Geralmente a placa-m??e possui mais ", 19, x_text, self.y_text + 80)
            self.game.draw_text("de um conector SATA.", 19, x_text, self.y_text + 100)
        if layer == 51:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Existem tr??s tipos de conectores SATA, o SATA I, SATA II e ", 19, 275, self.y_text)
            self.game.draw_text("SATA III. A diferen??a entre eles ?? a maior velocidade de ", 19, 275, self.y_text + 20)
            self.game.draw_text("transmiss??o do primeiro ao terceiro. O padr??o atual ?? o ", 19, 275, self.y_text + 40)
            self.game.draw_text("SATA III. Sua velocidade de transmiss??o chega a 600 MB/s", 19, 275, self.y_text + 60)
            self.game.draw_text("Recentemente esse padr??o tamb??m est?? sendo substitu??do ", 19, 275, self.y_text + 80)
            self.game.draw_text("por outro que voc?? ver?? daqui a pouco.", 19, 275, self.y_text + 100)
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
            #FAZER JOGO
            pass
        if layer == 59:
            self.draw_very_good()
        if layer == 60:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A vida ??til de um HD ?? de, em m??dia, 6 anos. Ent??o, para preservar os dados ", 19, x_text, self.y_text)
            self.game.draw_text("contidos nele deve ser feita uma c??pia de seguran??a chamada de ", 19, x_text,self.y_text + 20)
            self.game.draw_text("backup de dados. Ela geralmente ?? feita pela transfer??ncia dos dados de", 19, x_text,self.y_text + 40)
            self.game.draw_text("um HD para outro dispositivo de armazenamento, mas tamb??m h?? uma t??cnica", 19, x_text,self.y_text + 60)
            self.game.draw_text("de arranjo de discos independentes que consiste em duplicar a informa????o", 19, x_text,self.y_text + 80)
            self.game.draw_text("em um HD, caso haja problema, em outro HD. Essa t??cnica ?? chamada de RAID.", 19, x_text,self.y_text + 100)
        if layer == 61:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O RAID, al??m de desempenhar uma maior disponibilidade de dados, ", 19, x_text, self.y_text)
            self.game.draw_text("proporciona maior desempenho. Apesar de convencional, n??o ?? uma ", 19, x_text, self.y_text + 20)
            self.game.draw_text("tecnica muito utilizada pelos leigos, pois pode causar uma total ", 19, x_text, self.y_text + 40)
            self.game.draw_text("perda de dados, ent??o pense bem antes de recomendar ou realizar", 19, x_text, self.y_text + 60)
            self.game.draw_text("essa pr??tica.", 19, x_text, self.y_text + 80)
        if layer == 62:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O RAID pode ser classificado em diversos n??veis, como o N??vel 0, em que os discos", 19, x_text, self.y_text)
            self.game.draw_text("se comportam como se fossem apenas um devido ao particionamento de dados. ", 19, x_text, self.y_text + 20)
            self.game.draw_text("Como esse n??vel, a capacidade de armazenamento e a taxa de transfer??ncia de  ", 19, x_text, self.y_text + 40)
            self.game.draw_text("dados aumentam, por??m, caso um HD falhe, todos os discos ficam comprometidos.", 19, x_text, self.y_text + 60)
        if layer == 63:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Existem outros como o n??vel 1, que pode ser compreendido como ", 19, x_text, self.y_text)
            self.game.draw_text("o RAID propriamente dito, pois os discos s??o utilizados para ", 19, x_text, self.y_text + 20)
            self.game.draw_text("fornecer redund??ncia dos dados e o n??vel 5, que funciona como o", 19, x_text, self.y_text + 40)
            self.game.draw_text("RAID n??vel 0, mas com a possibilidade de recupera????o de informa????o ", 19, x_text, self.y_text + 60)
            self.game.draw_text("mesmo com a falha de um HD.", 19, x_text, self.y_text + 80)
        if layer == 64:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Essa t??cnica ?? mais utilizada em servidores e bancos de dados, mas tamb??m ", 19, x_text, self.y_text)
            self.game.draw_text("pode ser utilizada para computadores pessoais.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos.", 19, x_text, self.y_text + 80)
        if layer == 65:
            #FAZER JOGO
            pass
        if layer == 66:
            self.draw_very_good()
        if layer == 67:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora voc?? vai ver como fazer o processo de RAID 0.", 19,x_text, self.y_text)
            self.game.draw_text("Foi escolhido o n??vel 0 por se tratar do mais comum e mais simples.", 19,x_text, self.y_text + 20)
            self.game.draw_text("?? importante saber que essa pr??tica ?? permitida em determinados tipos ", 19,x_text, self.y_text + 40)
            self.game.draw_text("de placas-m??e (geralmente as mais recentes), ent??o ?? bom ler o manual ", 19,x_text, self.y_text + 60)
            self.game.draw_text("dela, principalmente a respeito do modo de inicializa????o. O modo ", 19,x_text, self.y_text + 80)
            self.game.draw_text("de ativa????o da RAID tamb??m depende da BIOS instalada na placa-m??e.", 19,x_text, self.y_text + 100)
        if layer == 68:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Inicialmente, deve-se conectar os HDs (preferencialmente com a mesma ", 19,x_text, self.y_text)
            self.game.draw_text("capacidade de armazenamento e padr??o de conex??o e sem nenhum arquivo, ", 19,x_text, self.y_text + 20)
            self.game.draw_text("pois ser?? formatado no final do processo) nas entradas SATA da placa", 19,x_text, self.y_text + 40)
            self.game.draw_text("-m??e. Como dito anteriormente, dependendo da placa-m??e pode haver uma", 19,x_text, self.y_text + 60)
            self.game.draw_text("ordem espec??fica de conectores. Depois da conex??o dos cabos de energia e ", 19,x_text, self.y_text + 80)
            self.game.draw_text("transfer??ncia de dados, deve-se ligar o computador e abrir o setup da BIOS.", 19,x_text, self.y_text + 100)
        if layer == 69:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Para fazer isso, durante a inicializa????o, deve-se pressionar uma", 19, 255, self.y_text)
            self.game.draw_text("tecla espec??fica do teclado at?? aparecer o setup. Geralmente essa ", 19, 255, self.y_text + 20)
            self.game.draw_text("tecla ?? o delete, F12, Esc, F2, entre outras (?? preciso consultar ", 19, 255,self.y_text + 40)
            self.game.draw_text("o manual da placa-m??e).", 19, 255,self.y_text + 60)
        if layer == 70:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ap??s aparecer o setup da BIOS, v?? at?? a op????o de sele????o de modo ", 19, x_text, self.y_text)
            self.game.draw_text("de SATA (geralmente est?? no menu chipset).", 19, x_text, self.y_text + 20)
            self.game.draw_text("Depois, nessa op????o de configura????o SATA (configuration SATA em ", 19, x_text,self.y_text + 40)
            self.game.draw_text("ingl??s), mude a op????o padr??o, geralmente AHCI, sigla para ", 19, x_text,self.y_text + 60)
            self.game.draw_text("Advanced Host Controller Interface, para a op????o", 19, x_text,self.y_text + 80)
            self.game.draw_text("RAID. Depois, salve e saia do setup.", 19, x_text,self.y_text + 100)
        if layer == 71:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Enquanto o computador estiver refazendo o boot, pressione as teclas ", 19, x_text, self.y_text)
            self.game.draw_text("???ctrl??? e ???i??? do teclado para aparecer a tela de configura????o de RAID.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Selecione a op????o de cria????o de volume RAID (create volume RAID em ", 19, x_text,self.y_text + 40)
            self.game.draw_text("ingl??s). Ap??s aparecer a janela de cria????o, adicione um nome ao novo ", 19, x_text,self.y_text + 60)
            self.game.draw_text("volume e selecione o tamanho da tira (strip size) adequado para o ", 19, x_text,self.y_text + 80)
            self.game.draw_text("RAID 0. Essa informa????o ser?? mostrada na aba de ajuda.", 19, x_text,self.y_text + 100)
        if layer == 72:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Depois, coloque a capacidade de armazenamento como a m??xima dos  ", 19, 255, self.y_text)
            self.game.draw_text("HDs juntos (j?? ?? a op????o padr??o).", 19, 255, self.y_text + 20)
            self.game.draw_text("Por fim, selecione a op????o de criar volume (create volume).", 19, 255,self.y_text + 40)
        if layer == 73:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Aparecer?? uma mensagem de aviso de que os dados ser??o", 19, x_text, self.y_text)
            self.game.draw_text("apagados. Basta clicar em sim (yes).", 19, x_text, self.y_text + 20)
            self.game.draw_text("Quando voltar para a tela inicial de configura????o de RAID,", 19, x_text, self.y_text + 40)
            self.game.draw_text("selecione sair (exit).", 19, x_text, self.y_text + 60)
        if layer == 74:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para testar se o RAID foi feito com ??xito, acesse o setup da BIOS ", 19, x_text, self.y_text)
            self.game.draw_text("novamente e v?? nas op????es de boot. Caso haja uma op????o com o nome ", 19, x_text, self.y_text + 20)
            self.game.draw_text("do volume novo, tudo foi feito corretamente. Por fim, selecione ", 19, x_text, self.y_text + 40)
            self.game.draw_text("essa op????o e salve as configura????es.", 19, x_text, self.y_text + 60)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos.", 19, x_text, self.y_text + 80)
        if layer == 75:
            #FAZER JOGO.
            pass
        if layer == 76:
            self.draw_very_good()
        if layer == 77:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora voc?? vai ver o dispositivo de armazenamento mais recente que ", 19, x_text, self.y_text)
            self.game.draw_text("provavelmente substituir?? completamente os HDs, o SSD.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Os SSD, sigla para solid state drive, s??o unidades de armazenamento ", 19, x_text, self.y_text + 40)
            self.game.draw_text("que utilizam c??lulas de mem??rias flash. Ele se difere do HD por n??o ", 19, x_text, self.y_text + 60)
            self.game.draw_text("ser mec??nico, o modo de armazenamento de dados funciona a partir de ", 19, x_text, self.y_text + 80)
            self.game.draw_text("um fen??meno chamado tunelamento qu??ntico.", 19, x_text, self.y_text + 100)
        if layer == 78:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Dentre as melhorias do SSD em rela????o ao HD podemos constatar a ", 19, 255, self.y_text)
            self.game.draw_text("aus??ncia de vibra????es, uma vez que sua constru????o e funcionamento ", 19, 255, self.y_text + 20)
            self.game.draw_text("n??o ?? mec??nica, o que elimina tamb??m os ru??dos e o risco de mal ", 19, 255, self.y_text + 40)
            self.game.draw_text("funcionamento por choques f??sicos, al??m de uma menor massa e um ", 19, 255, self.y_text + 60)
            self.game.draw_text("consumo reduzido de energia.", 19, 255, self.y_text + 80)
        if layer == 79:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Quanto ?? velocidade de transfer??ncia de dados, essa ?? a principal ", 19, 255, self.y_text)
            self.game.draw_text("evolu????o. Enquanto um HD possui uma velocidade de leitura e  ", 19, 255, self.y_text + 20)
            self.game.draw_text("escrita de at?? 200 MB/s, o SSD de padr??o SATA possui uma velocidade ", 19, 255, self.y_text + 40)
            self.game.draw_text("de mais de 500 MB/s.", 19, 255, self.y_text + 60)
        if layer == 80:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Mas o SSD ainda possui algumas desvantagens em rela????o ao HD, como ", 19, x_text, self.y_text)
            self.game.draw_text("o alto custo e caso ele pare de funcionar, n??o h?? nenhuma chance de", 19, x_text, self.y_text + 20)
            self.game.draw_text("recuperar os dados, diferente do HD, que ainda que esteja em mau ", 19, x_text, self.y_text + 40)
            self.game.draw_text("funcionamento, ?? poss??vel realizar uma recupera????o.", 19, x_text, self.y_text + 60)
        if layer == 81:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Essas vantagens ditas do SSD foram para o padr??o SATA, id??ntico  ", 19, 250, self.y_text)
            self.game.draw_text("ao do HD (ambos possuem o mesmo modo de instala????o), mas j?? ", 19, 250, self.y_text + 20)
            self.game.draw_text("existe uma melhoria para a tecnologia dos SSDs, que ?? a da ", 19, 250, self.y_text + 40)
            self.game.draw_text("mudan??a do padr??o de entrada.", 19, 250, self.y_text + 60)
        if layer == 82:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O novo padr??o de entrada para SSDs ?? o M.2. Esse padr??o possui v??rios protocolos ", 19, x_text, self.y_text)
            self.game.draw_text("distintos. Os mais comuns s??o o protocolo do padr??o SATA e o do padr??o NVME,  ", 19, x_text, self.y_text + 20)
            self.game.draw_text("sigla para Non-Volatile Memory Express. O padr??o M.2 SATA possui uma velocidade ", 19, x_text, self.y_text + 40)
            self.game.draw_text("de transfer??ncia muito maior que a do SSD de padr??o SATA III, podendo chegar a  ", 19, x_text, self.y_text + 60)
            self.game.draw_text("mais de 1300 MB/s, o que ?? quase tr??s vezes mais do que o ", 19, x_text, self.y_text + 80)
            self.game.draw_text("m??ximo de um SSD SATA III.", 19, x_text, self.y_text + 100)
        if layer == 83:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("J?? o padr??o M.2 NVME possui um protocolo com capacidades de transfer??ncia", 19, x_text, self.y_text)
            self.game.draw_text("id??nticas ao PCI Express da placa-m??e, com modelos atuais chegando a uma", 19, x_text, self.y_text + 20)
            self.game.draw_text("velocidade de transfer??ncia de mais de 3400 MB/s, quase 6 vezes mais do ", 19, x_text, self.y_text + 40)
            self.game.draw_text("que o m??ximo de SSD SATA III.", 19, x_text, self.y_text + 60)
        if layer == 84:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Al??m da diferen??a de velocidade, esse novo padr??o se diferencia pelo tamanho ", 19, x_text, self.y_text)
            self.game.draw_text("do hardware, sendo bem menor do que o SSD SATA III.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Agora voc?? vai ver como instalar um SSD M.2.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Por se tratar de um padr??o novo de conex??o, ele s?? estar?? presente em ", 19, x_text, self.y_text + 60)
            self.game.draw_text("placas-m??e recentes.", 19, x_text, self.y_text + 80)
        if layer == 85:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para conectar um SSD M.2, posicione-o no sentido em que possa ver ", 19, x_text, self.y_text)
            self.game.draw_text("os chips dele e insira a parte dos ???dentes??? no conector. De in??cio,", 19, x_text, self.y_text + 20)
            self.game.draw_text("ele ficar?? um pouco elevado, mas basta pression??-lo para o sentido", 19, x_text, self.y_text + 40)
            self.game.draw_text("da placa-m??e e parafus??-lo com uma chave.", 19, x_text, self.y_text + 60)
            self.game.draw_text("Pronto! A instala????o ?? bem r??pida.", 19, x_text, self.y_text + 80)
        if layer == 86:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Outra caracter??stica interessante dos SSDs ?? que eles tamb??m podem ", 19, x_text, self.y_text)
            self.game.draw_text("ser usados em RAID, mas fique atento quanto a isto: um SSD s?? pode ", 19, x_text, self.y_text + 20)
            self.game.draw_text("fazer RAID com outro SSD e um HD s?? pode fazer RAID com outro HD. ", 19, x_text, self.y_text + 40)
            self.game.draw_text("A tentativa mista pode causar s??rios problemas como a perda de ambos.", 19, x_text, self.y_text + 60)
        if layer == 87:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O SSD M.2 NVME possui uma configura????o diferente, pois n??o utiliza ", 19, 255, self.y_text)
            self.game.draw_text("o padr??o SATA, ent??o o processo de RAID pelo setup da BIOS ?? ", 19, 255, self.y_text + 20)
            self.game.draw_text("diferente. Vamos testar seus conhecimentos adquiridos.", 19, 255, self.y_text + 80)
        if layer == 88:
            #FAZER QUEST??O  
            pass
        if layer == 89:
            self.draw_very_good()
        if layer == 90:
            #FAZER QUEST??O  
            pass
        if layer == 91:
            self.draw_very_good()
        if layer == 92:
            #FAZER QUEST??O  
            pass
        if layer == 93:
           self.draw_very_good()
        if layer == 94:
            #FAZER QUEST??O  
            pass
        if layer == 95:
           self.draw_very_good()
        if layer == 96:
           #FAZER QUEST??O  
            pass
        if layer == 97:
           self.draw_very_good()    
        if layer == 98:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s4/end.png'), (0, 0))
            text = 'FasesWone='
            a = open('c:\ProtTech\data\data.txt', 'r')
            b = a.read()
            a2 = open('c:\ProtTech\data\data.txt', 'rt+')
            s = a2.readlines()[2]
            a2.close()
            if (text + "True,True,True,True,False") in s:
                b = b.replace(text + "True,True,True,True,False", text + "True,True,True,True,True", 1)
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
            
