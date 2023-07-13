b_width=19
b_height=19
list_al=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S']
list_l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
board_height_show=False


def create_board(b_width,b_height):
    board_list=[]
    for i in range(b_height*2+1):
        board_list.append(list())
        if i%2==0:
            for a in range(b_width):
                (board_list[i]).append("   ")
                (board_list[i]).append("  -")
                if a==b_width-1:
                    (board_list[i]).append("   ")
        else:
            for a in range(b_width):
                (board_list[i]).append("  |")
                (board_list[i]).append("   ")
                if a==b_width-1:
                    (board_list[i]).append("  |")
    return board_list


def create_value(b_width,b_height):
    board_value=[]
    for i in range((b_width)*(b_height)):
        board_value.append("")
    return board_value


def wrong_place(board_value,width,height,list_al):
    if board_value[((list_al.index(height))*19)+(list_al.index(width))]!="":
        return False
    return True


def value_change(board_value,width,height,player,list_al):
    (board_value[((list_al.index(height))*19)+(list_al.index(width))])=(player)
    return board_value


def check_row(board_value,b_width,b_height):
    b=0
    for a in range(b_height):
        for i in range(b_width-4):
            if (((board_value[b+i])==(board_value[b+i+1])) 
                and ((board_value[b+i+1])==(board_value[b+i+2])) 
                and ((board_value[b+2+i])==(board_value[b+i+3])) 
                and ((board_value[b+i+3])==(board_value[b+i+4])) 
                and ((board_value[b+i])!=(""))):
                return False
        b+=19
    return True


def check_col(board_value,b_width,b_height):
    for a in range(b_height-4):
        for i in range(b_width):
            if (((board_value[19*a+i])==(board_value[19*a+i+19])) and ((board_value[19*a+i+19])==(board_value[19*a+i+38])) and ((board_value[19*a+i+38])==(board_value[19*a+i+57])) and ((board_value[19*a+i+57])==(board_value[19*a+i+76])) and ((board_value[19*a+i])!=(""))):
                return False
    return True


def change_lower(letter,list_l):
    if letter in list_l:
        letter=list_al[list_l.index(letter)]
    return letter

def check_es(board_value,b_width,b_height):
    for a in range(b_height-4):
        for i in range(b_width-4):
            if (((board_value[19*a+i])==(board_value[19*a+i+20])) and ((board_value[19*a+i+20])==(board_value[19*a+i+40])) and ((board_value[19*a+i+40])==(board_value[19*a+i+60])) and ((board_value[19*a+i+60])==(board_value[19*a+i+80])) and ((board_value[19*a+i])!=(""))):
                return False
    return True


def check_ws(board_value,b_width,b_height):
    for a in range(b_height-4):
        for i in range(b_width-4):
            if (((board_value[19*a+i+4])==(board_value[19*a+i+4+18])) and ((board_value[19*a+i+4+18])==(board_value[19*a+i+4+36])) and ((board_value[19*a+i+4+36])==(board_value[19*a+i+4+54])) and ((board_value[19*a+i+4+54])==(board_value[19*a+i+4+72])) and ((board_value[19*a+i+4])!=(""))):
                return False
    return True


def check_winner(board_value,b_width,b_height):
    flag=check_row(board_value,b_width,b_height)
    if flag==False:
        return flag
    flag=check_col(board_value,b_width,b_height)
    if flag==False:
        return flag
    flag=check_es(board_value,b_width,b_height)
    if flag==False:
        return flag
    flag=check_ws(board_value,b_width,b_height)
    if flag==False:
        return flag
    

def board_show_f(board_game,list_al,board_height_show):
    board_show=[]
    a=0
    for i in range(b_width):
        board_show.append("     ")
        board_show.append(list_al[a])
        a+=1
    a=0
    if board_height_show==False:
        for i in range(b_height*2+1):
            if i%2==1:
                (board_game[i]).append("   ")
                (board_game[i]).append(list_al[a])
                a+=1
    board_show.append("\n")
    for i in range(b_height*2+1):
        board_peice=board_game[i]
        board_term="".join(str(x) for x in board_peice)
        board_show.append(board_term)
        board_show.append("\n")
    board_play="".join(str(x) for x in board_show)
    print(board_play)


def play_game(board_game,list_al,board_height_show,board_value,b_width,b_height,list_l):
    a=0
    while 1:
        if a%2==0:
            player="$"
            print("A($) turn")
            height=input("row:")
            width=input("col:")
            width=change_lower(width,list_l)
            height=change_lower(height,list_l)
            flag=True
            if (width not in list_al) or (height not in list_al):
                print("wrong input, please try again")
                continue
            flag=wrong_place(board_value,width,height,list_al)
            if flag==False:
                print("wrong input, please try again")
                continue
            board_value=value_change(board_value,width,height,player,list_al)
            board_game=player_A(board_game,width,height,list_al)
            board_show_f(board_game,list_al,board_height_show)
            flag=check_winner(board_value,b_width,b_height)
            if flag==False:
                print("Player A win")
                break
            a+=1
        else:
            player="#"
            print("B(#) turn")
            height=input("row:")
            width=input("col:")
            width=change_lower(width,list_l)
            height=change_lower(height,list_l)
            flag=True
            if (width not in list_al) or (height not in list_al):
                print("wrong input, please try again")
                continue
            flag=wrong_place(board_value,width,height,list_al)
            if flag==False:
                print("wrong input, please try again")
                continue
            board_value=value_change(board_value,width,height,player,list_al)
            board_game=player_B(board_game,width,height,list_al)
            board_show_f(board_game,list_al,board_height_show)
            flag=check_winner(board_value,b_width,b_height)
            if flag==False:
                print("Player B win")
                break
            a-=1


def player_A(board_game,width,height,list_al):
    board_term=board_game[list_al.index(height)*2+1]
    board_term[list_al.index(width)*2+1]="  $"
    board_game[list_al.index(height)*2+1]=board_term
    return board_game


def player_B(board_game,width,height,list_al):
    board_term=board_game[list_al.index(height)*2+1]
    board_term[list_al.index(width)*2+1]="  #"
    board_game[list_al.index(height)*2+1]=board_term
    return board_game


def start_game(b_width,b_height,list_al,board_height_show,list_l):
    board_game=create_board(b_width,b_height)
    board_value=create_value(b_width,b_height)
    board_show_f(board_game,list_al,board_height_show)
    board_height_show=True
    print("Gomoku Started  player:A($) vs player:B(#)")
    play_game(board_game,list_al,board_height_show,board_value,b_width,b_height,list_l)


while 1:
    choice=input("1 to begin, others to end:")
    if choice=="1":
        start_game(b_width,b_height,list_al,board_height_show,list_l)
    else:
        break