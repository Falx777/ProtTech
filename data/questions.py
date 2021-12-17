
class Questions():
    def __init__(self, layer):
        if layer == 0:
            pass
        if layer == 18:
            self.position = {'1': [[18, 120], [386, 173], False], '2': [[18, 195], [386, 255], False],
                        '3': [[18, 274], [386, 332], False], '4': [[18, 347], [386, 441], False],
                        '5': [[18, 429], [386, 484], False], '6': [[488, 120], [855, 173], False],
                        '7': [[488, 196], [855, 255], False], '8': [[488, 274], [855, 332], False],
                        '9': [[488, 351], [855, 411], False], '10': [[488, 429], [855, 484], False]}
            self.answ = [[1, 7], [2, 10], [3, 6], [4, 9], [5, 8]]
            self.feed = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
            self.image = 'data/img/worlds/w1/s1/q7.png'
            self.bar = 'data/img/bar_5.png'
            self.selected_bar = 'data/img/bar_5_g.png'
            self.offset = [-192, -36]
        if layer == 25:
            self.position = {'1': [[138, 161], [388, 240], False], '2': [[138, 275], [388, 355], False],
                             '3': [[138, 382], [388, 465], False], '4': [[538, 161], [787, 239], False],
                             '5': [[538, 275], [787, 349], False], '6': [[538, 387], [787, 464], False]}
            self.answ = [[1, 6], [2, 4], [3, 5]]
            self.feed = [[0, 0], [0, 0], [0, 0]]
            self.image = 'data/img/worlds/w1/s1/q8.png'
            self.bar = 'data/img/Bar.png'
            self.selected_bar = 'data/img/Bar_g.png'
            self.offset = [-142, -52]
        if layer == 35:
            self.position = {'1': [[18, 274], [386, 332], False], '2': [[18, 347], [386, 441], False],
                             '3': [[18, 429], [386, 484], False], '4': [[488, 274], [855, 332], False],
                             '5': [[488, 351], [855, 411], False], '6': [[488, 429], [855, 484], False],
                             '7': [[18, 155], [107, 223], False], '8': [[165, 155], [254, 223], False],
                             '9': [[312, 155], [401, 223], False], '10': [[459, 155], [548, 223], False],
                             '11': [[606, 155], [695, 223], False], '12': [[753, 155], [842, 223], False]}
            self.answ = [[1, 9], [2, 11], [3, 7], [4, 12], [5, 8], [6, 10]]
            self.feed = [[0, 0], [0, 0], [0, 0], [0, 0],[0, 0], [0, 0]]
            self.image = 'data/img/worlds/w1/s1/q9.png'
            self.bar = 'data/img/Squared_bar.png'
            self.selected_bar = 'data/img/Squared_bar_g.png'
            self.offset = [-48, -38]


class QuestionsTwo():
    def __init__(self, layer):
        if layer == 0:
            pass
        if layer == 8:
            self.position = {'1': [[18, 120], [386, 173], False], '2': [[18, 195], [386, 255], False],
                        '3': [[18, 274], [386, 332], False], '4': [[18, 347], [386, 441], False],
                        '5': [[488, 120], [855, 173], False], '6': [[488, 196], [855, 255], False],
                        '7': [[488, 274], [855, 332], False], '8': [[488, 351], [855, 411], False]}
            self.answ = [[1, 6], [2, 5], [3, 8], [4, 7]]
            self.feed = [[0, 0], [0, 0], [0, 0], [0, 0]]
            self.image = 'data/img/worlds/w1/s2/q8.png'
            self.bar = 'data/img/bar_5.png'
            self.selected_bar = 'data/img/bar_5_g.png'
            self.offset = [-192, -36]
        if layer == 41:
            self.position = {'1': [[18, 120], [386, 173], False], '2': [[18, 195], [386, 255], False],
                             '3': [[18, 274], [386, 332], False], '4': [[18, 347], [386, 441], False],
                             '5': [[496, 142], [627, 254], False], '6': [[496, 290], [627, 402], False],
                             '7': [[734, 142], [861, 254], False], '8': [[734, 290], [861, 402], False]}
            self.answ = [[1, 5], [2, 8], [3, 7], [4, 6]]
            self.feed = [[0, 0], [0, 0], [0, 0], [0, 0]]
            self.image = 'data/img/worlds/w1/s2/q9.png'
            self.bar = 'data/img/bar_3.png'
            self.selected_bar = 'data/img/bar_3_g.png'
            self.offset = [-65, -55]


