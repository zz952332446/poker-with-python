# -*- coding: utf-8 -*-
"""
模拟四个玩家的扑克牌游戏，52张牌
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
        return self._suite+self._face #返回如‘♥6’这种形式，用逗号、括号括扩一起都不行
        

        
class Poker(object):
    def __init__(self):
        self._cards=[Card(suite,face) 
                     for suite in '♥♠♣♣♦'
                     for face in range(1,14)] #没考虑大小王
        self._mycards=[]
    def cards_shuffle(self):
        """洗牌"""
        mycards=[] 
        for i in self._cards:
            mycards.append(str(i))
        self._mycards=mycards
        random.shuffle(self._mycards)  #洗牌
        
    def get_poker(self):
        """发牌"""
        member=[]
        for i in range(13):
            member.append(self._mycards[-1])
            self._mycards.pop()
        return member
        
class Player(object):
    def __init__(self,name):
        self._name=name
        self._cards_on_hand=[]
        

    def get(self,cards):
        self._cards_on_hand=cards
        
    def arrange(self,cards):
        """整理牌"""
        new_card=[]
        for card in cards: #‘♥6’拆正‘♥’，‘6’这种形式为之后的operator.itemgetter方便
           a=re.findall(r"\d+",card) #找出字符串中的数字
           b=list(card[0])
           c=(b+a)
           new_card.append(c)
        
        for card in new_card: #将花色后的数字类型变为int，方便整理牌
            for i in range(len(card)):
                card[1]=int(card[1])         
        new_card= sorted(new_card,key=operator.itemgetter(1),reverse=False) #以先数字为准从小到大整理牌

        d=''
        new_card2=[] #将拆开的‘♥’，6再合成‘♥6’
        for card in new_card:
            for item in card:
                d+=str(item)
            new_card2.append(d)
            d=''
        self._cards_on_hand=new_card2
            
P=Poker()
P.cards_shuffle()
players=[Player('小红'),Player('小蓝'),Player('小紫'),Player('小黑')]
for player in players:
    temp=P.get_poker()
    player.get(temp)
    print(player._name+':',end=' ')
    player.arrange(temp)
    print(player._cards_on_hand)
    
    
"""
结果展示
小红: ['♦2', '♥4', '♣5', '♥5', '♦7', '♣8', '♦8', '♥10', '♦11', '♠11', '♠12', '♣13', '♠13']
小蓝: ['♣1', '♣2', '♦3', '♦4', '♣4', '♣4', '♦6', '♠6', '♠7', '♣7', '♥9', '♦12', '♣13']
小紫: ['♠2', '♣3', '♠5', '♣6', '♥6', '♥8', '♦9', '♦10', '♠10', '♣10', '♥12', '♣12', '♥13']
小黑: ['♠1', '♥3', '♣3', '♠4', '♦5', '♣5', '♣7', '♥7', '♠8', '♠9', '♣10', '♥11', '♦13']

"""

        
