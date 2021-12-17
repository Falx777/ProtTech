from menu import *
'''
class Cursor():
    def __init__(self, game):
        pass


    def move_cursor(m):
        if m.game.DOWN_KEY:
            if m.state == "começar":
                m.bx, m.by = m.area['2']['x'], m.area['2']['y']
                m.state = "opções"
            elif m.state == "opções":
                m.bx, m.by = m.area['3']['x'], m.area['3']['y']
                m.state = "sobre"
            elif m.state == "sobre":
                m.bx, m.by = m.area['1']['x'], m.area['1']['y']
                m.state = "começar"
        if m.game.UP_KEY:
            if m.state == "começar":
                m.bx, m.by = m.area['3']['x'], m.area['3']['y']
                m.state = "sobre"
            elif m.state == "opções":
                m.bx, m.by = m.area['1']['x'], m.area['1']['y']
                m.state = "começar"
            elif m.state == "sobre":
                m.bx, m.by = m.area['2']['x'], m.area['2']['y']
                m.state = "opções"

'''
visual_vol = ['I', 'I', 'I', 'I']
vol = ''
for v in visual_vol:
    vol += " " + v







'''
class Main_Menu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "começar"
        self.start_x, self.start_y = 598, self.mid_h - 204
        self.option_x, self.option_y = 598, self.mid_h - 64
        self.credits_x, self.credits_y = 598, self.mid_h + 76
        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)

    def move(self, bx, by, area_x, area_y):
        coordenates = []
        return bx, by = area_x, area_y

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == "começar":
                self.bx, self.by = self.option_x, self.option_y
                self.state = "opções"
            elif self.state == "opções":
                self.bx, self.by = self.credits_x, self.credits_y
                self.state = "sobre"
            elif self.state == "sobre":
                self.bx, self.by = self.start_x, self.start_y
                self.state = "começar"
        if self.game.UP_KEY:
            if self.state == "começar":
                self.bx, self.by = self.credits_x, self.credits_y
                self.state = "sobre"
            elif self.state == "opções":
                self.bx, self.by = self.start_x, self.start_y
                self.state = "começar"
            elif self.state == "sobre":
                self.bx, self.by = self.option_x, self.option_y
                self.state = "opções"
'''

area = dict()
area['start'] = {'x': 598, 'y': - 204}
        #self.start_x, self.start_y = 598, self.mid_h - 204
area['option'] ={'x': 598, 'y': - 64}
        #self.option_x, self.option_y = 598, self.mid_h - 64
area['credits'] = {'x': 598, 'y': + 76}
        #self.credits_x, self.credits_y = 598, self.mid_h + 76