class QuestionsThree():
    def __init__(self, layer):
        r = 0
        if layer == 0:
            pass
        if layer == 48:
            self.position = {'1': [[20, 198], [400, 226], False], '2': [[20, 276], [400, 344], False],
                             '3': [[20, 354], [400, 422], False], '4': [[490, 198], [870, 266], False],
                             '5': [[490, 276], [870, 344], False], '6': [[490, 354], [870, 422], False],
                             '7': [[253, 432], [633, 500], False], '8': [[256, 124], [636, 192], False]}
            self.answ = [[1, 0], [2, 8], [3, 0], [4, 8], [5, 0], [6, 8], [7, 0]]
            self.feed = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0,0]]
            self.image = 'data/img/worlds/w1/s3/q3.png'
            self.bar = 'data/img/Bar_5.png'
            self.selected_bar = 'data/img/Bar_5_g.png'
            self.offset = [-192, -36]
            self.lay = 48
        if layer == 49:
            self.position = {'1': [[20, 198], [400, 226], False], '2': [[20, 276], [400, 344], False],
                             '3': [[20, 354], [400, 422], False], '4': [[490, 198], [870, 266], False],
                             '5': [[490, 276], [870, 344], False], '6': [[490, 354], [870, 422], False],
                             '7': [[253, 432], [633, 500], False], '8': [[256, 124], [636, 192], False]}
            self.answ = [[1, 8], [2, 0], [3, 8], [4, 0], [5, 8], [6, 0], [7, 8]]
            self.feed = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
            self.image = 'data/img/worlds/w1/s3/q3.png'
            self.bar = 'data/img/Bar_5.png'
            self.selected_bar = 'data/img/Bar_5_g.png'
            self.offset = [-192, -36]
            self.lay = 49
        if layer == 53:
            self.position = {'1': [[18, 120], [386, 173], False], '2': [[18, 195], [386, 255], False],
                             '3': [[18, 274], [386, 332], False], '4': [[496, 142], [627, 254], False],
                             '5': [[496, 290], [627, 402], False], '6': [[734, 142], [861, 254], False]}
            self.answ = [[1, 6], [2, 5], [3, 4]]
            self.feed = [[0, 0], [0, 0], [0, 0]]
            self.image = 'data/img/worlds/w1/s3/q4.png'
            self.bar = 'data/img/bar_3.png'
            self.selected_bar = 'data/img/bar_3_g.png'
            self.offset = [-65, -55]
        if layer == 61:
            self.position = {'1': [[18, 120], [386, 173], False], '2': [[18, 195], [386, 255], False],
                             '3': [[18, 274], [386, 332], False], '4': [[18, 354], [386, 422], False],
                             '5': [[18, 430], [386, 498], False], '6': [[496, 142], [627, 254], False],
                             '7': [[496, 290], [627, 402], False], '8': [[734, 142], [861, 254], False],
                             '9': [[734, 290], [861, 402], False], '10': [[617, 215], [749, 325], False]
                             }
            self.answ = [[1, 7], [2, 10], [3, 6], [4, 9], [5, 8]]
            self.feed = [[0, 0], [0, 0], [0, 0],[0, 0],[0, 0]]
            self.image = 'data/img/worlds/w1/s3/q5.png'
            self.bar = 'data/img/bar_3.png'
            self.selected_bar = 'data/img/bar_3_g.png'
            self.offset = [-65, -55]
        if layer == 71:
            self.position = {'1': [[138, 161], [388, 240], False], '2': [[138, 275], [388, 355], False],
                             '3': [[138, 382], [388, 465], False], '4': [[538, 161], [787, 239], False],
                             '5': [[538, 275], [787, 349], False], '6': [[538, 387], [787, 464], False]}
            self.answ = [[1, 6], [2, 4], [3, 5]]
            self.feed = [[0, 0], [0, 0], [0, 0]]
            self.image = 'data/img/worlds/w1/s3/q6.png'
            self.bar = 'data/img/Bar.png'
            self.selected_bar = 'data/img/Bar_g.png'
            self.offset = [-142, -52]
        if layer == 90:
            self.position = {'1': [[138, 161], [388, 240], False], '2': [[138, 275], [388, 355], False],
                             '3': [[138, 382], [388, 465], False], '4': [[538, 161], [787, 239], False],
                             '5': [[538, 275], [787, 349], False], '6': [[538, 387], [787, 464], False]}
            self.answ = [[1, 5], [2, 4], [3, 6]]
            self.feed = [[0, 0], [0, 0], [0, 0]]
            self.image = 'data/img/worlds/w1/s3/q10.png'
            self.bar = 'data/img/Bar.png'
            self.selected_bar = 'data/img/Bar_g.png'
            self.offset = [-142, -52]