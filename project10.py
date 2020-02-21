import random
from operator import itemgetter
from array import *



NUM=[i for i in range(2,15)]#deck and hand building
SYM=["C","S","D","H"]

DECK=[]
for i in SYM:
    for j in NUM:
        DECK.append([i,j])
random.shuffle (DECK)

hand_1=[]
hand_2=[]
for i in range (0,5):
    card_1=DECK.pop(-1)
    card_2=DECK.pop(-1)
    hand_1.append(card_1)
    hand_2.append(card_2)
        
hand_1.sort(key=itemgetter(1))
hand_2.sort(key=itemgetter(1))





def check_hand(hand):
    global temp2,temp3,temp4,temp5,HC,val
    temp2=temp3=temp4=temp5=val=""
    HC=hand[4][1]
    if check_SF(hand):
        return 9
    if check_FOAK(hand):
        return 8
    if check_FH(hand):
        return 7
    if check_FLUSH(hand):
        return 6
    if check_STRAIGHT(hand):
        val=temp5#temp5 is the value of the straight
        return 5
    if check_TOAK(hand):
        val=temp4#temp4 is the value of the three of a kind
        return 4
    if check_TP(hand):
        return 3
    if check_OP(hand):
        val=temp2#temp2 is the value of the one pair
        return 2
    return 1







def check_SF(hand):
    global val,temp5
    if check_FLUSH(hand) and check_STRAIGHT(hand):
        val=temp5
        return True
    else:
        return False

def check_FOAK(hand):
    global HC,val
    for i in range(0,2):
        if hand[i][1]==hand[i+3]:#no need to check the inbetween because the hand is sorted
            val=hand[i][1]
            if i==1:
                HC=hand[0][1]#if the FOAK are the last 4 then the high card is the first card
            return True
    return False

def check_FH(hand):
    global val,temp4,HC
    if check_TOAK(hand) and check_OP(hand):
        val=temp4 
        return True
    else:
        return False

def check_FLUSH(hand):
    if sum(x.count(hand[0][0]) for x in hand)==5:
        return True
    else:
        return False

def check_STRAIGHT(hand):
    global temp5
    temp=True
    for i in range (0,4):
        if hand[i][1]!=hand[i+1][1]-1:
            temp=False
        else:
            temp5=hand[4][1]
    if hand[0][1]==2 and hand[1][1]==3 and hand[2][1]==4 and hand[3][1]==5 and hand[4][1]==13:
        temp=True
        temp5=5
    return temp

def check_TOAK(hand):
    global HC,temp4
    for i in range(0,3):
        if hand[i][1]==hand[i+2][1]:#no need to check hand[i+1][1] because the hand is sorted
            temp4=hand[i][1]
            if i==2:
                HC=hand[1][1]#if the last 3 are the TOAK then the 2nd card is the high card,otherwise its the 5th card
            return True
    return False

def check_TP(hand):
    global HC,temp3,val
    temp3=0
    for i in range(0,2):
        if hand[i][1]==hand[i+1][1]:
            temp3=hand[i][1]#this is the smaller pair because hand is sorted
            for j in range(i+2,4):
                if hand[j][1]==hand[j+1][1]:
                        val=hand[j][1]
                        for i in range(0,5):
                            if hand[i][1]!=temp3 and hand[i][1]!=val:#this finds the card that isnt part of the two pairs
                                HC=hand[i][1]
                        return True
    return False

def check_OP(hand):
    global HC,temp2
    for i in range(0,4):
        if hand[i][1]==hand[i+1][1]:
            temp2=hand[i][1]
            if i==3:
                HC=hand[2][1]#if the last two are the pair then the high card is the 3rd card,otherwise its the 5th
            return True
    return False



def compare_hands():
    global win,rank1,rank2,val1,val2,HC1,HC2,temp3_1,temp3_2
    if rank1>rank2:
        win=1
    elif rank1<rank2:
        win=2
    else:#same rank
        if rank1==6 or rank1==1:#these need seperate check because they use only high card
            if HC1>HC2:
                win=1
            elif HC1<HC2:
                win=2
            else:
                win=0
        else:
            if val1>val2:
                win=1
            elif val1<val2:
                win=2
            else:
                if rank1==9 or rank1==5:#if the value of straights are the same then its a draw regardless of high card
                    win=0
                elif rank1==3:#if its 2 pairs it first checks the second pair first then continues to check high card
                    if temp3_1>temp3_2:
                        win=1
                    elif temp3_1<temp3_2:
                        win=2
                    else:
                        if HC1>HC2:
                            win=1
                        elif HC1<HC2:
                          win=2
                        else:
                            win=0
                else:
                    if HC1>HC2:
                        win=1
                    elif HC1<HC2:
                        win=2
                    else:
                        win=0
                
def announce():
    global win
    for i in range(0,5):
        if hand_1[i][1]==11:
            hand_1[i][1]="J"
        elif hand_1[i][1]==12:
            hand_1[i][1]="Q"
        elif hand_1[i][1]==13:
            hand_1[i][1]="K"
        elif hand_1[i][1]==14:
            hand_1[i][1]="A"
        if hand_2[i][1]==11:
            hand_2[i][1]="J"
        elif hand_2[i][1]==12:
            hand_2[i][1]="Q"
        elif hand_2[i][1]==13:
            hand_2[i][1]="K"
        elif hand_2[i][1]==14:
            hand_2[i][1]="A"
    print("player 1:",hand_1)
    print("player 2:",hand_2)
    if win==0:
        print("its a draw")
    else:
        print("player ",win," wins")


       



val1=HC1=temp3_1=val2=HC2=temp3_2=win=""
rank1=check_hand(hand_1)
val1=val
HC1=HC
temp3_1=temp3
rank2=check_hand(hand_2)
val2=val
HC2=HC
temp3_2=temp3
compare_hands()
announce()     




        
    
