# -*- coding: utf-8 -*-
"""
@author:黄炎哲
"""


import random
import operator
import re

class Card(object):
    def __init__(self,suite,face):
        self._suite=suite
        self._face=str(face)
    
        
    def __str__(self):
        """所有的花色与数字组合"""
        return self._suite+self._face #返回如‘♥6’这种形式
        

        
class Poker(object):
    def __init__(self):
        self._cards=[Card(suite,face) 
                     for suite in '♥♠♣♣♦'
                     for face in range(1,14)] #一副牌，没考虑大小王
        self._mycards=[]
        self._member_card1=[]
        self._member_card2=[]
    def cards_shuffle(self):
        """洗牌"""
        mycards=[] 
        for i in self._cards:
            mycards.append(str(i))
        self._mycards=mycards
        random.shuffle(self._mycards)  #洗牌
        
    def get_poker(self,p):#p是选择哪个player
        """发牌"""
        if p=='p1':
            for i in range(2):
                self._member_card1.append(self._mycards[-1])
                self._mycards.pop()
            return self._member_card1
        if p=='p2':
            for i in range(2):
                self._member_card2.append(self._mycards[-1])
                self._mycards.pop()
            return self._member_card2
    def get_next_poker(self,p):
        if p=='p1':        
            self._member_card1.append(self._mycards[-1])
            self._mycards.pop()
            return self._member_card1
        if p=='p2':        
            self._member_card2.append(self._mycards[-1])
            self._mycards.pop()
            return self._member_card2
        
class Player(object):
    def __init__(self,name):
        self._name=name
        self._cards_on_hand=[]
        #self._compare_card=[]
        

    def get(self,cards):
        self._cards_on_hand=cards
        
    def arrange(self,cards):
        """整理牌,按照数字从小到大"""
        new_card=[]
        for card in cards: 
           a=re.findall(r"\d+",card)
           b=list(card[0])
           c=(b+a)
           new_card.append(c)
        
        for card in new_card: #将花色后的数字类型变为int，方便整理牌
            for i in range(len(card)):
                card[1]=int(card[1])         
        new_card= sorted(new_card,key=operator.itemgetter(1),reverse=False) #以先数字为准从小到大整理

        d=''
        new_card2=[] #将拆开的‘♥’，6再合成‘♥6’
        for card in new_card:
            for item in card:
                d+=str(item)
            new_card2.append(d)
            d=''
        self._cards_on_hand=new_card2
        
    def arrange2(self):
        """整理牌,按照数字从小到大,便于比较点数"""
        self._compare_card=[]#这句容易漏加
        for i in self._cards_on_hand:
            self._compare_card.append(int(i[1:]))#提取数字,注意是1：
        for i in range(len(self._compare_card)): #点数规则
            if self._compare_card[i]>10:
                self._compare_card[i]=10
            if self._compare_card[i]==1:
                if sum(self._compare_card)<=21:
                    self._compare_card[i]=11

# 显示每轮双方的状态
def show_state(player,temp):
    print(player._name+':',end=' ')
    player.arrange(temp)
    player.arrange2()
    print(player._cards_on_hand)
  

            
P=Poker()
P.cards_shuffle()

player1=Player('你')
player2=Player('电脑')

"""你先决定是否叫牌"""
print("=====初始发牌=====")
temp1=P.get_poker('p1')
player1.get(temp1)
show_state(player1,temp1)

temp2=P.get_poker('p2')
player2.get(temp2)
show_state(player2,temp2)


while len(P._mycards)>0:
    
    if sum(player1._compare_card)==21:
        print('点数到达21，你胜出')
        break
    if sum(player2._compare_card)==21:
        print('点数到达21，电脑胜出')
        break
    if sum(player1._compare_card)>21:
        print(player1._compare_card)
        print('你点数大于21，电脑胜出')
        break
    if sum(player1._compare_card)<21:
        
        inp=input('叫牌吗？Y/N')
        if inp=='Y':
            temp3=P.get_next_poker('p1')
            player1.get(temp3)
            print("=====状态=====")
            show_state(player1,temp3)
            print(player2._name+':',end=' ')
            print(player2._cards_on_hand)
            continue
            
        if inp=='N':
            print('你没有选择叫牌')
            temp4=P.get_next_poker('p2') #电脑叫牌
            
            player2.get(temp4)
            print("=====状态=====")
            print(player1._name+':',end=' ')
            print(player1._cards_on_hand)
            show_state(player2,temp4)
            
            if sum(player2._compare_card)>sum(player1._compare_card):
                if sum(player2._compare_card)>21:    
                    print('电脑点数大于21，你胜出')
                    break
                    
                if sum(player2._compare_card)<21:
                    print('电脑点数大于你，电脑胜出')
                    break
            if sum(player2._compare_card)==sum(player1._compare_card):
                print('平局')
                break
            if sum(player2._compare_card)<sum(player1._compare_card):
                continue
        else:
            print('请重新确认是否叫牌')
            continue
        

        

