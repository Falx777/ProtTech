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
        self.i = 90
        self.layers = [90]
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
            self.game.draw_text("Você vai aprender agora um pouco sobre os outros hardwares", self.font_size, x_text, self.y_text)
        if layer == 2:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("As memórias no computador são dispositivos que podem armazenar ", self.font_size, x_text, self.y_text)
            self.game.draw_text("dados de maneira temporária ou permanente. A partir disso elas ", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("são classificadas em memórias voláteis e não voláteis.", self.font_size, x_text, self.y_text + 40)
        if layer == 3:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Uma memória volátil armazena dados apenas na presença de energia. ", self.font_size, 125, 360)
            self.game.draw_text("Caso a não haja energia, toda a informação contida nela é perdida ", self.font_size, 125, 415)
            self.game.draw_text("e por isso seu armazenamento é temporário. Alguns tipos de  ", self.font_size, 125, 435)
            self.game.draw_text("memórias voláteis são a RAM e a memória cache.", self.font_size, 125, 455)
        if layer == 4:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Uma memória não volátil não perde os dados escritos na ausência de ", self.font_size, x_text, self.y_text)
            self.game.draw_text("energia, por isso que a informação contida nela é duradoura. Alguns", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("tipos de memórias não voláteis são as memórias flash, ROM,", self.font_size, x_text, self.y_text + 40)
            self.game.draw_text("a unidade de estado sólido e o disco rígido.", self.font_size, x_text, self.y_text + 60)
            self.game.draw_text("Vamos começar com a memória RAM.", self.font_size, x_text, self.y_text + 80)
        if layer == 5:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A RAM, sigla cuja tradução consiste em memória de acesso randômico, ",self.font_size, x_text, self.y_text)
            self.game.draw_text("é uma memória volátil importante para o processamento das ", self.font_size,x_text, self.y_text + 20)
            self.game.draw_text("informações, por isso ela é classificada também como memória", self.font_size,x_text, self.y_text + 40)
            self.game.draw_text("primeira.", self.font_size,x_text, self.y_text + 60)
        if layer == 6:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O acesso randômico faz referência aos modo como transistores", self.font_size,251, self.y_text)
            self.game.draw_text("e capacitores são utilizados para referenciar bits 0 e 1, sendo ", self.font_size,251, self.y_text + 20)
            self.game.draw_text("que são selecionados aleatoriamente enquanto houver corrente", self.font_size,251, self.y_text + 40)
            self.game.draw_text("passando por eles.", self.font_size,251, self.y_text + 60)
        if layer == 7:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ao iniciar o computador, as informações que o processador necessita", 20, x_text, self.y_text)
            self.game.draw_text("para serem usadas em um curto período de tempo e são muito grandes ", 20, x_text,self.y_text + 20)
            self.game.draw_text("erem armazenadas na memória cache ficam armazenadas na RAM. ", 20, x_text, self.y_text + 40)
        if layer == 8:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Inicialmente, as informações de inicialização ficam armazenadas nas", 20, x_text, self.y_text)
            self.game.draw_text("memórias não voláteis e são transmitidas para a RAM, que por sua vez ", 20, x_text,self.y_text + 20)
            self.game.draw_text("as transmite para o processador.", 20, x_text, self.y_text + 40)
            self.game.draw_text("O processador é quem recorre ao acesso da RAM, fazendo uma cópia dos", 20, x_text, self.y_text + 60)
            self.game.draw_text("dados necessários para a memória cache caso haja um uso desses dados", 20, x_text, self.y_text + 80)
            self.game.draw_text("algum tempo depois.", 20, x_text, self.y_text + 100)
        if layer == 9:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Você deve estar pensando: por que o processador não acessa", 20, 250, self.y_text)
            self.game.draw_text("as informações diretamente da memória não volátil?", 20, 250,self.y_text + 20)
        if layer == 10:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Atualmente, isso ocorre devido ao tempo de transferência de dados. Para ", 19, x_text, self.y_text)
            self.game.draw_text("você perceber a diferença, dependendo do processador e da memória não volátil,", 19, x_text, self.y_text + 20)
            self.game.draw_text("a velocidade de acesso em comparação com a RAM é 60 mil vezes mais lenta, ou ", 19, x_text, self.y_text + 40)
            self.game.draw_text("seja, não vale a pena.", 19, x_text, self.y_text + 60)
        if layer == 11:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Agora veja um exemplo de funcionamento da trajetória de uma informação ao ", 19,x_text, self.y_text)
            self.game.draw_text("executar um programa:", 19, x_text, self.y_text + 20)
            self.game.draw_text("...abrindo um programa.", 19, x_text,self.y_text + 40)
            self.game.draw_text("HD -> RAM -> CPU.", 19, x_text,self.y_text + 60)
            self.game.draw_text("Note que enquanto o programa estiver rodando no computador, ele estará ", 19, x_text,self.y_text + 80)
            self.game.draw_text("tomando espaço na RAM.", 19, x_text,self.y_text + 100)
        if layer == 12:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Uma fonte nominal ainda possui o risco de queimar os ", 21, 239,self.y_text)
            self.game.draw_text("componentes ligados a ela caso haja algum problema, podendo ", 21, 239,self.y_text + 20)
            self.game.draw_text("ser um iniciador de incêndio.", 21, 239, self.y_text + 40)
            self.game.draw_text("Agora você vai ver como conectar uma fonte na placa-mãe e nos", 21, 239, self.y_text + 60)
            self.game.draw_text("outros componentes.", 21, 239, self.y_text + 80)
        if layer == 13:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Durante a evolução do hardware de memória de acesso remoto houveram", 21, x_text, self.y_text)
            self.game.draw_text("diversos padrões de tecnologias com cada uma ditando a capacidade", 21, x_text, self.y_text + 20)
            self.game.draw_text("máxima da RAM. Alguns dos padrões de memória são simm, dimm, ddr3 ", 21, x_text, self.y_text + 40)
            self.game.draw_text("sdram e ddr4 sdram.", 21, x_text, self.y_text + 60)
        if layer == 14:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O padrão mais antigo e não mais utilizado é o simm, sigla para Single", 21, x_text, self.y_text)
            self.game.draw_text("In-Line Memory Module. O substituto para o simm foi o dimm, sigla", 21, x_text, self.y_text + 20)
            self.game.draw_text("para Dual Inline Memory Module, que possuía o dobro da capacidade e", 21, x_text, self.y_text + 40)
            self.game.draw_text("taxa de transmissão.", 21, x_text, self.y_text + 60)
        if layer == 15:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O padrão DDR, sigla para Double-Data-Rate introduziu a técnica ", self.font_size, 249, self.y_text)
            self.game.draw_text("de duplicação de taxa de transferência, fazendo com que a ", self.font_size, 249, self.y_text + 20)
            self.game.draw_text("capacidade de transmissão aumentasse mais uma vez e assim ", self.font_size, 249, self.y_text + 40)
            self.game.draw_text("ocorreu para os consecutivos Padrões DDR.", self.font_size, 249, self.y_text + 60)
        if layer == 16:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os padrões mais comuns, atualmente, de RAM são os DDR3 e DDR4.", 20, x_text, self.y_text)
            self.game.draw_text("O padrão DDR3 permite a criação de memórias com frequência de 800 MHz até ", 20, x_text, self.y_text + 20)
            self.game.draw_text("2400 MHz e possui uma capacidade de armazenamento de até 8 GB por slot. ", 20, x_text, self.y_text + 40)
            self.game.draw_text("Algumas placas-mãe possuem até mais de 4 slots de RAM, então pode-se ", 20, x_text, self.y_text + 60)
            self.game.draw_text("aumentar a capacidade mesmo com a limitação de 8 GB por slot.", 20, x_text, self.y_text + 80)
        if layer == 17:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O padrão DDR4 é o mais recente. Ele permite a criação de memórias com", 21, x_text, self.y_text)
            self.game.draw_text("frequência de 2.133 até 4.266 MHz e possui uma capacidade de ", 21, x_text, self.y_text + 20)
            self.game.draw_text("armazenamento de até 16 GB por slot.", 21, x_text, self.y_text + 40)
        if layer == 18:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("A mesma característica da placa-mãe DDR3 vale para a DDR4, porém,", 19, 249,self.y_text)
            self.game.draw_text("não é possível utilizar uma memória de um padrão em um slot de outro. ", 19, 249,self.y_text + 20)
            self.game.draw_text("Além do encaixe não ser possível, há o risco de perda ou excesso de ", 19, 249,self.y_text + 40)
            self.game.draw_text("energia, pois a memória DDR3 (1.5V) requer uma tensão maior do que a ", 19, 249,self.y_text + 60)
            self.game.draw_text("DDR4 (1.2V). Por isso que as placas-mãe precisam ser ", 19, 249,self.y_text + 80)
            self.game.draw_text("compatíveis com o tipo de memória.", 19, 249,self.y_text + 100)
        if layer == 19:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Sobre as marcas, devido à relativa simplicidade de criação da memória de ", 19,x_text, self.y_text)
            self.game.draw_text("acesso randômico, há uma quantidade de empresas muito maior do que as de ", 19,x_text, self.y_text + 20)
            self.game.draw_text("processadores.", 19,x_text, self.y_text + 40)
        if layer == 20:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A nomenclatura de uma memória DDR é a seguinte: DDR() []/PC() {} ", 19, x_text,self.y_text )
            self.game.draw_text("O parêntesis indica o tipo de DDR (2, 3, 4 ou 5).", 19, x_text,self.y_text + 20)
            self.game.draw_text("O colchete indica o clock máximo da memória.", 19, x_text,self.y_text + 40)
            self.game.draw_text("A chave indica a velocidade máxima de transferência de dados, medida em mb/s.", 19, x_text,self.y_text + 60)
            self.game.draw_text("A diferença entre frequência e velocidade de transferência é que a", 19, x_text,self.y_text + 80)
            self.game.draw_text("transferência de dados é feita a cada determinada quantidade de ciclos.", 19, x_text,self.y_text + 100)
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
            self.game.draw_text("Outras características que podemos ver sobre a RAM é que a sua ", 21, x_text,self.y_text)
            self.game.draw_text("frequência máxima é premeditada pelo processador instalado.", 21, x_text,self.y_text + 20)
            self.game.draw_text("Processadores da Intel da 6ª e 7ª geração, por exemplo, permitem uma", 21, x_text,self.y_text + 40)
            self.game.draw_text("frequência máxima de memória de 2.400 MHz, mesmo se a memória for", 21, x_text,self.y_text + 60)
            self.game.draw_text("de 3.200 MHz.", 21, x_text,self.y_text + 80)
        if layer == 24:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Uma parte maior dos processadores da AMD já possuem uma liberação", 19, 247,self.y_text)
            self.game.draw_text("de frequência mais alta do que os da Intel.", 19, 247,self.y_text + 20)
        if layer == 25:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Além disso, ao utilizar mais de uma memória, o recomendado é que ", 21, x_text,self.y_text)
            self.game.draw_text("tenham a mesma frequência, independente da marca, pois com", 21, x_text,self.y_text + 20)
            self.game.draw_text("frequências diferentes, o processador precisa acessá-las de uma ", 21, x_text,self.y_text + 40)
            self.game.draw_text("mesma maneira, então ele vai igualar a frequência da RAM baseando-", 21, x_text,self.y_text + 60)
            self.game.draw_text("-se na menor frequência, ou seja, ocorre uma perda de velocidade.", 21, x_text,self.y_text + 80)
        if layer == 26:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Um canal de memória apenas pode não ser suficiente para acompanhar ", 21, x_text, self.y_text)
            self.game.draw_text("a velocidade dos processadores. A partir disso surgiu a prática", 21, x_text, self.y_text + 20)
            self.game.draw_text("de dual-channel, que nada mais é do que utilizar memórias em", 21, x_text, self.y_text + 40)
            self.game.draw_text("uma configuração que dobre a capacidade de transferência e leitura", 21, x_text, self.y_text + 60)
            self.game.draw_text("de informações para o processador.", 21, x_text, self.y_text + 80)
        if layer == 27:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Esse tipo de configuração depende da especificação da placa-", 20, 247,self.y_text)
            self.game.draw_text("-mãe do processador. Atualmente, ele é tão comum que já está ", 20, 247,self.y_text + 20)
            self.game.draw_text("presente na maioria dos computadores. A recomendação para", 20, 247,self.y_text + 40)
            self.game.draw_text("o uso do dual-channel é que se utilize pentes de memórias com ", 20, 247,self.y_text + 60)
            self.game.draw_text("a mesma capacidade de armazenamento e frequência e que ", 20, 247,self.y_text + 80)
            self.game.draw_text("seja mais de um pente e em número par de quantidade.", 20, 247,self.y_text + 100)
        if layer == 28:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Perceba que se utilizar apenas um pente de RAM DDR4 de 8 GB e dois pentes de ", 19, x_text, self.y_text)
            self.game.draw_text("RAM DDR4 de 4 GB cada, a segunda opção acaba sendo mais rápida do que a", 19, x_text, self.y_text + 20)
            self.game.draw_text("rimeira, mesmo com a mesma capacidade.", 19, x_text, self.y_text + 40)
            self.game.draw_text("O modo de como as RAMs foram instaladas por você durante a prática anterior", 19, x_text, self.y_text + 60)
            self.game.draw_text("é em dual-channel.", 19, x_text, self.y_text + 80)
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
            self.game.draw_text("A ROM, sigla para Ready-Only Memory, é uma memória não volátil.", 19, x_text, self.y_text)
            self.game.draw_text("Ela armazena uma informação feita pelo fabricante uma única", 19, x_text, self.y_text + 20)
            self.game.draw_text("vez e que, depois disso, só pode ser lida, ou seja, não é possível", 19, x_text, self.y_text + 40)
            self.game.draw_text("alterar ou remover a informação. Daí o seu nome: memória somente de", 19, x_text, self.y_text + 60)
            self.game.draw_text("leitura.", 19, x_text, self.y_text + 80)
        if layer == 32:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O termo ROM é utilizado para identificar vários tipos de memória, como a ", 19, x_text, self.y_text)
            self.game.draw_text("memória prom, eprom, eeprom e memória flash.", 19, x_text, self.y_text + 20)
        if layer == 33:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("A memória prom, sigla para Programmable Read-Only Memory, é ", 19, 243, self.y_text)
            self.game.draw_text("utilizada para programar informações de dispositivos especiais e ", 19, 243, self.y_text + 20)
            self.game.draw_text("armazená-las nessa memória para depois ser utilizada apenas como ", 19, 243, self.y_text + 40)
            self.game.draw_text("leitura.", 19, 243, self.y_text + 60)
        if layer == 34:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A eprom, sigla para Erasable Programmable Read-Only Memory, é um tipo de ", 19, x_text, self.y_text)
            self.game.draw_text("memória cujos dados podem ser apagados por meio de radiação ultravioleta.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Apenas com isso é possível reutilizá-la.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Há ainda outras formas de apagar as informações da ROM, depende do seu tipo.", 19, x_text, self.y_text + 60)
        if layer == 35:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os hardwares instalados no PCI-E possuem entradas externas e por", 19, x_text, self.y_text)
            self.game.draw_text("isso, na maioria das vezes, são instalados já com a placa-mãe dentro ", 19,x_text, self.y_text + 20)
            self.game.draw_text("do gabinete.", 19,x_text, self.y_text + 40)
        if layer == 36:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Por exemplo, a eeprom, sigla para Electrically Erasable Programmable ", 19,243, self.y_text)
            self.game.draw_text("Read-Only Memory, pode ser apagada ou alterada por meio de descarga ", 19, 243,self.y_text + 20)
            self.game.draw_text("elétrica.", 19, 243,self.y_text + 40)
        if layer == 37:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A memória flash possui o mesmo método da eeprom, porém, se diferencia ", 19, 139, self.y_text)
            self.game.draw_text("na maior velocidade e menor custo.", 19, 139, self.y_text + 20)
            self.game.draw_text("A ROM mais conhecida e mais utilizada é a BIOS e como foi dito nas fases", 19, 139, self.y_text + 40)
            self.game.draw_text("anteriores, o software presente nessa memória é chamado de firmware.", 19, 139, self.y_text + 60)
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
            self.game.draw_text("Agora você vai ver outro tipo de memória não volátil, a presente no disco rígido.", 19, x_text,self.y_text)
            self.game.draw_text("O disco rígido, também chamado de HD, é o hardware responsável pelo ", 19, x_text,self.y_text + 20)
            self.game.draw_text("armazenamento dos dados a longo prazo como os softwares (programas e SO) e as ", 19, x_text,self.y_text + 40)
            self.game.draw_text("informações salvas dos usuários.", 19, x_text,self.y_text + 60)
        if layer == 43:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Uma outra função do HD se refere à transmissão de seus dados para", 19, x_text,self.y_text)
            self.game.draw_text("processamento. Normalmente, o HD utiliza a RAM como ponte de transferência ", 19, x_text,self.y_text + 20)
            self.game.draw_text("de informação, mas  é possível emular essa RAM no HD, aumentando a ", 19, x_text,self.y_text + 40)
            self.game.draw_text("capacidade total de RAM.", 19, x_text,self.y_text + 60)
        if layer == 44:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A capacidade de armazenamento de dados do HD é medida em Gigabytes e ", 19, x_text, self.y_text)
            self.game.draw_text("Terabytes. Já a sua velocidade de transferência é medida em MB/s.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Os HDs mais comuns no mercado são os de capacidade acima de 500 GB até ", 19, x_text,self.y_text + 40)
            self.game.draw_text("2 TB.", 19, x_text,self.y_text + 60)
        if layer == 45:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O funcionamento do HD é mecânico. Ele consiste no uso de um  ", 19, 275, self.y_text)
            self.game.draw_text("disco interno capaz de girar em torno de si, próximo a uma bobina  ", 19, 275, self.y_text + 20)
            self.game.draw_text("em forma de pinça que propaga impulsos magnéticos no disco.", 19, 275, self.y_text + 40)
            self.game.draw_text("Esses impulsos interagem com o disco gravando dados. ", 19, 275, self.y_text + 60)
        if layer == 46:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("É importante saber que a bobina não encosta no ", 19, x_text, self.y_text)
            self.game.draw_text("disco.  Caso isso ocorra, principalmente se o HD estiver ligado,", 19, x_text, self.y_text + 20)
            self.game.draw_text("pode causar sérios danos como travamentos, perda de ", 19, x_text, self.y_text + 40)
            self.game.draw_text("arquivos ou o não funcionamento completo do HD.", 19, x_text, self.y_text + 60)
        if layer == 47:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Por isso é recomendado ter cuidado ao manusear o HD enquanto estiver ", 19, x_text, self.y_text)
            self.game.draw_text("em uso, pois qualquer choque pode causar sérios problemas.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Esse problema ocorre com mais frequência com notebook, pois, devido ", 19, x_text, self.y_text + 40)
            self.game.draw_text("à sua portabilidade, também são mais passíveis de quedas e choques.", 19, x_text, self.y_text + 60)
        if layer == 48:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Outra característica interessante a ser notada é que, como ", 19, 255, self.y_text)
            self.game.draw_text("a gravação ocorre por impulsos magnéticos, o uso de ímãs  ", 19, 255, self.y_text + 20)
            self.game.draw_text("próximos ao HD também pode causar danos, mas isso ocorre ", 19, 255, self.y_text + 40)
            self.game.draw_text("apenas com ímãs fortes se o HD estiver desligado. Isso ", 19, 255, self.y_text + 60)
            self.game.draw_text("ocorre  porque os ímãs desestabilizam o campo magnético do", 19, 255, self.y_text + 80)
            self.game.draw_text("disco, podendo apagar as informações.", 19, 255, self.y_text + 100)
        if layer == 49:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Então, por motivos de segurança, nunca deixe um HD próximo a um imã.", 19, x_text, self.y_text)
            self.game.draw_text("Outra parte importante do HD é o conector de energia, que fornece ", 19, x_text, self.y_text + 20)
            self.game.draw_text("energia para o hardware, e o conector de transferência de dados. ", 19, x_text, self.y_text + 40)
            self.game.draw_text("Antigamente, utilizava-se o padrão IDE, porém, os HDs de hoje possuem ", 19, x_text, self.y_text + 60)
            self.game.draw_text("o conector que permite uma transferência de dados mais rápida, o SATA.", 19, x_text, self.y_text + 80)
        if layer == 50:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("É importante saber que existem dois conectores SATA no HD. Um para se conectar ", 19, x_text, self.y_text)
            self.game.draw_text("à fonte, que é o que foi visto nas fases anteriores, e outro para se conectar à ", 19, x_text, self.y_text + 20)
            self.game.draw_text("placa-mãe. Este  é mais simples de se identificar, pois é o menor conector SATA.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Para conectar o HD à placa-mãe basta pegar um cabo SATA e conectá-lo na entrada ", 19, x_text, self.y_text + 60)
            self.game.draw_text("SATA (em forma de L) da placa mãe. Geralmente a placa-mãe possui mais ", 19, x_text, self.y_text + 80)
            self.game.draw_text("de um conector SATA.", 19, x_text, self.y_text + 100)
        if layer == 51:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Existem três tipos de conectores SATA, o SATA I, SATA II e ", 19, 275, self.y_text)
            self.game.draw_text("SATA III. A diferença entre eles é a maior velocidade de ", 19, 275, self.y_text + 20)
            self.game.draw_text("transmissão do primeiro ao terceiro. O padrão atual é o ", 19, 275, self.y_text + 40)
            self.game.draw_text("SATA III. Sua velocidade de transmissão chega a 600 MB/s", 19, 275, self.y_text + 60)
            self.game.draw_text("Recentemente esse padrão também está sendo substituído ", 19, 275, self.y_text + 80)
            self.game.draw_text("por outro que você verá daqui a pouco.", 19, 275, self.y_text + 100)
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
            self.game.draw_text("A vida útil de um HD é de, em média, 6 anos. Então, para preservar os dados ", 19, x_text, self.y_text)
            self.game.draw_text("contidos nele deve ser feita uma cópia de segurança chamada de ", 19, x_text,self.y_text + 20)
            self.game.draw_text("backup de dados. Ela geralmente é feita pela transferência dos dados de", 19, x_text,self.y_text + 40)
            self.game.draw_text("um HD para outro dispositivo de armazenamento, mas também há uma técnica", 19, x_text,self.y_text + 60)
            self.game.draw_text("de arranjo de discos independentes que consiste em duplicar a informação", 19, x_text,self.y_text + 80)
            self.game.draw_text("em um HD, caso haja problema, em outro HD. Essa técnica é chamada de RAID.", 19, x_text,self.y_text + 100)
        if layer == 61:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O RAID, além de desempenhar uma maior disponibilidade de dados, ", 19, x_text, self.y_text)
            self.game.draw_text("proporciona maior desempenho. Apesar de convencional, não é uma ", 19, x_text, self.y_text + 20)
            self.game.draw_text("tecnica muito utilizada pelos leigos, pois pode causar uma total ", 19, x_text, self.y_text + 40)
            self.game.draw_text("perda de dados, então pense bem antes de recomendar ou realizar", 19, x_text, self.y_text + 60)
            self.game.draw_text("essa prática.", 19, x_text, self.y_text + 80)
        if layer == 62:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O RAID pode ser classificado em diversos níveis, como o Nível 0, em que os discos", 19, x_text, self.y_text)
            self.game.draw_text("se comportam como se fossem apenas um devido ao particionamento de dados. ", 19, x_text, self.y_text + 20)
            self.game.draw_text("Como esse nível, a capacidade de armazenamento e a taxa de transferência de  ", 19, x_text, self.y_text + 40)
            self.game.draw_text("dados aumentam, porém, caso um HD falhe, todos os discos ficam comprometidos.", 19, x_text, self.y_text + 60)
        if layer == 63:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Existem outros como o nível 1, que pode ser compreendido como ", 19, x_text, self.y_text)
            self.game.draw_text("o RAID propriamente dito, pois os discos são utilizados para ", 19, x_text, self.y_text + 20)
            self.game.draw_text("fornecer redundância dos dados e o nível 5, que funciona como o", 19, x_text, self.y_text + 40)
            self.game.draw_text("RAID nível 0, mas com a possibilidade de recuperação de informação ", 19, x_text, self.y_text + 60)
            self.game.draw_text("mesmo com a falha de um HD.", 19, x_text, self.y_text + 80)
        if layer == 64:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Essa técnica é mais utilizada em servidores e bancos de dados, mas também ", 19, x_text, self.y_text)
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
            self.game.draw_text("Agora você vai ver como fazer o processo de RAID 0.", 19,x_text, self.y_text)
            self.game.draw_text("Foi escolhido o nível 0 por se tratar do mais comum e mais simples.", 19,x_text, self.y_text + 20)
            self.game.draw_text("É importante saber que essa prática é permitida em determinados tipos ", 19,x_text, self.y_text + 40)
            self.game.draw_text("de placas-mãe (geralmente as mais recentes), então é bom ler o manual ", 19,x_text, self.y_text + 60)
            self.game.draw_text("dela, principalmente a respeito do modo de inicialização. O modo ", 19,x_text, self.y_text + 80)
            self.game.draw_text("de ativação da RAID também depende da BIOS instalada na placa-mãe.", 19,x_text, self.y_text + 100)
        if layer == 68:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Inicialmente, deve-se conectar os HDs (preferencialmente com a mesma ", 19,x_text, self.y_text)
            self.game.draw_text("capacidade de armazenamento e padrão de conexão e sem nenhum arquivo, ", 19,x_text, self.y_text + 20)
            self.game.draw_text("pois será formatado no final do processo) nas entradas SATA da placa", 19,x_text, self.y_text + 40)
            self.game.draw_text("-mãe. Como dito anteriormente, dependendo da placa-mãe pode haver uma", 19,x_text, self.y_text + 60)
            self.game.draw_text("ordem específica de conectores. Depois da conexão dos cabos de energia e ", 19,x_text, self.y_text + 80)
            self.game.draw_text("transferência de dados, deve-se ligar o computador e abrir o setup da BIOS.", 19,x_text, self.y_text + 100)
        if layer == 69:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Para fazer isso, durante a inicialização, deve-se pressionar uma", 19, 255, self.y_text)
            self.game.draw_text("tecla específica do teclado até aparecer o setup. Geralmente essa ", 19, 255, self.y_text + 20)
            self.game.draw_text("tecla é o delete, F12, Esc, F2, entre outras (é preciso consultar ", 19, 255,self.y_text + 40)
            self.game.draw_text("o manual da placa-mãe).", 19, 255,self.y_text + 60)
        if layer == 70:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Após aparecer o setup da BIOS, vá até a opção de seleção de modo ", 19, x_text, self.y_text)
            self.game.draw_text("de SATA (geralmente está no menu chipset).", 19, x_text, self.y_text + 20)
            self.game.draw_text("Depois, nessa opção de configuração SATA (configuration SATA em ", 19, x_text,self.y_text + 40)
            self.game.draw_text("inglês), mude a opção padrão, geralmente AHCI, sigla para ", 19, x_text,self.y_text + 60)
            self.game.draw_text("Advanced Host Controller Interface, para a opção", 19, x_text,self.y_text + 80)
            self.game.draw_text("RAID. Depois, salve e saia do setup.", 19, x_text,self.y_text + 100)
        if layer == 71:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Enquanto o computador estiver refazendo o boot, pressione as teclas ", 19, x_text, self.y_text)
            self.game.draw_text("‘ctrl’ e ‘i’ do teclado para aparecer a tela de configuração de RAID.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Selecione a opção de criação de volume RAID (create volume RAID em ", 19, x_text,self.y_text + 40)
            self.game.draw_text("inglês). Após aparecer a janela de criação, adicione um nome ao novo ", 19, x_text,self.y_text + 60)
            self.game.draw_text("volume e selecione o tamanho da tira (strip size) adequado para o ", 19, x_text,self.y_text + 80)
            self.game.draw_text("RAID 0. Essa informação será mostrada na aba de ajuda.", 19, x_text,self.y_text + 100)
        if layer == 72:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Depois, coloque a capacidade de armazenamento como a máxima dos  ", 19, 255, self.y_text)
            self.game.draw_text("HDs juntos (já é a opção padrão).", 19, 255, self.y_text + 20)
            self.game.draw_text("Por fim, selecione a opção de criar volume (create volume).", 19, 255,self.y_text + 40)
        if layer == 73:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Aparecerá uma mensagem de aviso de que os dados serão", 19, x_text, self.y_text)
            self.game.draw_text("apagados. Basta clicar em sim (yes).", 19, x_text, self.y_text + 20)
            self.game.draw_text("Quando voltar para a tela inicial de configuração de RAID,", 19, x_text, self.y_text + 40)
            self.game.draw_text("selecione sair (exit).", 19, x_text, self.y_text + 60)
        if layer == 74:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para testar se o RAID foi feito com êxito, acesse o setup da BIOS ", 19, x_text, self.y_text)
            self.game.draw_text("novamente e vá nas opções de boot. Caso haja uma opção com o nome ", 19, x_text, self.y_text + 20)
            self.game.draw_text("do volume novo, tudo foi feito corretamente. Por fim, selecione ", 19, x_text, self.y_text + 40)
            self.game.draw_text("essa opção e salve as configurações.", 19, x_text, self.y_text + 60)
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
            self.game.draw_text("Agora você vai ver o dispositivo de armazenamento mais recente que ", 19, x_text, self.y_text)
            self.game.draw_text("provavelmente substituirá completamente os HDs, o SSD.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Os SSD, sigla para solid state drive, são unidades de armazenamento ", 19, x_text, self.y_text + 40)
            self.game.draw_text("que utilizam células de memórias flash. Ele se difere do HD por não ", 19, x_text, self.y_text + 60)
            self.game.draw_text("ser mecânico, o modo de armazenamento de dados funciona a partir de ", 19, x_text, self.y_text + 80)
            self.game.draw_text("um fenômeno chamado tunelamento quântico.", 19, x_text, self.y_text + 100)
        if layer == 78:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Dentre as melhorias do SSD em relação ao HD podemos constatar a ", 19, 255, self.y_text)
            self.game.draw_text("ausência de vibrações, uma vez que sua construção e funcionamento ", 19, 255, self.y_text + 20)
            self.game.draw_text("não é mecânica, o que elimina também os ruídos e o risco de mal ", 19, 255, self.y_text + 40)
            self.game.draw_text("funcionamento por choques físicos, além de uma menor massa e um ", 19, 255, self.y_text + 60)
            self.game.draw_text("consumo reduzido de energia.", 19, 255, self.y_text + 80)
        if layer == 79:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Quanto à velocidade de transferência de dados, essa é a principal ", 19, 255, self.y_text)
            self.game.draw_text("evolução. Enquanto um HD possui uma velocidade de leitura e  ", 19, 255, self.y_text + 20)
            self.game.draw_text("escrita de até 200 MB/s, o SSD de padrão SATA possui uma velocidade ", 19, 255, self.y_text + 40)
            self.game.draw_text("de mais de 500 MB/s.", 19, 255, self.y_text + 60)
        if layer == 80:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Mas o SSD ainda possui algumas desvantagens em relação ao HD, como ", 19, x_text, self.y_text)
            self.game.draw_text("o alto custo e caso ele pare de funcionar, não há nenhuma chance de", 19, x_text, self.y_text + 20)
            self.game.draw_text("recuperar os dados, diferente do HD, que ainda que esteja em mau ", 19, x_text, self.y_text + 40)
            self.game.draw_text("funcionamento, é possível realizar uma recuperação.", 19, x_text, self.y_text + 60)
        if layer == 81:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Essas vantagens ditas do SSD foram para o padrão SATA, idêntico  ", 19, 250, self.y_text)
            self.game.draw_text("ao do HD (ambos possuem o mesmo modo de instalação), mas já ", 19, 250, self.y_text + 20)
            self.game.draw_text("existe uma melhoria para a tecnologia dos SSDs, que é a da ", 19, 250, self.y_text + 40)
            self.game.draw_text("mudança do padrão de entrada.", 19, 250, self.y_text + 60)
        if layer == 82:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O novo padrão de entrada para SSDs é o M.2. Esse padrão possui vários protocolos ", 19, x_text, self.y_text)
            self.game.draw_text("distintos. Os mais comuns são o protocolo do padrão SATA e o do padrão NVME,  ", 19, x_text, self.y_text + 20)
            self.game.draw_text("sigla para Non-Volatile Memory Express. O padrão M.2 SATA possui uma velocidade ", 19, x_text, self.y_text + 40)
            self.game.draw_text("de transferência muito maior que a do SSD de padrão SATA III, podendo chegar a  ", 19, x_text, self.y_text + 60)
            self.game.draw_text("mais de 1300 MB/s, o que é quase três vezes mais do que o ", 19, x_text, self.y_text + 80)
            self.game.draw_text("máximo de um SSD SATA III.", 19, x_text, self.y_text + 100)
        if layer == 83:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Já o padrão M.2 NVME possui um protocolo com capacidades de transferência", 19, x_text, self.y_text)
            self.game.draw_text("idênticas ao PCI Express da placa-mãe, com modelos atuais chegando a uma", 19, x_text, self.y_text + 20)
            self.game.draw_text("velocidade de transferência de mais de 3400 MB/s, quase 6 vezes mais do ", 19, x_text, self.y_text + 40)
            self.game.draw_text("que o máximo de SSD SATA III.", 19, x_text, self.y_text + 60)
        if layer == 84:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Além da diferença de velocidade, esse novo padrão se diferencia pelo tamanho ", 19, x_text, self.y_text)
            self.game.draw_text("do hardware, sendo bem menor do que o SSD SATA III.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Agora você vai ver como instalar um SSD M.2.", 19, x_text, self.y_text + 40)
            self.game.draw_text("Por se tratar de um padrão novo de conexão, ele só estará presente em ", 19, x_text, self.y_text + 60)
            self.game.draw_text("placas-mãe recentes.", 19, x_text, self.y_text + 80)
        if layer == 85:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para conectar um SSD M.2, posicione-o no sentido em que possa ver ", 19, x_text, self.y_text)
            self.game.draw_text("os chips dele e insira a parte dos “dentes” no conector. De início,", 19, x_text, self.y_text + 20)
            self.game.draw_text("ele ficará um pouco elevado, mas basta pressioná-lo para o sentido", 19, x_text, self.y_text + 40)
            self.game.draw_text("da placa-mãe e parafusá-lo com uma chave.", 19, x_text, self.y_text + 60)
            self.game.draw_text("Pronto! A instalação é bem rápida.", 19, x_text, self.y_text + 80)
        if layer == 86:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Outra característica interessante dos SSDs é que eles também podem ", 19, x_text, self.y_text)
            self.game.draw_text("ser usados em RAID, mas fique atento quanto a isto: um SSD só pode ", 19, x_text, self.y_text + 20)
            self.game.draw_text("fazer RAID com outro SSD e um HD só pode fazer RAID com outro HD. ", 19, x_text, self.y_text + 40)
            self.game.draw_text("A tentativa mista pode causar sérios problemas como a perda de ambos.", 19, x_text, self.y_text + 60)
        if layer == 87:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O SSD M.2 NVME possui uma configuração diferente, pois não utiliza ", 19, 255, self.y_text)
            self.game.draw_text("o padrão SATA, então o processo de RAID pelo setup da BIOS é ", 19, 255, self.y_text + 20)
            self.game.draw_text("diferente. Vamos testar seus conhecimentos adquiridos.", 19, 255, self.y_text + 80)
        if layer == 88:
            #FAZER QUESTÃO  
            pass
        if layer == 89:
            self.draw_very_good()
        if layer == 90:
            #FAZER QUESTÃO  
            pass
        if layer == 91:
            self.draw_very_good()
        if layer == 92:
            #FAZER QUESTÃO  
            pass
        if layer == 93:
           self.draw_very_good()
        if layer == 94:
            #FAZER QUESTÃO  
            pass
        if layer == 95:
           self.draw_very_good()
        if layer == 96:
           #FAZER QUESTÃO  
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
            