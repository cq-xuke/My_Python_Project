# -*- coding: utf-8 -*-
import random

cc_map = {0:0, 1:10} 
ch_map = {0:0, 1:10, 2:11, 3:24, 4:39, 5:5}

def draw_cc(position):
        card_num = random.randint(0, 15)
        if card_num in cc_map:
                return cc_map[card_num]
        return position

def draw_ch(position):
        card_num = random.randint(0, 15)
        if card_num in ch_map:
                return ch_map[card_num] 
        if(card_num == 6 or card_num == 7):
                if position < 5:
                        return 5
                if position < 15:
                        return 15
                if position < 25:
                        return 25
                if position < 35:
                        return 35
                return 5
        if(card_num == 8):
                if position < 12:
                        return 12
                if position < 28:
                        return 28
                return 12
        if(card_num == 9):
                if position == 36:
                        return draw_cc(33)
                return position-3
        return position

position = 0
rolls = 100000
square_count_map = {}
for i in xrange(40):
        square_count_map[i] = 0
doubles_count = 0

for i in xrange(rolls):
        d1 = random.randint(1,4)
        d2 = random.randint(1,4)
        if(d1 == d2):
                doubles_count += 1
        else:   
                doubles_count = 0
        if(doubles_count == 3):
                position = 10 
                doubles_count = 0
        else:   
                position += (d1 + d2)
                position %= 40
        if(position == 30):
                position = 10
        elif(position in [2,17,33]):
                position = draw_cc(position)
        elif(position in [7,22,36]):
                position = draw_ch(position)
        square_count_map[position]+=1

for square in xrange(40):
        print(square, round(100 * square_count_map[square] / float(rolls), 4))

print(sorted(square_count_map, key=lambda square: square_count_map[square])[:-4:-1])