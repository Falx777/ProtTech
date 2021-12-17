import pygame, time
from data.score import *
from pygame.locals import *
from data.questions import *


class Fases5():
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


class FaseFiveWorldOne(Fases5):
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
        Fases5.__init__(self, game)

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
            #if not self.gamdata/img_layer:
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
            """if self.gamdata/img_layer:
                if self.layers[len(self.layers) - 1] != 18 and self.layers[len(self.layers) - 1] :
                    wri_wro = self.score.alternatives(self.answer[str(self.layers[len(self.layers) - 1])], int(self.state))
                    if wri_wro:
                        self.wright = True
                        if self.wright:
                            pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                            pygame.mixer.Channel(1).set_volume(0.04)
                            self.i += 1
                            self.layers.append(self.i)
                            self.gamdata/img_layer = False
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
            self.game.draw_text("Nesta fase você verá um pouco sobre alguns periféricos do computador.", self.font_size, x_text, self.y_text)
        if layer == 2:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os dispositivos periféricos são aqueles que possuem uma interação ", self.font_size, x_text, self.y_text)
            self.game.draw_text("mais direta com o usuário do computador e mais distante da parte ", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("de funcionamento interno, daí o nome periférico. Eles realizam ", self.font_size, x_text, self.y_text + 40)
            self.game.draw_text("uma interação com os sentidos, podendo ser visual, física ou", self.font_size, x_text, self.y_text + 60)
            self.game.draw_text("data/auditiva.", self.font_size, x_text, self.y_text + 80)
        if layer == 3:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Essa interação pode ser tanto para realizar um processo quanto para", self.font_size, 125, 360)
            self.game.draw_text("transmitir os resultados dele. A partir disso, classificamos os", self.font_size, 125, 415)
            self.game.draw_text("periféricos como dispositivos de entrada e saída.", self.font_size, 125, 435)
        if layer == 4:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Dentre esses dispositivos, há também a classificação como essenciais ", self.font_size, x_text, self.y_text)
            self.game.draw_text("e não essenciais. Os dispositivos essenciais são aqueles em que caso ", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("o usuário não o tenha, isso dificultará muito o uso do computador. ", self.font_size, x_text, self.y_text + 40)
            self.game.draw_text("Já os dispositivos não essenciais são para aplicações específicas, ", self.font_size, x_text, self.y_text + 60)
            self.game.draw_text("que não são necessárias para a manipulação do computador.", self.font_size, x_text, self.y_text + 80)
        if layer == 5:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os dispositivos essenciais dos computadores são: Mouse, Teclado, ",self.font_size, x_text, self.y_text)
            self.game.draw_text("Gabinete, Monitor e dispositivo de saída de som.", self.font_size,x_text, self.y_text + 20)
        if layer == 6:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Já os dispositivos não essenciais são: impressoras, pen drives, ", self.font_size,251, self.y_text)
            self.game.draw_text("câmeras, cartões de memória e microfones.", self.font_size,251, self.y_text + 20)
            self.game.draw_text("Vamos iniciar com o monitor.", self.font_size,251, self.y_text + 40)
        if layer == 7:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os monitores são os hardwares de saída do computador. Sua função é ", 20, x_text, self.y_text)
            self.game.draw_text("transmitir a informação processada por meio de imagens.", 20, x_text,self.y_text + 20)
            self.game.draw_text("Os componentes de destaque do monitor são o display, os circuitos ", 20, x_text, self.y_text + 40)
            self.game.draw_text("eletrônicos, uma proteção (geralmente de plástico), um conector ", 20, x_text, self.y_text + 60)
            self.game.draw_text("para um cabo de energia que se liga à tomada e um conector de ", 20, x_text, self.y_text + 80)
            self.game.draw_text("transmissão de dados (impressão de dados no display).", 20, x_text, self.y_text + 100)
        if layer == 8:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Essa conexão com a fonte permite o funcionamento do monitor O ", 20, x_text, self.y_text)
            self.game.draw_text("display é a parte do monitor que mostra as informações propriamente ditas.", 20, x_text,self.y_text + 20)
            self.game.draw_text("Os circuitos internos fazem a configuração de transmissão para o display.", 20, x_text, self.y_text + 40)
        if layer == 9:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Na parte do display, existem tipos diferentes e cada ", 20, 250, self.y_text)
            self.game.draw_text("um deles possui uma tecnologia diferente, o que ", 20, 250,self.y_text + 20)
            self.game.draw_text("influencia em transmissões com configurações de imagens ", 20, 250,self.y_text + 40)
            self.game.draw_text("diferentes, desde a resolução, fidelidade de cor, ", 20, 250,self.y_text + 60)
            self.game.draw_text("brilho e taxa de atualização.", 20, 250,self.y_text + 80)
        if layer == 10:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Os monitores com os displays mais comuns são os do tipo LCD, sigla para Liquid ", 19, x_text, self.y_text)
            self.game.draw_text("Cristal Display e LED, sigla para Light Emitting Diode.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Os monitores LCD possuem lâmpadas fluorescentes que iluminam peças de vidro", 19, x_text, self.y_text + 40)
            self.game.draw_text("polarizado preenchidas com um cristal líquido para formar a imagem.", 19, x_text, self.y_text + 60)
        if layer == 11:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Os monitores LED possuem um princípio semelhante ao LCD, com a única ", 19,x_text, self.y_text)
            self.game.draw_text("diferença sendo o uso de lâmpadas LED em vez de fluorescentes. O LED ", 19, x_text, self.y_text + 20)
            self.game.draw_text("é uma evolução do LCD, pois pode ser mais fino e mais eficiente ", 19, x_text,self.y_text + 40)
            self.game.draw_text("energeticamente.", 19, x_text,self.y_text + 60)
        if layer == 12:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Além disso, as diferenças mais notáveis desses dois tipos ", 21, 239,self.y_text)
            self.game.draw_text("de monitores é a diferença de contraste, fidelidade e número ", 21, 239,self.y_text + 20)
            self.game.draw_text("de cores em que o LED é superior em tudo em relação ao LCD, ", 21, 239, self.y_text + 40)
            self.game.draw_text("com a ordem de contraste por pixel chegando na casa dos", 21, 239, self.y_text + 60)
            self.game.draw_text("milhões enquanto que no LCD, está na casa dos milhares.", 21, 239, self.y_text + 80)
        if layer == 13:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O conector de transferência de imagem também pode ser diferente.", 21, x_text, self.y_text)
            self.game.draw_text("Como visto anteriormente, os conectores de transferência de ", 21, x_text, self.y_text + 20)
            self.game.draw_text("imagens em tempo real podem ser USB, HDMI, DisplayPort e VGA.", 21, x_text, self.y_text + 40)
        if layer == 14:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os monitores mais comuns no mercado atual são os com conectores ", 21, x_text, self.y_text)
            self.game.draw_text("HDMI e VGA. Você já viu a diferença entre eles, mas uma coisa que ", 21, x_text, self.y_text + 20)
            self.game.draw_text("não foi dita foi a resolução máxima que cada um suporta.", 21, x_text, self.y_text + 40)
        if layer == 15:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O conector VGA permite uma transmissão de imagem em uma ", self.font_size, 249, self.y_text)
            self.game.draw_text("resolução máxima de 2040 x 1536 pixels, isso é um pouco ", self.font_size, 249, self.y_text + 20)
            self.game.draw_text("mais do que uma alta resolução padrão (1920 x 1080).", self.font_size, 249, self.y_text + 40)
            self.game.draw_text("Já o conector HDMI permite uma transmissão de imagem em ", self.font_size, 249, self.y_text + 60)
            self.game.draw_text("uma resolução máxima de 4k x 2k, ou seja, ", self.font_size, 249, self.y_text + 80)
            self.game.draw_text("4096 x 2160 pixels.", self.font_size, 249, self.y_text + 100)
        if layer == 16:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Além disso, há uma considerável diferença de taxa de atualização máxima ", 20, x_text, self.y_text)
            self.game.draw_text("de acordo com a conexão.", 20, x_text, self.y_text + 20)
            self.game.draw_text("Para instalar o monitor, basta conectá-lo à placa-mãe, pelo cabo de ", 20, x_text, self.y_text + 40)
            self.game.draw_text("transferência de dados e depois o conectar o cabo de energia na tomada. ", 20, x_text, self.y_text + 60)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos...", 20, x_text, self.y_text + 80)
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
            #FAZER JOGO
            pass
        if layer == 22:
            self.draw_very_good()
        if layer == 23:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora você vai ver outro periférico, o teclado.", 21, x_text,self.y_text)
            self.game.draw_text("O teclado é um componente periférico de entrada, pois, a partir da ", 21, x_text,self.y_text + 20)
            self.game.draw_text("sua manipulação pelo usuário, os dados são inseridos no computador.", 21, x_text,self.y_text + 40)
        if layer == 24:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("A constituição básica de um teclado são as teclas e um chip ", 19, 247,self.y_text)
            self.game.draw_text("interno. Cada uma das teclas possui caracteres (1 ou mais de 1) ", 19, 247,self.y_text + 20)
            self.game.draw_text("impressos que simbolizam uma função ou um caractere gráfico. Ao ", 19, 247,self.y_text + 40)
            self.game.draw_text("pressionar uma tecla, o chip interno envia a informação para o ", 19, 247,self.y_text + 60)
            self.game.draw_text("computador, podendo ser de forma cabeada ou sem fio", 19, 247,self.y_text + 80)
            self.game.draw_text("(wireless).", 19, 247,self.y_text + 100)
        if layer == 25:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os principais padrões de conectores de teclado são o ps/2 e o USB, além ", 21, x_text,self.y_text)
            self.game.draw_text("da conexão bluetooth.", 21, x_text,self.y_text + 20)
        if layer == 26:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            
            self.game.draw_text("O conector ps/2 é um padrão de entrada mais antigo do que os outros e já ", 21, x_text,self.y_text )
            self.game.draw_text("nem aparece mais em placas-mãe mais novas, principalmente por ter um ", 21, x_text,self.y_text + 20)
            self.game.draw_text("encaixe único e proporcionar uma transferência baixa de dados e em  ", 21, x_text,self.y_text + 40)
            self.game.draw_text("menor velocidade. Já a conexão USB proporciona uma velocidade de  ", 21, x_text,self.y_text + 60)
            self.game.draw_text("transmissão cerca de 800 mil vezes mais rápida.", 21, x_text,self.y_text + 80)
        if layer == 27:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Mas mesmo com uma grande desvantagem no quesito de trans-", 20, 247,self.y_text)
            self.game.draw_text("missão de dados, o padrão ps/2 ainda é utilizado como uma forma de ", 20, 247,self.y_text + 20)
            self.game.draw_text("segurança, pois uso da porta USB requer habilitação pelo software na máquina, ", 20, 140,self.y_text + 40)
            self.game.draw_text("servindo como uma porta para uso mal intencionado do computador, podendo", 20, 140,self.y_text + 60)
            self.game.draw_text("utilizar um pendrive, por exemplo, para copiar dados, instalar ", 20, 140,self.y_text + 80)
            self.game.draw_text("malwares, dentre outras coisas, aí é que entra o padrão ps/2.", 20, 140,self.y_text + 100)
        if layer == 28:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Por se tratar de um padrão diferente, o administrador de um computador pode ", 19, x_text, self.y_text)
            self.game.draw_text("bloquear todas as portas USB sem prejudicar o teclado.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Para instalar o teclado, basta conectar o cabo à placa-mãe. Se for USB, ", 19, x_text, self.y_text + 40)
            self.game.draw_text("basta plugar o cabo. Se for ps/2, você deve ficar atento à cor, pois a entrada ps/2 ", 19, x_text, self.y_text + 60)
            self.game.draw_text("é semelhante à entrada do mouse, mas se você ligar, ela não funcionará.", 19, x_text, self.y_text + 80)
        if layer == 29:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para instalar o teclado, basta conectar o cabo à placa-mãe. Se for ", 19, x_text, self.y_text)
            self.game.draw_text("USB, basta plugar o cabo. Se for ps/2, você deve ficar atento à cor, ", 19, x_text, self.y_text + 20)
            self.game.draw_text("pois a entrada ps/2 é semelhante à entrada do mouse, mas se você ", 19, x_text, self.y_text + 40)
            self.game.draw_text("ligar, ela não funcionará.", 19, x_text, self.y_text + 60)
        if layer == 30:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para diferenciar uma entrada da outra, basta saber a qual cor corresponde o ", 19, x_text, self.y_text)
            self.game.draw_text("periférico, ou olhar na placa-mãe. Geralmente, o conector ps/2 está ", 19, x_text, self.y_text + 20)
            self.game.draw_text("representado pela cor roxa (lilás).", 19, x_text, self.y_text + 40)
            self.game.draw_text("Ainda sobre os teclados, existem tipos diferentes quanto a sua ergonomia.", 19, x_text, self.y_text + 60)
            self.game.draw_text("Os tipos de teclado mais comuns no mercado atual são o teclado mecânico ", 19, x_text, self.y_text + 80)
            self.game.draw_text("e o de membrana.", 19, x_text, self.y_text + 100)
        if layer == 31:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O teclado mecânico possui interruptores individuais de baixo das ", 19, x_text, self.y_text)
            self.game.draw_text("teclas e são ativados por uma mola. Graças a independência das teclas, ", 19, x_text, self.y_text + 20)
            self.game.draw_text("esse tipo de teclado reconhece mais de um comando de forma simultânea ", 19, x_text, self.y_text + 40)
            self.game.draw_text("e outra de suas características peculiares é o retorno sonoro a ", 19, x_text, self.y_text + 60)
            self.game.draw_text("cada pressão de tecla.", 19, x_text, self.y_text + 80)
        if layer == 32:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O teclado de membrana não possui teclas independentes em um circuito, ", 19, x_text, self.y_text)
            self.game.draw_text("além disso, há uma membrana, geralmente de silicone, sensível à ", 19, x_text, self.y_text + 20)
            self.game.draw_text("pressão que interliga as peças.", 19, x_text, self.y_text + 40)
        if layer == 33:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Dentre as vantagens do teclado de membrana estão uma maior ", 19, 243, self.y_text)
            self.game.draw_text("resistência à sujeira e líquidos e a possibilidade de fabricação de ", 19, 243, self.y_text + 20)
            self.game.draw_text("modelos flexíveis, além do preço relativamente mais baixo do que o ", 19, 243, self.y_text + 40)
            self.game.draw_text("teclado mecânico (devido à sua construção mais simples). Já a ", 19, 243, self.y_text + 60)
            self.game.draw_text("desvantagem desse tipo de teclado pode ser vista na falta de um ", 19, 243, self.y_text + 80)
            self.game.draw_text("retorno tátil para cada tecla e um tempo de resposta mais longo.", 19, 243, self.y_text + 100)
        if layer == 34:
            #FAZER JOGO
            pass
        if layer == 35:
            self.draw_very_good()
        if layer == 36:
             #FAZER JOGO
            pass
        if layer == 37:
            self.draw_very_good()
        if layer == 38:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O mouse é outro dispositivo de entrada. Ele tem como função movimentar o ", 19, x_text,self.y_text)
            self.game.draw_text("cursor na tela do computador com interface gráfica. Além da movimentação ", 19, x_text,self.y_text + 20)
            self.game.draw_text("do cursor, outras movimentações acionadas pelo mouse são o clique, o duplo ", 19, x_text,self.y_text + 40)
            self.game.draw_text("clique e arrastar e soltar. Os mouses", 19, x_text,self.y_text + 60)
            self.game.draw_text("mais simples possuem três botões (O botão direito, o botão ", 19, x_text,self.y_text + 80)
            self.game.draw_text("esquerdo e o scroll).", 19, x_text,self.y_text + 100)
        if layer == 39:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Assim como o teclado, o mouse pode ser conectado por duas portas ", 19, 255,self.y_text)
            self.game.draw_text("principais: a ps/2 e o USB (além da conexão sem fio). ", 19, 255,self.y_text + 20)
            self.game.draw_text("A especificação da conexão ps/2 do mouse é idêntica ao ps/2 do ", 19, 255,self.y_text + 40)
            self.game.draw_text("teclado, com diferença que ela só funciona para conectar o mouse. ", 19, 255,self.y_text + 60)
            self.game.draw_text("Caso um teclado seja conectado, ele não vai funcionar.", 19, 255,self.y_text + 80)
        if layer == 40:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ainda no ps/2 do mouse, para diferenciá-lo do ps/2 do teclado, basta ", 19, x_text,self.y_text)
            self.game.draw_text("identificar sua cor, que geralmente é verde. No conector USB, ocorre ", 19, x_text,self.y_text + 20)
            self.game.draw_text("a mesma especificação que para o usb do teclado, com ambos podendo ", 19, x_text,self.y_text + 40)
            self.game.draw_text("trocar de entrada sem haver problema de incompatibilidade.", 19, x_text,self.y_text + 60)
        if layer == 41:
              #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Além do mouse, existem dispositivos semelhantes quanto ao serviço de ", 19, x_text,self.y_text)
            self.game.draw_text("operação. São eles: o trackball e o touchpad. O touchpad é comumente ", 19, x_text,self.y_text + 20)
            self.game.draw_text("encontrado em notebooks e guia o cursor conforme a posição do dedo em ", 19, x_text,self.y_text + 40)
            self.game.draw_text("sua área de atuação e o trackball é fisicamente parecido com o mouse,", 19, x_text,self.y_text + 60)
            self.game.draw_text("mas a movimentação do cursor se baseia na movimentação da bola", 19, x_text,self.y_text + 80)
            self.game.draw_text("spresente nele, enquanto que o corpo fica estático.", 19, x_text,self.y_text + 100)
        if layer == 42:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Sobre a tecnologia de movimentação do mouse, há dois tipos mais comuns no ", 19, x_text,self.y_text)
            self.game.draw_text("mercado: o mouse óptico e a laser.", 19, x_text,self.y_text + 20)
        if layer == 43:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ambos possuem uma tecnologia baseada na emissão de luz e reflexão dela em ", 19, x_text,self.y_text)
            self.game.draw_text("uma superfície até um processador digital de sinal presente no circuito ", 19, x_text,self.y_text + 20)
            self.game.draw_text("interno do mouse. De acordo com a captação de variação de luz refletida é ", 19, x_text,self.y_text + 40)
            self.game.draw_text("calculada uma coordenada, que é enviada para o computador fazer a", 19, x_text,self.y_text + 60)
            self.game.draw_text("movimentação do cursor.", 19, x_text,self.y_text + 80)
        if layer == 44:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O diferencial entre o mouse óptico e o laser está no tipo de luz emitida.", 19, x_text, self.y_text)
            self.game.draw_text("O mouse óptico utiliza fotodiodos e LED. Já o laser utiliza luz infravermelha.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Devido a utilização de luz infravermelha, o mouse laser permite captar uma ", 19, x_text,self.y_text + 40)
            self.game.draw_text("maior DPI. Mas você deve estar se perguntando, o que é DPI?", 19, x_text,self.y_text + 60)
        if layer == 45:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Bom, DPI, sigla para Dots Per Inch, é a quantidade de pontos que ", 19, 275, self.y_text)
            self.game.draw_text("podem ser encontrados em uma polegada de uma determinada ", 19, 275, self.y_text + 20)
            self.game.draw_text("imagem, podendo ser compreendido também como resolução ", 19, 275, self.y_text + 40)
            self.game.draw_text("medida pelo mouse. Então, quanto maior o DPI, maior a", 19, 275, self.y_text + 60)
            self.game.draw_text("precisão do mouse.", 19, 275, self.y_text + 80)
        if layer == 46:
            #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Geralmente é possível regular a quantidade de DPI, mas se ele for ", 19, x_text, self.y_text)
            self.game.draw_text("aumentado e a resolução for mantida constante, a sensação será de ", 19, x_text, self.y_text + 20)
            self.game.draw_text("um cursor com maior velocidade. Por isso que nas configurações de ", 19, x_text, self.y_text + 40)
            self.game.draw_text("mouse do SO de uma máquina, a opção de aumento de DPI é descrita", 19, x_text, self.y_text + 60)
            self.game.draw_text("como velocidade do ponteiro.", 19, x_text, self.y_text + 80)
        if layer == 47:
             #COLOCAR IMAGEM
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Voltando para os tipos de mouse, um valor comum para mouses a laser ", 19, x_text, self.y_text)
            self.game.draw_text("é de 3600 DPI, podendo ser muito maior do que isso.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Outra diferença entre os tipos de mouse é que o óptico possui um número ", 19, x_text, self.y_text + 40)
            self.game.draw_text("limitado de superfícies para operação, sendo necessárias superfícies", 19, x_text, self.y_text + 60)
            self.game.draw_text("mais lisas e limpas como um mousepad. Já o mouse laser não possui tanta ", 19, x_text, self.y_text + 80)
            self.game.draw_text("interferência quanto a superfície.", 19, x_text, self.y_text + 100)
        if layer == 48:
            #FAZER JOGO
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
            