import pygame, time
from data.score import *
from pygame.locals import *
from data.questions import *


class Fases02():
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


class FaseTwoWorldOne(Fases02):
    def __init__(self, game):
        self.i = 1
        self.layers = [1]
        self.not_fading = True
        self.wrong, self.wright = False, False
        self.score = Score()
        self.margin_reg = "right"
        self.area = dict()
        self.state = "1"
        self.answer = dict()
        self.answer = {'8': 1, '29': 1, '30': 1,'41':1, '47':1, '64':1, '70': 1}
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
        Fases02.__init__(self, game)

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
            self.q = QuestionsTwo(0)
            self.game.current_menu = self.game.fases_1
            self.run_display = False
            self.gaming_layer = False
            self.game.reset_keys()
            self.state = '1'
            self.layers.clear()
            self.i = 1
            self.layers.append(1)
        if self.game.SPACE_KEY and self.layers[len(self.layers) - 1] != 8 and self.layers[len(self.layers) - 1] != 41 and self.layers[len(self.layers) - 1] != 47 and self.layers[len(self.layers) - 1] != 64:
            if not self.gamimg_layer and self.layers[len(self.layers) - 1] != 73:
                self.i += 1
                self.layers.append(self.i)
                self.ok = True
                self.clock = 0
            if not self.gamimg_layer and self.layers[len(self.layers) - 1] == 73:
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
            self.game.draw_text("Agora que você tem um entendimento dos conceitos básicos, você vai se ", self.font_size, x_text, self.y_text)
            self.game.draw_text("aprofundar nos conceitos de cada hardware de um computador.", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("Primeiro veremos a placa-mãe.", self.font_size, x_text, self.y_text + 60)
        if layer == 2:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/placa_mae.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("A placa-mãe, também chamada de motherboard, ou mainboard é o ", self.font_size, x_text, self.y_text)
            self.game.draw_text("componente que serve para interligar todos os outros componentes do ", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("computador, transferindo informações e energia para as demais peças ", self.font_size, x_text, self.y_text + 40)
            self.game.draw_text("de hardware.", self.font_size, x_text, self.y_text + 60)
            self.game.draw_text("Você consegue perceber quão importante é a placa-mãe?", self.font_size, x_text, self.y_text + 80)
        if layer == 3:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/placas_mae.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Aqui está uma imagem de uma placa-mãe genérica e uma placa-mãe recente.", self.font_size, 125, 415)
        if layer == 4:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/super_io.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Vamos começar com uma parte de simples entendimento, o Chip Super I/O.", self.font_size, x_text, self.y_text)
            self.game.draw_text("Esse chip é um controlador de dispositivos de entrada e saída e suas", self.font_size, x_text, self.y_text + 20)
            self.game.draw_text("respectivas portas, daí o seu nome e inglês Input/output.", self.font_size, x_text, self.y_text + 40)
        if layer == 5:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/super_io_2.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Dentre os controles que são passados pelo Super I/O, podemos citar, ",self.font_size, x_text, self.y_text)
            self.game.draw_text("as interfaces de mouse e teclado, porta para impressoras e seriais. ", self.font_size,x_text, self.y_text + 20)
            self.game.draw_text("Recentemente, esse chip perdeu muitas dessas funções para o uso ", self.font_size, x_text,self.y_text + 40)
            self.game.draw_text("das interfaces usb por causa do melhor controle dos componentes ", self.font_size, x_text,self.y_text + 60)
            self.game.draw_text("de maneira independente. ", self.font_size, x_text,self.y_text + 80)
        if layer == 6:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/ssc.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Agora vamos ver outras partes da placa-mãe.", self.font_size,251, self.y_text)
            self.game.draw_text("Você pode ter percebido que a placa-mãe possui diversas ", self.font_size,251, self.y_text + 20)
            self.game.draw_text("entradas, mas não pense que todas têm a mesma função. ", self.font_size,251, self.y_text + 40)
            self.game.draw_text("Essas entradas são classificadas em três tipos:", self.font_size,251, self.y_text + 60)
            self.game.draw_text("slot, soquete e conector.", self.font_size,251, self.y_text + 80)
        if layer == 7:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/ssc.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os slots são os encaixes de RAM e de interconexão de componentes ", 20, x_text, self.y_text)
            self.game.draw_text("periféricos (conhecidos como PCI).", 20, x_text,self.y_text + 20)
            self.game.draw_text("O soquete é um encaixe quadrado onde se coloca o processador.", 20, x_text, self.y_text + 40)
            self.game.draw_text("E o conector é o encaixe de um cabo para equipamentos elétricos ou eletrônicos.", 20, x_text,self.y_text + 60)
            self.game.draw_text("Por exemplo, o conector SATA.", 20, x_text, self.y_text + 80)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos:", 20, x_text, self.y_text + 100)
            self.q = QuestionsTwo(8)
        if layer == 8:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Relacione o encaixe com o termo", 24, 253, 35)
            self.game.display.blit(pygame.image.load(self.q.image), (0, 0))
            self.game.draw_text("Slot", 25, 180, 138)
            self.game.draw_text("Socket", 25, 160, 220)
            self.game.draw_text("Conector", 25, 150, 295)
            self.game.draw_text("Chip BIOS", 25, 140, 379)
            self.game.draw_text("Encaixe processador", 25, 550, 138)
            self.game.draw_text("Encaixe PCI express", 25, 550, 220)
            self.game.draw_text("Não é encaixe", 25, 590, 295)
            self.game.draw_text("Encaixe de energia 24 pinos", 25, 510, 379)
            self.selected_question()
            pygame.display.update()
        if layer == 9:
            self.draw_very_good()
        if layer == 10:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/intel_amd.png'), (275, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Ainda nos soquetes, é importante saber que o seu encaixe vai depender da marca", 19, x_text, self.y_text)
            self.game.draw_text("e da versão do processador.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Vamos trabalhar os processadores mais a frente, mas já é bom saber que ", 19, x_text, self.y_text + 40)
            self.game.draw_text("atualmente as empresas que dominam o ramo de processadores de arquitetura x86", 19, x_text, self.y_text + 60)
            self.game.draw_text("e x64 são a Intel e a AMD.", 19, x_text,self.y_text + 80)
        if layer == 11:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/soquetes.png'), (215, 17))
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.base_layer(layer)
            self.game.draw_text("Cada empresa fabrica processadores que requerem soquetes distintos.", 21,x_text, self.y_text)
            self.game.draw_text("Inclusive, uma mesma empresa possui soquetes diferentes para cada linha", 21, x_text, self.y_text + 20)
            self.game.draw_text("de processadores produzidos.", 21, x_text,self.y_text + 40)
        if layer == 12:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/lga1150.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("No caso da Intel, seus processadores são divididos em linhas e", 21, 239,self.y_text)
            self.game.draw_text("gerações. As linhas antigas de processadores utilizavam um ", 21, 239,self.y_text + 20)
            self.game.draw_text("soquete LGA1150 (LGA, do inglês, Land Grid Array).", 21, 239, self.y_text + 40)
        if layer == 13:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/LGA.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Esse termo LGA indica que os pinos que fazem contato direto do ", 21, x_text, self.y_text)
            self.game.draw_text("processador com a placa-mãe são soldados nesta. E o 1150 significa a", 21, x_text, self.y_text + 20)
            self.game.draw_text("quantidade de pinos. Esse tipo de soquete 1150 era utilizado nos", 21, x_text, self.y_text + 40)
            self.game.draw_text("processadores até a quinta geração.", 21, x_text, self.y_text + 60)
        if layer == 14:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/lga1151.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O soquete de processadores Intel mais presente no mercado atual é o ", 21, x_text, self.y_text)
            self.game.draw_text("LGA1151 (com 1151 pinos). Ele possui o suporte para os processadores Intel ", 21, x_text, self.y_text + 20)
            self.game.draw_text("Celeron, i3, i5, i7 e i9 da sexta geração até a atual (11ª geração).", 21, x_text, self.y_text + 40)
            self.game.draw_text("Como os pinos ficam presos na placa-mãe, geralmente os soquetes ", 21, x_text, self.y_text + 60)
            self.game.draw_text("vêm com uma proteção de metal.", 21, x_text, self.y_text + 80)
        if layer == 15:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/lga2011.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Há também o soquete LGA2011, que é um soquete utilizado em ", self.font_size, 249, self.y_text)
            self.game.draw_text("placas-mãe de computadores top de linha e em servidores.", self.font_size, 249, self.y_text + 20)
            self.game.draw_text("Agora vamos ver os soquetes da concorrente da Intel, a AMD.", self.font_size, 249, self.y_text + 60)
        if layer == 16:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pga.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Uma grande diferença entre os soquetes atuais da Intel e da AMD é que a AMD", 20, x_text, self.y_text)
            self.game.draw_text("utiliza soquetes do tipo PGA (do inglês, Pin Grid Array). Esse tipo de soquete,", 20, x_text, self.y_text + 20)
            self.game.draw_text("diferente do LGA, possui os pinos de ligação direta com a placa-mãe direto no", 20, x_text, self.y_text + 40)
            self.game.draw_text("processador.", 20, x_text, self.y_text + 60)
        if layer == 17:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino_quebrado.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Como os pinos estão no processador, devido ao manuseio ou troca ", 21, x_text, self.y_text)
            self.game.draw_text("constante, esses pinos possuem maior facilidade de serem danificados, ", 21, x_text, self.y_text + 20)
            self.game.draw_text("seja quebrando-os ou entortando-os.", 21, x_text, self.y_text + 40)
        if layer == 18:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/AM4.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("A AMD possui diversos tipos de soquete, mas o mais novo é ", 21, 249,self.y_text)
            self.game.draw_text("que surgiu com a linha Ryzen, o AM4. ", 21, 249,self.y_text + 20)
        if layer == 19:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/seta_soquete.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para colocar um processador no soquete é bem simples. Na parte de trás ou da ", 19,x_text, self.y_text)
            self.game.draw_text("frente do processador há uma seta em realce em um dos cantos. Essa mesma seta ", 19,x_text, self.y_text + 20)
            self.game.draw_text("pode ser encontrada no soquete da placa-mãe.", 19, x_text,self.y_text + 40)
        if layer == 20:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei1.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei2.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei3.png'), (215, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei4.png'), (215, 17))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei5.png'), (215, 17))
            if self.clock == 5:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei6.png'), (215, 17))
            if self.clock == 6:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei7.png'), (215, 17))
            if self.clock == 7:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei8.png'), (215, 17))
            pygame.time.wait(70)
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Primeiro, puxe a ponta da haste de metal (trava) para o lado e depois, ", 19, x_text, self.y_text)
            self.game.draw_text("puxe-a para cima e para trás no sentido da sua mão.", 19, x_text, self.y_text + 20)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 7:
                self.clock = 1
        if layer == 21:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei9.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei10.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei11.png'), (215, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei12.png'), (215, 17))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei13.png'), (215, 17))
            if self.clock == 5:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei14.png'), (215, 17))
            pygame.time.wait(100)
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Se houver uma proteção no soquete, puxe-a também para cima e para trás, ou ela", 19, x_text, self.y_text)
            self.game.draw_text("será puxada com a haste.", 19, x_text, self.y_text + 20)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 5:
                self.clock = 1
        if layer == 22:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei15.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei16.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei17.png'), (215, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei18.png'), (215, 17))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei18.png'), (215, 17))
            pygame.time.wait(250)
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Depois, coloque o processador na posição em que essas setas estejam", 21, x_text, self.y_text)
            self.game.draw_text("apontando para o mesmo local.", 21, x_text, self.y_text + 20)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 4:
                self.clock = 1
        if layer == 23:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei32.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei31.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei30.png'), (215, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei29.png'), (215, 17))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei28.png'), (215, 17))
            if self.clock == 5:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei21.png'), (215, 17))
            if self.clock == 6:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei20.png'), (215, 17))
            if self.clock == 7:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei19.png'), (215, 17))
            if self.clock == 8:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei22.png'), (215, 17))
            if self.clock == 9:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei23.png'), (215, 17))
            if self.clock == 10:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei24.png'), (215, 17))
            if self.clock == 11:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei25.png'), (215, 17))
            if self.clock == 12:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei26.png'), (215, 17))
            if self.clock == 13:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei27.png'), (215, 17))
            if self.clock == 14:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_intel/soquetei1.png'), (215, 17))
            pygame.time.wait(70)
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Por fim, faça o processo reverso do encaixe e movimento da trava.", 21, x_text,self.y_text)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 14:
                self.clock = 1
        if layer == 24:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea1.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea2.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea3.png'), (215, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea4.png'), (215, 17))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea5.png'), (215, 17))
            if self.clock == 5:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea6.png'), (215, 17))
            if self.clock == 6:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea7.png'), (215, 17))
            if self.clock == 7:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea8.png'), (215, 17))
            if self.clock == 8:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea9.png'), (215, 17))
            if self.clock == 9:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea10.png'), (215, 17))
            if self.clock == 10:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea11.png'), (215, 17))
            if self.clock == 11:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea12.png'), (215, 17))
            if self.clock == 12:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea13.png'), (215, 17))
            if self.clock == 13:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea14.png'), (215, 17))
            if self.clock == 14:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea15.png'), (215, 17))
            if self.clock == 15:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea16.png'), (215, 17))
            if self.clock == 16:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/sqt_amd/soquetea17.png'), (215, 17))
            pygame.time.wait(70)
            self.base_layer(layer)
            self.game.draw_text("Os pinos que fazem contato direto do processador com a placa-mãe", 19, 247,self.y_text)
            self.game.draw_text("possuem diversas funções e por isso todos eles são necessários para", 19, 247,self.y_text + 20)
            self.game.draw_text("um funcionamento a longo prazo de um computador. ", 19, 247, self.y_text + 40)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 17:
                self.clock = 1
        if layer == 25:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/evitar.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("No momento de instalação e manuseio de um processador de soquete PGA, ", 19, x_text,self.y_text)
            self.game.draw_text("cuidado para colocá-lo apenas em superfícies planas e sem tome contato ", 19, x_text, self.y_text + 20)
            self.game.draw_text("com energia quando fora do soquete.", 19, x_text, self.y_text + 40)
            self.game.draw_text("E quando for manusear o soquete LGA, tome cuidado para não entortar", 21, x_text, self.y_text + 60)
            self.game.draw_text("os pinos ao forçar o processador no encaixe.", 21, x_text, self.y_text + 80)
        if layer == 26:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/lga_quebrado.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Uma curiosidade é que se um pino de soquete LGA quebrar ou entortar, é", 21, x_text, self.y_text)
            self.game.draw_text("possível trocar o soquete de algumas placas-mãe, mas caso não seja, ", 21, x_text, self.y_text + 20)
            self.game.draw_text("será necessário trocar a placa-mãe por inteiro ou soldar o pino.", 21, x_text, self.y_text + 40)
        if layer == 27:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino_quebrado.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Já no caso de um pino de um soquete PGA quebrar ou entortar,", 21, 247,self.y_text)
            self.game.draw_text("pode-se tentar soldar outro pino, mas se não funcionar, é ", 21, 247,self.y_text + 20)
            self.game.draw_text("necessário trocar o processador.", 21, 247,self.y_text + 40)
        if layer == 28:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino_quebrado.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Geralmente, um processador é bem mais custoso do que uma placa-mãe, então ", 19, x_text, self.y_text)
            self.game.draw_text("é melhor tomar cuidado ao manusear esse tipo de processador.", 19, x_text, self.y_text + 20)
            self.game.draw_text(" Agora vamos testar seus conhecimentos adquiridos.", 19, x_text, self.y_text + 60)
        if layer == 29:
            mx, my = pygame.mouse.get_pos()
            self.gamimg_layer = True
            processor1 = pygame.image.load('data/img/worlds/w1/s2/processador_i.png')
            processador2 = pygame.image.load('data/img/worlds/w1/s2/processador_a.png')
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/mb1.png'), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Analise o soquete e coloque o processador adequado", 20, 220, 35)
            self.game.draw_text("Utilize o mouse para movimentação.", 20, 290, 55)
            self.game.draw_text("Utilize o botão direito para girar o processador.", 20, 240, 75)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/sqt_intel.png'), (0, 0))
            if self.socket_event['hst']:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/haste_1.png'), (0, 0))
            if self.socket_event['hst2']:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/haste_2.png'), (0, 0))
            if self.socket_event['hst3']:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/haste_3.png'), (0, 0))
            if self.socket_event['hst'] and self.socket_event['intel'] == [679, 225]:
                time.sleep(0.6)
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
                self.socket_event['prcssd1'], self.socket_event['prcssd2'], self.socket_event['prtc'], self.socket_event['prtc2'], self.socket_event['hst'], self.socket_event['hst2'], self.socket_event['hst3'], self.socket_event['lkd1'], self.socket_event['angle'], self.socket_event['intel'], self.socket_event['angle2'], self.socket_event['amd'], self.socket_event['lkd2'] = True, True, True, False, True, False, False, False, 0, [4, 329], 0, [28, 97], False
                self.slide['hst'], self.slide['hst3'], self.slide['prtc'] = False, False, False
            if self.socket_event['prcssd2']:
                self.game.display.blit(pygame.transform.rotate(processador2, self.socket_event['angle2']),(self.socket_event['amd'][0], self.socket_event['amd'][1]))
            if self.socket_event['prcssd1']:
                self.game.display.blit(pygame.transform.rotate(processor1, self.socket_event['angle']),(self.socket_event['intel'][0], self.socket_event['intel'][1]))
            if self.socket_event['prtc']:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/protecao.png'), (0, 0))
            if self.socket_event['prtc2']:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/protecao_2.png'), (0, 0))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    #processador
                    if 218 > mx > 44 and 494 > my > 329 and self.socket_event['prcssd1'] and self.socket_event['prcssd2']:
                        if event.button == 1:
                            self.socket_event['prcssd1'] = False
                            self.socket_event['lkd1'] = True
                        if event.button == 3:
                            self.socket_event['angle'] += 90
                    elif 234 > mx > 28 and 302 > my > 97 and self.socket_event['prcssd1'] and self.socket_event['prcssd2']:
                        if event.button == 1:
                            self.socket_event['prcssd2'] = False
                            self.socket_event['lkd2'] = True
                            self.socket_event['prcssd1'] = True
                            self.socket_event['lkd1'] = False
                        if event.button == 3:
                            self.socket_event['angle2'] += 90
                    elif (event.button == 1 and not self.socket_event['prtc2']) or (event.button == 1 and not (853 > mx > 679 and 390 > my > 225)):
                        self.socket_event['prcssd1'] = True
                        self.socket_event['lkd1'] = False
                        self.socket_event['prcssd2'] = True
                        self.socket_event['lkd2'] = False
                    #haste
                    if self.socket_event['prtc'] and not self.socket_event['prtc2'] and not self.socket_event['lkd1']:
                        if self.socket_event['hst'] and not self.socket_event['hst2'] and not self.socket_event['hst3']:
                            if event.button == 1:
                                if 667 > mx > 613 and 236 > my > 161:
                                    self.slide['hst'] = True
                                    #self.slide['hst3'] = False
                        if not self.socket_event['hst'] and self.socket_event['hst2'] and not self.socket_event['hst3']:
                            if event.button == 1:
                                if 645 > mx > 583 and 253 > my > 168:
                                    self.slide['hst'] = False
                                    self.slide['hst3'] = False
                        if not self.socket_event['hst'] and self.socket_event['hst2'] and not self.socket_event['hst3']:
                            if event.button == 1:
                                if 639 > mx > 585 and 187 > my > 154:
                                    self.slide['hst'] = False
                                    self.slide['hst3'] = True
                        if not self.socket_event['hst'] and not self.socket_event['hst2'] and self.socket_event['hst3']:
                            if event.button == 1:
                                if 655 > mx > 588 and 411 > my > 388:
                                    self.slide['hst'] = True
                                    self.slide['hst3'] = False
                        #protecao
                        if self.socket_event['hst3']:
                            if event.button == 1:
                                if 857 > mx > 669 and 449 > my > 419:
                                    self.slide['prtc'] = True
                    if self.socket_event['prtc2'] and not self.socket_event['lkd1']:
                        if event.button == 1:
                            if 902 > mx > 627 and 242 > my > 209:
                                self.slide['prtc'] = False
                    if self.socket_event['angle'] == 360:
                        self.socket_event['angle'] = 0
                    #encaixe
                    if self.socket_event['prtc2'] and self.socket_event['lkd1'] and self.socket_event['hst3']:
                        if event.button == 1:
                            if 853 > mx > 679 and 390 > my > 225 and self.socket_event['angle'] == 180:
                                self.socket_event['intel'][0], self.socket_event['intel'][1] = 679, 225
                                self.socket_event['prcssd1'] = True
                                self.socket_event['lkd1'] = False
                            elif 853 > mx > 679 and 390 > my > 225 and self.socket_event['angle'] != 180:
                                self.socket_event['prcssd1'] = True
                                self.socket_event['lkd1'] = False
                if event.type == MOUSEMOTION or event.type == MOUSEBUTTONUP:
                    #haste
                    if self.slide['hst'] and not self.slide['hst3'] and 618 > mx > 575 and 237 > my > 162:
                        self.socket_event['hst'] = False
                        self.socket_event['hst2'] = True
                    if not self.slide['hst'] and not self.slide['hst3'] and 666 > mx > 604 and 254 > my > 169:
                        self.socket_event['hst'] = True
                        self.socket_event['hst2'] = False
                    if not self.slide['hst'] and self.slide['hst3'] and 655 > mx > 586 and 410 > my > 190:
                        self.socket_event['hst'] = False
                        self.socket_event['hst2'] = False
                        self.socket_event['hst3'] = True
                    if self.slide['hst'] and not self.slide['hst3'] and 640 > mx > 589 and 387 > my > 183:
                        self.socket_event['hst'] = False
                        self.socket_event['hst2'] = True
                        self.socket_event['hst3'] = False
                    #protecao
                    if self.slide['prtc'] and 857 > mx > 669 and 411 > my > 203:
                        self.socket_event['prtc'] = False
                        self.socket_event['prtc2'] = True
                    if not self.slide['prtc'] and 903 > mx > 627 and 447 > my > 245:
                        self.socket_event['prtc'] = True
                        self.socket_event['prtc2'] = False
            if self.socket_event['lkd1']:
                self.game.display.blit(pygame.transform.rotate(processor1, self.socket_event['angle']), (mx - 85, my - 82))
            if self.socket_event['lkd2']:
                self.game.display.blit(pygame.transform.rotate(processador2, self.socket_event['angle2']),(mx - 100, my -100))
        if layer == 30:
            mx, my = pygame.mouse.get_pos()
            self.gamimg_layer = True
            processor1 = pygame.image.load('data/img/worlds/w1/s2/processador_i.png')
            processador2 = pygame.image.load('data/img/worlds/w1/s2/processador_a.png')
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/mb2.png'), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Analise o soquete e coloque o processador adequado", 20, 220, 35)
            if self.socket_event['hst3']:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/haste_6.png'), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/sqt_amd.png'), (0, 0))
            if self.socket_event['hst']:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/haste_4.png'), (0, 0))
            if self.socket_event['hst'] and self.socket_event['amd'] == [379, 218]:
                time.sleep(0.6)
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
                self.socket_event['prcssd1'], self.socket_event['prcssd2'], self.socket_event['prtc'], self.socket_event['prtc2'], self.socket_event['hst'], self.socket_event['hst2'], self.socket_event['hst3'], self.socket_event['lkd1'], self.socket_event['angle'], self.socket_event['intel'], self.socket_event['angle2'], self.socket_event['amd'], self.socket_event['lkd2'] = True, True, True, False, True, False, False, False, 0 ,[4,329], 0, [28, 97], False
                self.slide['hst'], self.slide['hst3'], self.slide['prtc'] = False, False, False
            if self.socket_event['hst2']:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/haste_5.png'), (0, 0))
            if self.socket_event['prcssd2']:
                self.game.display.blit(pygame.transform.rotate(processador2, self.socket_event['angle2']),
                                       (self.socket_event['amd'][0], self.socket_event['amd'][1]))
            if self.socket_event['prcssd1']:
                self.game.display.blit(pygame.transform.rotate(processor1, self.socket_event['angle']),
                                       (self.socket_event['intel'][0], self.socket_event['intel'][1]))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    # processador
                    if 218 > mx > 44 and 494 > my > 329 and self.socket_event['prcssd1'] and self.socket_event['prcssd2']:
                        if event.button == 1:
                            self.socket_event['prcssd1'] = False
                            self.socket_event['lkd1'] = True
                        if event.button == 3:
                            self.socket_event['angle'] += 90
                    elif 234 > mx > 28 and 302 > my > 97 and self.socket_event['prcssd1'] and self.socket_event['prcssd2']:
                        if event.button == 1:
                            self.socket_event['prcssd2'] = False
                            self.socket_event['lkd2'] = True
                            self.socket_event['prcssd1'] = True
                            self.socket_event['lkd1'] = False
                        if event.button == 3:
                            self.socket_event['angle2'] += 90
                    elif event.button == 1 and not (585 > mx > 379 and 423 > my > 218):
                        self.socket_event['prcssd1'] = True
                        self.socket_event['lkd1'] = False
                        self.socket_event['prcssd2'] = True
                        self.socket_event['lkd2'] = False
                    # haste
                    if not self.socket_event['lkd1'] or not self.socket_event['lkd2']:
                        if self.socket_event['hst'] and not self.socket_event['hst2'] and not self.socket_event['hst3']:
                            if event.button == 1:
                                if 609 > mx > 599 and 427 > my > 271:
                                    self.slide['hst'] = True
                                    self.slide['hst3'] = False
                        if not self.socket_event['hst'] and self.socket_event['hst2'] and not self.socket_event['hst3']:
                            if event.button == 1:
                                if 654 > mx > 620 and 410 > my > 336:
                                    self.slide['hst'] = False
                                    self.slide['hst3'] = False
                        if not self.socket_event['hst'] and self.socket_event['hst2'] and 657 > mx > 629 and 407 > my > 383:
                            if event.button == 1:
                                self.slide['hst'] = False
                                self.slide['hst3'] = True
                        if not self.socket_event['hst'] and not self.socket_event['hst2'] and self.socket_event['hst3']:
                            if event.button == 1:
                                if 681 > mx > 625 and 225 > my > 189:
                                    self.slide['hst'] = True
                                    self.slide['hst3'] = False
                    # encaixe
                    if self.socket_event['angle2'] == 360:
                        self.socket_event['angle2'] = 0
                    if self.socket_event['lkd2'] and self.socket_event['hst3']:
                        if event.button == 1:
                            if 585 > mx > 379 and 423 > my > 218 and self.socket_event['angle2'] == 90:
                                self.socket_event['amd'][0], self.socket_event['amd'][1] = 379, 218
                                self.socket_event['prcssd2'] = True
                                self.socket_event['lkd2'] = False
                            elif 585 > mx > 379 and 423 > my > 218 and self.socket_event['angle2'] != 90:
                                self.socket_event['prcssd2'] = True
                                self.socket_event['lkd2'] = False
                if event.type == MOUSEMOTION:
                    # haste
                    if self.slide['hst'] and not self.slide['hst3'] and 710 > mx > 624 and 424 > my > 336:
                        self.socket_event['hst'] = False
                        self.socket_event['hst2'] = True
                    if not self.slide['hst'] and not self.slide['hst3'] and 618 > mx > 509 and 442 > my > 334:
                        self.socket_event['hst'] = True
                    #    self.socket_event['hst3'] = False
                        self.socket_event['hst2'] = False
                    if not self.slide['hst'] and self.slide['hst3'] and 710 > mx > 614 and 340 > my > 159:
                        self.socket_event['hst'] = False
                        self.socket_event['hst2'] = False
                        self.socket_event['hst3'] = True
                    if self.slide['hst'] and not self.slide['hst3'] and 700 > mx > 614 and 423 > my > 215:
                        self.socket_event['hst'] = False
                        self.socket_event['hst2'] = True
                        self.socket_event['hst3'] = False
            if self.socket_event['lkd1']:
                self.game.display.blit(pygame.transform.rotate(processor1, self.socket_event['angle']),
                                       (mx - 85, my - 82))
            if self.socket_event['lkd2']:
                self.game.display.blit(pygame.transform.rotate(processador2, self.socket_event['angle2']),
                                       (mx - 100, my - 100))
        if layer == 31:
            self.draw_very_good()
        if layer == 32:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/conector_cooler.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora você vai ver outro conector da placa-mãe, o conector FAN.", 19, x_text, self.y_text)
            self.game.draw_text("Esse conector é ligado ao cabo dos hardwares chamados de cooler e FAN.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Eles são responsáveis pela dissipação do calor dos componentes internos.", 19, x_text, self.y_text + 40)
        if layer == 33:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/cooler.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("O cooler é um tipo de FAN que pode ser visto como “mini ventilador” ", 19, 243, self.y_text)
            self.game.draw_text("devido ao seu funcionamento com pás em rotação, mas ele também ", 19, 243, self.y_text + 20)
            self.game.draw_text("possui uma parte metálica no seu fundo para facilitar a transferência", 19, 243, self.y_text + 40)
            self.game.draw_text("de calor entre a superfície do processador e ele.", 19, 243, self.y_text + 60)
        if layer == 34:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fans.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Já o FAN é composto apenas da parte da ventoinha.", 19, x_text, self.y_text)
            self.game.draw_text("Um computador pode ter um cooler e vários FANs e, geralmente, nem todos eles ", 19, x_text, self.y_text + 20)
            self.game.draw_text("precisam estar conectados na placa-mãe. Os FANs são utilizados nos", 19, x_text, self.y_text + 40)
            self.game.draw_text("processadores, placas de vídeo e no próprio gabinete. O conector FAN padrão das ", 19, x_text, self.y_text + 60)
            self.game.draw_text("placas-mãe é o para a CPU (processador).", 19, x_text, self.y_text + 80)
        if layer == 35:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/cooler_instalado.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O cooler para processador é específico para dissipar o calor desse ", 19, x_text, self.y_text)
            self.game.draw_text("hardware. Ele é encaixado em cima do processador e a alimentação de ", 19,x_text, self.y_text + 20)
            self.game.draw_text("energia vem do conector FAN próximo ao soquete do processador. ", 19, x_text,self.y_text + 40)
        if layer == 36:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/local_conector_fan.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("As placas-mãe são bem claras quanto aos seus conectores, então", 19,243, self.y_text)
            self.game.draw_text("para encontrar o conector FAN da CPU, basta ler o nome que ", 19, 243,self.y_text + 20)
            self.game.draw_text("está ao lado do encaixe.", 19, 243,self.y_text + 40)
            self.game.draw_text("Esse conector FAN possui normalmente quatro pinos para o ", 19, 243,self.y_text + 60)
            self.game.draw_text("encaixe com o cabo que servem para permitir o controle da ", 19, 243,self.y_text + 80)
            self.game.draw_text("velocidade da ventoinha.", 19, 243,self.y_text + 100)
        if layer == 37:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/conector_fan.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Já os conectores FAN não encaixados na placa-mãe, geralmente utilizados ", 19, 139,
                                self.y_text)
            self.game.draw_text("nos gabinetes, possuem dois ou três pinos, e consequentemente, não há ", 19, 139,
                                self.y_text + 20)
            self.game.draw_text("um controle direto de velocidade.", 19, 139,
                                self.y_text + 40)
        if layer == 38:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/ar.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Ainda sobre os FANs, é importante saber que dentro do computador deve haver um", 19, x_text,self.y_text)
            self.game.draw_text("único sentido de ar, ou seja, se os coolers forem instalados na frente e atrás do ", 19, x_text,self.y_text + 20)
            self.game.draw_text("gabinete, ambos não devem ser encaixados no sentido de saída de ar. Pelo menos ", 19, x_text,self.y_text + 40)
            self.game.draw_text("um deve ter sentido de entrada. O mesmo vale para o cooler dos processadores.", 19, x_text,self.y_text + 60)
        if layer == 39:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/water_cooler.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Atualmente, há um tipo de cooler que não funciona por dissipação ", 19,275, self.y_text)
            self.game.draw_text("a base de ar, mas a base de líquido. Ele é chamado de Water Cooler.",19, 275, self.y_text + 20)
        if layer == 40:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/radiador.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os water coolers possuem um canal por onde percorre um líquido que vai de ", 19, x_text, self.y_text)
            self.game.draw_text("dentro do cooler até um radiador, semelhante ao resfriamento de um carro.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Eles possuem uma dissipação de calor muito maior do que os coolers a ar e são", 19, x_text, self.y_text + 40)
            self.game.draw_text("utilizados geralmente para dar uma maior longevidade aos processadores ", 19, x_text,self.y_text + 60)
            self.game.draw_text("básicos ou para arrefecer o stress causado por altas demandas", 19, x_text,self.y_text + 80)
            self.game.draw_text("de processamento.", 19, x_text,self.y_text + 100)
            self.q = QuestionsTwo(41)
        if layer == 41:
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Identifique o dispositivo de dissipação de ", 22, 253, 35)
            self.game.draw_text("dissipação de calor de acordo com a imagem.", 22, 240, 75)
            self.game.display.blit(pygame.image.load(self.q.image), (0, 0))
            self.game.draw_text("Cooler de processador", 25, 70, 138)
            self.game.draw_text("Water Cooler", 25, 120, 220)
            self.game.draw_text("FAN de Gabinete", 25, 100, 295)
            self.game.draw_text("Ventoinha de Placa de Vídeo", 25, 30, 379)
            self.selected_question()
            pygame.display.update()
        if layer == 42:
            self.draw_very_good()
        if layer == 43:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/coolers.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Para encaixar o cooler do processador na placa-mãe, é preciso identificar o tipo ", 19, x_text,self.y_text)
            self.game.draw_text("de soquete do processador e o tipo de encaixe do cooler. Existem dois tipos ", 19, x_text,self.y_text + 20)
            self.game.draw_text("de encaixe para o cooler: o de pinos de plástico e os de parafuso.", 19, x_text,self.y_text + 40)
        if layer == 44:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler1.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler2.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler3.png'), (215, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler4.png'), (215, 17))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler5.png'), (215, 17))
            if self.clock == 5:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler6.png'), (215, 17))
            if self.clock == 6:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler7.png'), (215, 17))
            if self.clock == 7:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler8.png'), (215, 17))
            if self.clock == 8:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler9.png'), (215, 17))
            if self.clock == 9:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler10.png'), (215, 17))
            pygame.time.wait(70)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/bordas.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Nos coolers de encaixe de pino de plástico, você deve verificar se estão travados ", 19, x_text, self.y_text)
            self.game.draw_text("ou não girando-os e vendo se eles se mexem. Caso estejam destravados, gire-os", 19, x_text, self.y_text + 20)
            self.game.draw_text("para travá-los.", 19, x_text,self.y_text + 40)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 10:
                self.clock = 0
        if layer == 45:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler11.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler12.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler13.png'), (215, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler14.png'), (215, 17))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler15.png'), (215, 17))
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                pygame.mixer.Channel(1).set_volume(0.05)
            if self.clock == 5:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler16.png'), (215, 17))
            if self.clock == 6:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler17.png'), (215, 17))
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                pygame.mixer.Channel(1).set_volume(0.1)
            pygame.time.wait(270)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/bordas.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Posicione os encaixes do cooler nos orifícios da placa-mãe próximos", 19, 255, self.y_text)
            self.game.draw_text("ao soquete e pressione para baixo a diagonal do cooler até ouvir um ", 19, 255, self.y_text + 20)
            self.game.draw_text("som. Depois, pressione a outra diagonal até ouvir o mesmo click.", 19, 255,self.y_text + 40)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 7:
                self.clock = 0
        if layer == 46:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler18.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler19.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler20.png'), (215, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler21.png'), (215, 17))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler22.png'), (215, 17))
            if self.clock == 5:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler23.png'), (215, 17))
            if self.clock == 6:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/cooler24.png'), (215, 17))
            pygame.time.wait(120)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/cooler_1/bordas.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Por fim, conecte o cabo do cooler no conector CPU FAN.", 19, x_text, self.y_text)
            self.game.draw_text("Vamos testar seu conhecimento com base nessas definições:", 19, x_text, self.y_text + 80)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 6:
                self.clock = 0
        if layer == 47:
            mx, my = pygame.mouse.get_pos()
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/q10.png'), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            if self.cooler['clr'] and self.cooler['psi'] == [70,250]:
                if not self.cooler['p1']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino1.png'), self.cooler['psi'])
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino1_g.png'), self.cooler['psi'])
                if not self.cooler['p2']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino2.png'), self.cooler['psi'])
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino2_g.png'), self.cooler['psi'])
                if not self.cooler['p3']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino3.png'), self.cooler['psi'])
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino3_g.png'), self.cooler['psi'])
                if not self.cooler['p4']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino4.png'), self.cooler['psi'])
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino4_g.png'), self.cooler['psi'])
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/cooler1.png'), self.cooler['psi'])
            elif self.cooler['clr'] and self.cooler['psi'] == [481, 182]:
                if not self.cooler['p1']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino1_p.png'), self.cooler['psi'])
                    if self.cooler['s1'][0] < 1:
                        self.cooler['s1'][0] = 2
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                        pygame.mixer.Channel(1).set_volume(0.3)
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino1_g.png'), self.cooler['psi'])
                if not self.cooler['p2']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino2_p.png'), self.cooler['psi'])
                    if self.cooler['s1'][1] < 1:
                        self.cooler['s1'][1] = 2
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                        pygame.mixer.Channel(1).set_volume(0.3)
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino2_g.png'), self.cooler['psi'])
                if not self.cooler['p3']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino3_p.png'), self.cooler['psi'])
                    if self.cooler['s1'][2] < 1:
                        self.cooler['s1'][2] = 2
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                        pygame.mixer.Channel(1).set_volume(0.3)
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino3_g.png'), self.cooler['psi'])
                if not self.cooler['p4']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino4_p.png'), self.cooler['psi'])
                    if self.cooler['s1'][3] < 1:
                        self.cooler['s1'][3] = 2
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                        pygame.mixer.Channel(1).set_volume(0.3)
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino4_g.png'), self.cooler['psi'])
                if not self.cooler['pn'] and not self.cooler['pin'] and self.cooler['clr'] and not self.cooler['p1'] and not self.cooler['p2'] and not self.cooler['p3'] and not self.cooler['p4'] and (self.cooler['psi'] == [481, 182]):
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/cooler2.png'), self.cooler['psi'])
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/cooler1.png'), self.cooler['psi'])
            if self.cooler['pin'] and self.cooler['pn']:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/cooler3.png'), (0, 0))
            self.game.draw_text("Analise o soquete e coloque o processador adequado", 20, 220, 25)
            self.game.draw_text("Em cima do processador há uma pasta térmica. ", 19, 260, 45)
            self.game.draw_text("Falaremos dela nas próximas fases.", 19, 310, 65)
            if self.cooler['pin'] and self.cooler['pn']:
                self.bios[1] +=1
            if self.bios[1] > 25:
                time.sleep(0.6)
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
                self.bios[1] == 0
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 328 > mx > 70 and 508 > my > 250:
                            self.cooler['clr'] = False
                            self.cooler['lkd'] = True
                        if not (742 > mx > 481 and 340 > my > 182) and not (328 > mx > 70 and 508 > my > 250):
                            self.cooler['clr'] = True
                            self.cooler['lkd'] = False
                        if (742 > mx > 481 and 340 > my > 182) and self.cooler['p4'] and self.cooler['p3'] and self.cooler['p2'] and self.cooler['p1']:
                            self.cooler['clr'] = True
                            self.cooler['lkd'] = False
                            self.cooler['psi'][0], self.cooler['psi'][1] = 481, 182
                        if self.cooler['clr'] and not self.cooler['p1'] and not self.cooler['p2'] and not self.cooler['p3'] and not self.cooler['p4'] and (self.cooler['psi'] == [481, 182]) and 517 > mx > 482 and 328 > my > 281:
                            self.cooler['pin'] = True
                    if event.button == 3:
                        if self.cooler['clr'] and ((149 > mx > 114 and 303 > my > 268) or (563 > mx > 528 and 237 > my > 202)):
                            self.cooler['p4'] = not self.cooler['p4']
                        if self.cooler['clr'] and ((296 > mx > 261 and 315 > my > 280) or (703 > mx > 676 and 247 > my > 212)):
                            self.cooler['p3'] = not self.cooler['p3']
                        if self.cooler['clr'] and ((297 > mx > 262 and 478 > my > 443) or (705 > mx > 677 and 416 > my > 381)):
                            self.cooler['p2'] = not self.cooler['p2']
                        if self.cooler['clr'] and ((145 > mx > 110 and 486 > my > 451) or (556 > mx > 521 and 421 > my > 384)):
                            self.cooler['p1'] = not self.cooler['p1']
                if event.type == MOUSEMOTION:
                    if 462 > mx > 427 and 333 > my > 286 and  self.cooler['pin']:
                        self.cooler['pn'] = True
            if self.cooler['lkd']:
                if not self.cooler['p1']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino1.png'), (mx - 125, my - 125))
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino1_g.png'), (mx - 125, my - 125))
                if not self.cooler['p2']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino2.png'), (mx - 125, my - 125))
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino2_g.png'), (mx - 125, my - 125))
                if not self.cooler['p3']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino3.png'), (mx - 125, my - 125))
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino3_g.png'), (mx - 125, my - 125))
                if not self.cooler['p4']:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino4.png'), (mx - 125, my - 125))
                else:
                    self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/pino4_g.png'), (mx - 125, my - 125))
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/cooler1.png'), (mx - 125, my - 125))
        if layer == 48:
            self.draw_very_good()
        if layer == 49:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/slot.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora vamos ver os encaixes slots.", 19, x_text, self.y_text)
            self.game.draw_text("Como dito anteriormente, os slots são os locais para se encaixar as ", 19, x_text, self.y_text + 20)
            self.game.draw_text("memórias RAM e placas adicionais, como placa de rede e placa de vídeo.", 19, x_text, self.y_text + 40)
        if layer == 50:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/dimm.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Os slots para a memória RAM de computadores são chamados de barramentos e o ", 19, x_text, self.y_text)
            self.game.draw_text("módulo de slot atual é o módulo de memória em linha dupla, chamado de dimm.", 19, x_text, self.y_text + 20)
        if layer == 51:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/ddrs.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("O dimm dá suporte a diversas gerações de memória RAM, como ddr,", 19, 275, self.y_text)
            self.game.draw_text("ddr2, ddr3 e ddr4 nos modelos atuais (falaremos sobre as", 19, 275, self.y_text + 20)
            self.game.draw_text("memórias RAM na próxima fase).", 19, 275, self.y_text + 40)
        if layer == 52:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/encaixe_DDRs.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("É importante saber que há uma diferença do slot de memória para cada geração, ", 19, x_text, self.y_text)
            self.game.draw_text("então não é possível encaixar uma memória dd3 em um slot para memórias ", 19, x_text, self.y_text + 20)
            self.game.draw_text("ddr4 e funcionar.", 19, x_text, self.y_text + 40)
        if layer == 53:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/ddr5.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("As memórias mais presentes no mercado atual são as da versão ddr4, mas ainda ", 19, x_text, self.y_text)
            self.game.draw_text("há memórias do tipo ddr3 e nos próximos anos o mercado comercializará as", 19, x_text, self.y_text + 20)
            self.game.draw_text("memórias ddr5, por isso é importante que você saiba diferenciar um slot ddr4 de ", 19, x_text, self.y_text + 40)
            self.game.draw_text("ddr3. ", 19, x_text, self.y_text + 60)
        if layer == 54:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/dual_channel_vs_single.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Agora vamos ver como encaixar a memória RAM no slot.", 19, 245, self.y_text)
            self.game.draw_text("Falaremos das funcionalidades da memória RAM na próxima fase, mas", 19, 245,self.y_text + 20)
            self.game.draw_text("para a instalação da memória na placa-mãe, é preciso saber que elas", 19, 245, self.y_text + 40)
            self.game.draw_text("podem ser colocadas em par (processo chamado de dual channel) ou", 19, 245, self.y_text + 60)
            self.game.draw_text("singularmente (processo chamado de single channel).", 19, 245, self.y_text + 80)
        if layer == 55:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/mb_slot.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("O encaixe da memória é diferente de acordo com o modo de como ela será", 19, x_text, self.y_text)
            self.game.draw_text("colocada e isso dependerá da placa-mãe.", 19, x_text,self.y_text + 20)
        if layer == 56:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/local_ddr3.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Primeiro, verifique o slot de memória que a placa-mãe possui para depois", 19, x_text, self.y_text)
            self.game.draw_text("adquirir ou selecionar a memória. Caso já tenha a memória, procure adquirir ", 19, x_text,self.y_text + 20)
            self.game.draw_text("uma placa-mãe com o respectivo slot.", 19, x_text,self.y_text + 40)
        if layer == 57:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/segurando_RAM.png'), (215, 17))
            self.base_layer(layer)
            self.game.draw_text("Depois de selecionar a memória RAM, manuseie-a com as duas", 19, 260, self.y_text)
            self.game.draw_text("mãos segurando nas pontas de cima dela e verifique o sentido ", 19, 260,self.y_text + 20)
            self.game.draw_text("do dente da memória.", 19, 260,self.y_text + 40)
        if layer == 58:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/mb_slot.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Caso você tenha dificuldade em encontrar qual o slot para colocar a memória RAM, ", 19, x_text, self.y_text)
            self.game.draw_text("basta perceber quais são os slots de mesmo tamanho em que estão juntos em par", 19, x_text,self.y_text + 20)
            self.game.draw_text("um com o outro paralelamente.", 19, x_text,self.y_text + 40)
        if layer == 59:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/local_ddr3.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Também é possível encontrar na placas-mãe, ao lado do nome dimm (DDR), o nome ", 19, x_text, self.y_text)
            self.game.draw_text("do slot (geralmente são chamados de 1 e 2 ou A1, A2, B1 e B2).", 19, x_text,self.y_text + 20)
        if layer == 60:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/dual_channel.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Esses nomes são importantes, pois, caso as memórias sejam colocadas", 19, x_text, self.y_text)
            self.game.draw_text("em Dual Channel e houverem 4 slots, elas devem ser colocadas ", 19, x_text,self.y_text + 20)
            self.game.draw_text("em uma ordem de acordo com as especificações da placa-mãe. ", 19, x_text,self.y_text + 40)
            self.game.draw_text("Geralmente é escolhido o padrão colocando uma memória no slot", 19, x_text,self.y_text + 60)
            self.game.draw_text("A1 e outra no slot B1 ou uma no slot A2 e a outra, no B2.", 19, x_text,self.y_text + 80)
        if layer == 61:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot1.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot2.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot3.png'), (215, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot4.png'), (215, 17))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot5.png'), (215, 17))
            if self.clock == 5:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot6.png'), (215, 17))
            if self.clock == 6:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot7.png'), (215, 17))
            if self.clock == 7:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot8.png'), (215, 17))
            if self.clock == 8:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot9.png'), (215, 17))
            pygame.time.wait(120)
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Voltando para a instalação em si, abra as chaves do slot que ficam ", 19, x_text, self.y_text)
            self.game.draw_text("nas suas extremidades (às vezes pode haver apenas uma chave) puxando-as ", 19, x_text,self.y_text + 20)
            self.game.draw_text("no sentido defora do slot.", 19, x_text,self.y_text + 40)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 9:
                self.clock = 0
        if layer == 62:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/fundo_mb.png'), (215, 17))
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot10.png'), (215, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot11.png'), (215, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/slot12.png'), (215, 17))
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                pygame.mixer.Channel(1).set_volume(0.05)
            pygame.time.wait(120)
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Agora, coloque a memória RAM no slot e pressione-a para baixo em", 21, x_text, self.y_text)
            self.game.draw_text("cada uma das extremidades até fazer um click.", 21, x_text,self.y_text + 20)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 3:
                self.clock = 0
        if layer == 63:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/dual_channel.png'), (215, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Caso o modo de instalação da memória seja em dual Channel, ", 19, x_text, self.y_text)
            self.game.draw_text("basta seguir os mesmos passos no slot adequado.", 19, x_text, self.y_text + 20)
            self.game.draw_text("Agora vamos testar seus conhecimentos adquiridos.", 19, x_text, self.y_text + 80)
        if layer == 64:
            mx, my = pygame.mouse.get_pos()
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/q11.png'), (0, 0))
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
                #self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/anim/slot/RAMDDR3.png'), (23, 104))
            if self.slot['psi1'] == [474, 211] or self.slot['psi1'] == [474, 238] or self.slot['psi1'] == [474, 292] or self.slot['psi1'] == [474, 320]:
                pygame.time.delay(800)
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
            if not self.slot['ddr4']:
                self.slot['ddr4'] = True
                self.slot['lkd'][1] = False
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 113 > mx > 23 and 504 > my > 104:
                                self.slot['ddr3'] = not self.slot['ddr3']
                                self.slot['lkd'][0] = True
                        if not (113 > mx > 23 and 504 > my > 104) and self.slot['lkd'][0] and ((self.slot['slt1'][1] and self.slot['slt1'][2]) or (self.slot['slt2'][1] and self.slot['slt2'][2]) or (self.slot['slt3'][1] and self.slot['slt3'][2]) or (self.slot['slt4'][1] and self.slot['slt4'][2])):
                            self.slot['ddr3'] = True
                            self.slot['lkd'][0] = False
                        if 216 > mx > 126 and 504 > my > 104:
                            self.slot['ddr4'] = not self.slot['ddr4']
                            self.slot['lkd'][1] = True
                        if not (216 > mx > 126 and 504 > my > 104) and self.slot['lkd'][1] and not (877 > mx > 477 and 305 > (my - 90) > 281):
                            self.slot['ddr4'] = True
                            self.slot['lkd'][1] = False
                        if self.slot['ddr3'] and self.slot['ddr4']:
                            if 475 > mx > 448 and 303 > my > 276:
                                self.slt['slt1'][0] = False
                                self.slt['slt1'][1] = True
                            if 447 > mx > 420 and 304 > my > 277:
                                self.slt['slt1'][0] = True
                                self.slt['slt1'][1] = False
                            if 475 > mx > 448 and 333 > my > 306:
                                self.slt['slt2'][0] = False
                                self.slt['slt2'][1] = True
                            if 447 > mx > 420 and 334 > my > 307:
                                self.slt['slt2'][0] = True
                                self.slt['slt2'][1] = False
                            if 475 > mx > 448 and 383 > my > 356:
                                self.slt['slt3'][0] = False
                                self.slt['slt3'][1] = True
                            if 447 > mx > 420 and 383 > my > 356:
                                self.slt['slt3'][0] = True
                                self.slt['slt3'][1] = False
                            if 475 > mx > 448 and 407 > my > 386:
                                self.slt['slt4'][0] = False
                                self.slt['slt4'][1] = True
                            if 447 > mx > 420 and 407 > my > 386:
                                self.slt['slt4'][0] = True
                                self.slt['slt4'][1] = False
                            if 905 > mx > 878 and 303 > my > 276:
                                self.slt['slt1'][0] = False
                                self.slt['slt1'][2] = True
                            if 935 > mx > 908 and 304 > my > 277:
                                self.slt['slt1'][0] = True
                                self.slt['slt1'][2] = False
                            if 905 > mx > 878 and 333 > my > 306:
                                self.slt['slt2'][0] = False
                                self.slt['slt2'][2] = True
                            if 935 > mx > 908 and 334 > my > 307:
                                self.slt['slt2'][0] = True
                                self.slt['slt2'][2] = False
                            if 905 > mx > 878 and 383 > my > 356:
                                self.slt['slt3'][0] = False
                                self.slt['slt3'][2] = True
                            if 935 > mx > 908 and 383 > my > 356:
                                self.slt['slt3'][0] = True
                                self.slt['slt3'][2] = False
                            if 905 > mx > 878 and 407 > my > 386:
                                self.slt['slt4'][0] = False
                                self.slt['slt4'][2] = True
                            if 935 > mx > 908 and 407 > my > 386:
                                self.slt['slt4'][0] = True
                                self.slt['slt4'][2] = False
                        if 876 > mx + 200 > 477 and 305 > my + 45 > 281 and not self.slot['lkd'][0] and not self.slot['psi1'] == [474, 234] and not self.slot['psi1'] == [474, 288] and not self.slot['psi1'] == [474, 316] and not self.slot['psi1'] == [474, 238] and not self.slot['psi1'] == [474, 292] and not self.slot['psi1'] == [474, 320]:
                            if self.slot['slt1'][1] and self.slot['slt1'][2]:
                                self.slot['psi1'] = [474, 207]
                                self.slot['ddr3'] = True
                        if 876 > mx + 200 > 477 and 334 > my + 45 > 310 and not self.slot['lkd'][0] and not self.slot['psi1'] == [474, 207] and not self.slot['psi1'] == [474, 288] and not self.slot['psi1'] == [474, 316] and not self.slot['psi1'] == [474, 211] and not self.slot['psi1'] == [474, 292] and not self.slot['psi1'] == [474, 320]:
                            if self.slot['slt2'][1] and self.slot['slt2'][2]:
                                self.slot['psi1'] = [474, 234]
                                self.slot['ddr3'] = True
                        if 876 > mx + 200 > 477 and 384 > my + 45 > 360 and not self.slot['lkd'][0] and not self.slot['psi1'] == [474, 234] and not self.slot['psi1'] == [474, 207] and not self.slot['psi1'] == [474, 316] and not self.slot['psi1'] == [474, 238] and not self.slot['psi1'] == [474, 211] and not self.slot['psi1'] == [474, 320]:
                            if self.slot['slt3'][1] and self.slot['slt3'][2]:
                                self.slot['psi1'] = [474, 288]
                                self.slot['ddr3'] = True
                        if 876 > mx + 200 > 477 and 414 > my + 45 > 392 and not self.slot['lkd'][0] and not self.slot['psi1'] == [474, 234] and not self.slot['psi1'] == [474, 288] and not self.slot['psi1'] == [474, 207] and not self.slot['psi1'] == [474, 238] and not self.slot['psi1'] == [474, 292] and not self.slot['psi1'] == [474, 320]:
                            if self.slot['slt4'][1] and self.slot['slt4'][2]:
                                self.slot['psi1'] = [474, 316]
                                self.slot['ddr3'] = True
                        if self.slot['psi1'] == [474, 207] and not self.slt['slt1'][3] and not self.slot['lkd'][0] and not self.slot['psi1'] == [474, 238] and not self.slot['psi1'] == [474, 292] and not self.slot['psi1'] == [474, 320]:
                            self.slt['slt1'][3] = True
                            self.slot['lkd'][0] = True
                        if self.slot['psi1'] == [474, 234] and not self.slt['slt2'][3] and not self.slot['lkd'][0] and not self.slot['psi1'] == [474, 207] and not self.slot['psi1'] == [474, 288] and not self.slot['psi1'] == [474, 316] and not self.slot['psi1'] == [474, 211] and not self.slot['psi1'] == [474, 292] and not self.slot['psi1'] == [474, 320]:
                            self.slt['slt2'][3] = True
                            self.slot['lkd'][0] = True
                        if self.slot['psi1'] == [474, 288] and not self.slt['slt3'][3] and not self.slot['lkd'][0] and not self.slot['psi1'] == [474, 234] and not self.slot['psi1'] == [474, 207] and not self.slot['psi1'] == [474, 316] and not self.slot['psi1'] == [474, 238] and not self.slot['psi1'] == [474, 211] and not self.slot['psi1'] == [474, 320]:
                            self.slt['slt3'][3] = True
                            self.slot['lkd'][0] = True
                        if self.slot['psi1'] == [474, 316] and not self.slt['slt3'][3] and not self.slot['lkd'][0] and not self.slot['psi1'] == [474, 234] and not self.slot['psi1'] == [474, 288] and not self.slot['psi1'] == [474, 207] and not self.slot['psi1'] == [474, 238] and not self.slot['psi1'] == [474, 292] and not self.slot['psi1'] == [474, 320]:
                            self.slt['slt4'][3] = True
                            self.slot['lkd'][0] = True
                if event.type == MOUSEMOTION:
                    if not self.slt['slt1'][0] and self.slt['slt1'][1]:
                        if 447 > mx > 383 and 303 > my > 276:
                            self.slot['slt1'][0] = False
                            self.slot['slt1'][1] = True
                    if self.slt['slt1'][0] and not self.slt['slt1'][1]:
                        if 513 > mx > 448 and 314 > my > 277:
                            self.slot['slt1'][0] = True
                            self.slot['slt1'][1] = False
                    if not self.slt['slt2'][0] and self.slt['slt2'][1]:
                        if 447 > mx > 383 and 332 > my > 305:
                            self.slot['slt2'][0] = False
                            self.slot['slt2'][1] = True
                    if self.slt['slt2'][0] and not self.slt['slt2'][1]:
                        if 514 > mx > 450 and 334 > my > 307:
                            self.slot['slt2'][0] = True
                            self.slot['slt2'][1] = False
                    if not self.slt['slt3'][0] and self.slt['slt3'][1]:
                        if 447 > mx > 382 and 383 > my > 356:
                            self.slot['slt3'][0] = False
                            self.slot['slt3'][1] = True
                    if self.slt['slt3'][0] and not self.slt['slt3'][1]:
                        if 514 > mx > 450 and 376 > my > 359:
                            self.slot['slt3'][0] = True
                            self.slot['slt3'][1] = False
                    if not self.slt['slt4'][0] and self.slt['slt4'][1]:
                        if 447 > mx > 382 and 413 > my > 386:
                            self.slot['slt4'][0] = False
                            self.slot['slt4'][1] = True
                    if self.slt['slt4'][0] and not self.slt['slt4'][1]:
                        if 515 > mx > 451 and 413 > my > 386:
                            self.slot['slt4'][0] = True
                            self.slot['slt4'][1] = False
                    if not self.slt['slt1'][0] and self.slt['slt1'][2]:
                        if 969 > mx > 905 and 303 > my > 276:
                            self.slot['slt1'][0] = False
                            self.slot['slt1'][2] = True
                    if self.slt['slt1'][0] and not self.slt['slt1'][2]:
                        if 905 > mx > 841 and 314 > my > 277:
                            self.slot['slt1'][0] = True
                            self.slot['slt1'][2] = False
                    if not self.slt['slt2'][0] and self.slt['slt2'][2]:
                        if 969 > mx > 905 and 332 > my > 305:
                            self.slot['slt2'][0] = False
                            self.slot['slt2'][2] = True
                    if self.slt['slt2'][0] and not self.slt['slt2'][2]:
                        if 905 > mx > 841 and 334 > my > 307:
                            self.slot['slt2'][0] = True
                            self.slot['slt2'][2] = False
                    if not self.slt['slt3'][0] and self.slt['slt3'][2]:
                        if 969 > mx > 905 and 383 > my > 356:
                            self.slot['slt3'][0] = False
                            self.slot['slt3'][2] = True
                    if self.slt['slt3'][0] and not self.slt['slt3'][2]:
                        if 905 > mx > 841 and 376 > my > 359:
                            self.slot['slt3'][0] = True
                            self.slot['slt3'][2] = False
                    if not self.slt['slt4'][0] and self.slt['slt4'][2]:
                        if 969 > mx > 905 and 413 > my > 386:
                            self.slot['slt4'][0] = False
                            self.slot['slt4'][2] = True
                    if self.slt['slt4'][0] and not self.slt['slt4'][2]:
                        if 905 > mx > 841 and 413 > my > 386:
                            self.slot['slt4'][0] = True
                            self.slot['slt4'][2] = False
                    if self.slt['slt1'][3] and 874 > mx > 474 and 332 > my > 297:
                        self.slot['psi1'] = [474, 211]
                        if self.slot['psi1'] == [474, 211]:
                            self.slot['slt1'][2], self.slot['slt1'][1] = False, False
                            self.slot['slt1'][0] = True
                        self.slt['slt1'][3] = False
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                        pygame.mixer.Channel(1).set_volume(0.05)
                    if self.slt['slt2'][3] and 874 > mx > 474 and 359 > my > 324:
                        self.slot['psi1'] = [474, 238]
                        if self.slot['psi1'] == [474, 238]:
                            self.slot['slt2'][2], self.slot['slt2'][1] = False, False
                            self.slot['slt2'][0] = True
                        self.slt['slt2'][3] = False
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                        pygame.mixer.Channel(1).set_volume(0.05)
                    if self.slt['slt3'][3] and 874 > mx > 474 and 410 > my > 375 and not self.slot['psi1'] == [474, 316]:
                        self.slot['slt3'][2], self.slot['slt3'][1] = False, False
                        self.slot['slt3'][0] = True
                        self.slot['psi1'] = [474, 292]
                        if self.slot['psi1'] == [474, 292]:
                            self.slot['slt3'][2], self.slot['slt3'][1] = False, False
                            self.slot['slt3'][0] = True
                        self.slt['slt3'][3] = False
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                        pygame.mixer.Channel(1).set_volume(0.05)
                    if self.slt['slt4'][3] and 874 > mx > 474 and 439 > my > 404:
                        self.slot['slt4'][2], self.slot['slt4'][1] = False, False
                        self.slot['slt4'][0] = True
                        self.slot['psi1'] = [474, 320]
                        if self.slot['psi1'] == [474, 320]:
                            self.slot['slt4'][2], self.slot['slt4'][1] = False, False
                            self.slot['slt4'][0] = True
                        self.slt['slt4'][3] = False
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/click.mp3'))
                        pygame.mixer.Channel(1).set_volume(0.05)
            if self.slot['slt1'][0]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s11.png'), (0, 0))
            if self.slot['slt1'][1] and not self.slot['slt1'][2]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s12.png'), (0, 0))
            if self.slot['slt1'][2] and not self.slot['slt1'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s13.png'), (0, 0))
            if self.slot['slt1'][1] and self.slot['slt1'][2]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s14.png'), (0, 0))
            if self.slot['slt2'][0]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s21.png'), (0, 0))
            if self.slot['slt2'][1] and not self.slot['slt2'][2]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s22.png'), (0, 0))
            if self.slot['slt2'][2] and not self.slot['slt2'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s23.png'), (0, 0))
            if self.slot['slt2'][1] and self.slot['slt2'][2]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s24.png'), (0, 0))
            if self.slot['slt3'][0]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s31.png'), (0, 0))
            if self.slot['slt3'][1] and not self.slot['slt3'][2]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s32.png'), (0, 0))
            if self.slot['slt3'][2] and not self.slot['slt3'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s33.png'), (0, 0))
            if self.slot['slt3'][1] and self.slot['slt3'][2]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s34.png'), (0, 0))
            if self.slot['slt4'][0]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s41.png'), (0, 0))
            if self.slot['slt4'][1] and not self.slot['slt4'][2]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s42.png'), (0, 0))
            if self.slot['slt4'][2] and not self.slot['slt4'][1]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s43.png'), (0, 0))
            if self.slot['slt4'][1] and self.slot['slt4'][2]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s44.png'), (0, 0))
            if self.slot['ddr3']:
                if self.slot['psi1'] == [23, 104]:
                    self.slot['angle1'] = 90
                self.game.display.blit(
                    pygame.transform.rotate(pygame.image.load('data/img/worlds/w1/s2/anim/slot/RAMDDR3.png'),
                                            self.slot['angle1']), self.slot['psi1'])
            else:
                self.slot['angle1'] = 0
                self.game.display.blit(
                    pygame.transform.rotate(pygame.image.load('data/img/worlds/w1/s2/anim/slot/RAMDDR3.png'),
                                            self.slot['angle1']), (mx - 200, my - 45))
            if self.slot['ddr4']:
                if self.slot['psi2'] == [126, 104]:
                    self.slot['angle2'] = 90
                self.game.display.blit(
                    pygame.transform.rotate(pygame.image.load('data/img/worlds/w1/s2/anim/slot/RAMDDR4.png'),
                                            self.slot['angle2']), self.slot['psi2'])
            else:
                self.slot['angle2'] = 0
                self.game.display.blit(
                    pygame.transform.rotate(pygame.image.load('data/img/worlds/w1/s2/anim/slot/RAMDDR4.png'),
                                            self.slot['angle2']), (mx - 200, my - 45))
            if self.slot['psi1'][1] == 211:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s15.png'), (0, 0))
            if self.slot['psi1'][1] == 238:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s25.png'), (0, 0))
            if self.slot['psi1'][1] == 292:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s35.png'), (0, 0))
            if self.slot['psi1'][1] == 320:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/s45.png'), (0, 0))
            self.game.draw_text("Verifique a geração de memória RAM compatível com", 20, 220, 25)
            self.game.draw_text("a placa-mãe e instale aquela em single channel.", 19, 260, 45)
        if layer == 65:
            self.draw_very_good()
        if layer == 66:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/marcas_BIOS.png'), (275, 17))
            self.base_layer(layer)
            self.game.draw_text("Um outro elemento importante da placa-mãe é o chip BIOS.", 19,265, self.y_text)
        if layer == 67:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/BIOS.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("Você já viu um pouco sobre a BIOS durante a fase 1. Podemos ver", 19,x_text, self.y_text)
            self.game.draw_text("esse firmware atuando quando ligamos o computador, pois é o primeiro ", 19,x_text, self.y_text + 20)
            self.game.draw_text("software a ser iniciado. As informações desse software que são mostradas", 19,x_text, self.y_text + 40)
            self.game.draw_text("no monitor do computador são extraídas desse chip Bios.", 19,x_text, self.y_text + 60)
        if layer == 68:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/BIOS.png'), (275, 17))
            self.base_layer(layer)
            x_text = self.margin_left if self.margin_reg == "left" else self.margin_right
            self.game.draw_text("É importante sempre atualizar as versões da BIOS da placa-mãe quando ", 19,x_text, self.y_text)
            self.game.draw_text("disponíveis e com isso, essas atualizações substituem as versões ", 19,x_text, self.y_text + 20)
            self.game.draw_text("anteriores presentes no chip.", 19,x_text, self.y_text + 40)
        if layer == 69:
            if self.clock == 0:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/lig1.png'), (275, 17))
            if self.clock == 1:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/lig2.png'), (275, 17))
            if self.clock == 2:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/lig3.png'), (275, 17))
            if self.clock == 3:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/keyboard1.png'), (0, 0))
            if self.clock == 4:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/keyboard2.png'), (0, 0))
            if self.clock == 5:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/keyboard3.png'), (0, 0))
            if self.clock == 6:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/lig4.png'), (275, 17))
            if self.clock == 7:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/lig4.png'), (275, 17))
            if self.clock == 8:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/lig4.png'), (275, 17))
            if self.clock == 9:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/lig4.png'), (275, 17))
            pygame.time.wait(300)
            self.base_layer(layer)
            self.game.draw_text("Para acessar o software BIOS, enquanto o computador estiver ", 19, 255, self.y_text)
            self.game.draw_text("ligando, pressione uma das teclas especiais até aparecer a interface", 19, 255, self.y_text + 20)
            self.game.draw_text("do firmware.", 19, 255,self.y_text + 40)
            self.game.draw_text("Lembrando que os computadores mais novos acionam o firmware", 19, 255,self.y_text + 60)
            self.game.draw_text("UEFI como modo normal em vez da BIOS.", 19, 255,self.y_text + 80)
            self.game.draw_text("Vamos testar seus conhecimentos adquiridos.", 19, 255,self.y_text + 100)
            self.blit_screen()
            self.clock += 1
            if self.clock >= 10:
                self.clock = 0
        if layer == 70:
            mx, my = pygame.mouse.get_pos()
            self.gamimg_layer = True
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/up_bar.png'), (0, 0))
            self.game.draw_text("Entre na interface do firmware do computador.", 20, 260, 35)
            timer = 10 - int(self.count_click / 20)
            self.game.draw_text(f"TEMPO: {timer}", 20, 440, 65)
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/ligar_computador.png'), (320, 115))
            if self.click_event:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/bios_ligando.png'), (320, 115))
                self.count_click += 1
            if self.bios[0]:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/bios_ligada.png'), (320, 115))
                self.bios[1] += 1
            if not self.click_event:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s1/logan_ligar_computador.png'), (320, 115))
                self.game.draw_text("-Ligue o computador por aqui.", 17, 585, 130)
            if self.count_click > 220:
                self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/so_ligando.png'), (320, 115))
                self.click_event = False
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/wrong_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.count_click = 0
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/keyboard.png'), (0, 0))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if 496 > mx > 473 and 256 > my > 237:
                        if event.button == 1:
                            self.click_event = True
                    if self.click_event:
                        if 574 > mx > 547 and 347 > my > 323:
                            self.click_event = False
                            self.bios[0] = True
            if self.bios[1] > 0:
                self.bios[1] += 1
            if self.bios[1] > 15:
                self.score.alternatives(self.answer[str(self.layers[len(self.layers) - 1])], 1)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('data/aud/correct_answer.mp3'))
                pygame.mixer.Channel(1).set_volume(0.04)
                self.i += 1
                self.layers.append(self.i)
                self.gamimg_layer = False
                self.game.reset_keys()
                self.state = '1'
        if layer == 71:
            self.draw_very_good()
        if layer == 72:
            self.game.display.blit(pygame.image.load('data/img/worlds/w1/s2/end.png'), (0, 0))
            text = 'FasesWone='
            a = open('c:\ProtTech\data\data.txt', 'r')
            b = a.read()
            a2 = open('c:\ProtTech\data\data.txt', 'rt+')
            s = a2.readlines()[2]
            a2.close()
            if (text + "True,True,False") in s:
                b = b.replace(text + "True,True,False", text + "True,True,True", 1)
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
            