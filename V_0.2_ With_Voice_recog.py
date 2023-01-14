import numpy as np
import speech_recognition as sr
import pyttsx3


listener = sr.Recognizer()
engine = pyttsx3.init()
# engine.say("Hello, Welcome to THE Battleship Game !")
# print("Hello, Welcome to THE Battleship Game !")
# engine.runAndWait()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)    



def talk(text):
    engine.say(text)
    engine.runAndWait()
    


            
def show_grid(which):
    print("   ",end= " ")
    for i  in range(n):
        print(i+1,end = "    ")
    print("")
    print("   ",end= "")
    for i  in range(2*n+2):
        print("━",end = "━") 
    print("")
    for i in range(n):
        print(i+1,end = " ")
        print("┃",end=" ")
        for j in range(n):
            if which==1:
                print(gridA[i][j],end = "    ")
            elif which==3:
                print(grid1[i][j],end = "    ")
            elif which==4:
                print(grid2[i][j],end = "    ")
            else:
                print(gridB[i][j],end = "    ")
        print("")
        print("  ┃")
        
        
def ship_info(i,p_no):
    f=0
    while f==0:  
        try:
            print("Enter the middle coordinate of ship ",i+1,": (x,y)",end = "")
            num=str(i+1)
            talk("Enter the middle coordinate of ship " + num)
            [x2,y2] = input().split(",")
        except ValueError:
            print("ERROR: Invalid coordinate format. Should be of format x ,y where x=row number, y=column nuber")
            print()
            talk("ERROR: Invalid coordinate format. Should be of format x ,y where x=row number, y=column nuber")
        else:
            try:
                x2=int(x2)
                y2=int(y2)
            except ValueError:
                print("ERROR: The Corrdinates should be natural Numbers")
                talk("ERROR: The Corrdinates should be natural Numbers")
                print()
            else:
                if x2<1 or y2<1 or x2>n or y2>n:
                    print("Coordinate not found in grid. Enter Again.")
                    talk("Coordinate not found in grid. Enter Again.")
                    print()
                else:
                    f=1
    
            # [x2,y2] = input("Coordinate 2: ").split(",")
            # [x3,y3] = input("Coordinate 3: ").split(",")
            # x1,x2,x3,y1,y2,y3=int(x1),int(x2),int(x3),int(y1),int(y2),int(y3)
            # if(abs(x1-x2)==1 and abs(x2-x3)==1  and abs(x1-x3)==2 and y1 == y2 and y2 == y3):
            #     if(x1 <=n and x1 >= 1 and x2 <=n and x2 >= 1  and x3 <=n and x3 >= 1 and y1 <= n and y1 >= 1):
            #         flag = 1;
            # if(abs(y1-y2)==1 and abs(y2-y3)==1  and abs(y1-y3)==2 and x1 == x2 and x2 == x3):
            #     if(y1 <=n and y1 >= 1 and y2 <=n and y2 >= 1  and y3 <=n and y3 >= 1 and x1 <= n and x1 >= 1):
            #         flag = 1;

    flag = 0
    bu=0
    while bu==0:
        talk("Select Horizontal or Vertical")
        horv=input("horizontal[h] or vertical[v]: ")
        if horv=="h":
            bu=1
            if y2!=1 and y2!=n:
                [x1,y1]=[x2,y2-1]
                [x3,y3]=[x2,y2+1]
                flag=1
                
        elif horv=="v":
            bu=1
            if x2!=1 and x2!=n:
                [x1,y1]=[x2-1,y2]
                [x3,y3]=[x2+1,y2]
                flag=1
                
        else:
            print("Invalid Selection")
            talk("Invalid Selection")
    if flag==0:
        print()
        print("Invalid Ship coordinate. Ship does not fit")
        talk("Invalid Ship coordinate. Ship does not fit")
        print()
        return ship_info(i,p_no)
    else:
        if p_no==1:
            grid1[x1-1][y1-1]="/"
            grid1[x2-1][y2-1]="/"
            grid1[x3-1][y3-1]="/"
            show_grid(3)
        else:
            grid2[x1-1][y1-1]="/"
            grid2[x2-1][y2-1]="/"
            grid2[x3-1][y3-1]="/" 
            show_grid(4)
        name = []
        name.append([x1,y1])
        name.append([x2,y2])
        name.append([x3,y3])
        return name



def clear():
    print("\n"*20)
    
    
truthness=True
while truthness==True:
    
    clear()
    print("                      WELCOME TO BATTLESHIP  ")
    print("Enemies ship has entered your radar. And it's your duty to destroy them all.")
    talk("WELCOME TO BATTLESHIP")
    talk("Enemies ship has entered your radar. And it's your duty to destroy them all.")
    talk("Press enter to countinue")
    ran=input("Press enter to continue")

    
    print()
    print("play game[p]")
    print("instruction[i]")
    talk("Play game or go to instructions")
    x=input("Select: ")
    print()
    if x.lower()=="p":
        print("ENTER PLAYER'S NAME")
        talk("ENTER PLAYER'S NAME")
        p_name1=input("Player 1: ")
        p_name2=input("Player 2: ")
        loop=1
        while loop==1:
            try:
                talk("Enter the grid size: ")
                n=int(input("Enter the grid size: "))
                
                if n>2:
                    loop=0
                else:
                    print("ERROR: Grid size should be greater than 2")
                    talk("ERROR: Grid size should be greater than 2")
            except ValueError:
                print("ERROR: Grid Size should be a natural number")
                talk("ERROR: Grid Size should be a natural number")
        gridA=np.full((n,n),"0")
        gridB=np.full((n,n),"0")
        grid1=np.full((n,n),"0")  
        grid2=np.full((n,n),"0")  
        print("")   
        show_grid(1)
        
        
        loop=1
        while loop==1:
            try:
                talk("Enter the number of ships: ")
                ship_no=(int(input("Enter the number of ships: ")))
                if ship_no > ((n**2)/3)-1:
                    print("Error:Too many ships, cannot fit")
                    talk("Error: Too many ships, cannot fit")
                else:
                    loop=0
            except ValueError:
                print("ERROR: Ship number should be a natural number")
                talk("ERROR: Ship number should be a natural number")
        clear()
        print("FOR" ,p_name1.upper()," ")
        forp="FOR "+p_name1.upper()
        talk(forp)
        ships1 = []
        show_grid(3)
        for ship_list1 in range(ship_no):
            om=0
            while om==0:
                currship=ship_info(ship_list1,1)
                mn=0
                for xy in range(ship_list1):
                    for yz in range(3):
                        if ships1[xy][yz]==currship[0] or ships1[xy][yz]==currship[1] or ships1[xy][yz]==currship[2]:
                            print("ERROR: Coordinate ",ships1[xy][yz]," overlap in two ships. Enter Again.")
                            overlap=str(xy)+str(yz)
                            talk("ERROR: Coordinate "+ overlap+"overlap in two ships. Enter Again." )
                            mn=1
                            [x1,y1],[x2,y2],[x3,y3]=currship[0],currship[1],currship[2]
                            grid1[x1-1][y1-1]="0"
                            grid1[x2-1][y2-1]="0"
                            grid1[x3-1][y3-1]="0"
                            grid1[ships1[xy][yz][0]-1][ships1[xy][yz][1]-1]="/"
                            break
                if mn==0:
                    om=1
                    ships1.append(currship)
        talk("Press enter to countinue")
        extra=input("Press enter to countinue")
        clear()
        print("FOR" ,p_name2.upper()," ")
        forp="FOR "+p_name2.upper()
        talk(forp)
        show_grid(4)
        ships2 = []
        for ship_list2 in range(ship_no):
            om=0
            while om==0:
                currship=ship_info(ship_list2,2)
                mn=0
                for xy in range(ship_list2):
                    for yz in range(3):
                        if ships2[xy][yz]==currship[0] or ships2[xy][yz]==currship[1] or ships2[xy][yz]==currship[2]:
                            print("ERROR: Coordinate ",ships2[xy][yz]," overlap in two ships. Enter Again.")
                            talk("ERROR: Coordinate "+ overlap+"overlap in two ships. Enter Again." )
                            mn=1
                            [x1,y1],[x2,y2],[x3,y3]=currship[0],currship[1],currship[2]
                            grid2[x1-1][y1-1]="0"
                            grid2[x2-1][y2-1]="0"
                            grid2[x3-1][y3-1]="0"
                            grid2[ships2[xy][yz][0]-1][ships2[xy][yz][1]-1]="/"
                if mn==0:
                    om=1
                    ships2.append(currship)
        talk("Press enter to countinue")
        extra=input("Press enter to countinue")  
        clear()
        p1=0
        p2=0
        l1=[]
        l2=[]
        for chance in range(2*(n**2)+2):
            while p1!=ship_no and p2!=ship_no:
                if chance%2==0:
                    show_grid(1)
                    print (p_name1.capitalize(), "'s Turn")
                    talk(p_name1+" Turn")
                    f=0
                    while f==0:  
                        try:
                            talk("Enter Coordinate to fire missile: ")
                            [x,y] = input("Enter Coordinate to fire missile: ").split(",")
                        except ValueError:
                            print("ERROR: Invalid coordinate format. Should be of format x,y where x=row number, y=column nuber")
                            print()
                            talk("ERROR: Invalid coordinate format. Should be of format x,y where x=row number, y=column nuber")
                        else:
                            try:
                                x=int(x)
                                y=int(y)
                            except ValueError:
                                print("ERROR: The Corrdinates should be natural Numbers")
                                talk("ERROR: The Corrdinates should be natural Numbers")
                                print()
                            else:
                                if [x,y] in l1:
                                    print("You Had already Fired there. Enter another Coordinate")
                                    print()
                                    talk("You Had already Fired there. Enter another Coordinate")
                                elif x<1 or y<1 or x>n or y>n:
                                    print("Coordinate not found in grid. Enter Again.")
                                    talk("Coordinate not found in grid. Enter Again.")
                                    print()
                                else:
                                    l1.append([x,y])
                                    f=1
                    t=0
                    for no in range(ship_no):
                        if [x,y] in ships2[no]:
                            print("A Direct Hit ")
                            talk("A Direct Hit ")
                            ships2[no].remove([x,y])
                            gridA[x-1][y-1]="X"
                            t=1
                            break
                            if len(ships2[no])==0:
                                print("A ship is sunk")
                                talk("A ship is sunk")
                    if t==0:
                        print("You Missed")
                        talk("You Missed")
                        gridA[x-1][y-1]="-"
                    talk("Press Enter to Countinue")
                    extra=input("Press Enter to Countinue")
                    chance+=1
                else:
                    show_grid(2)
                    print (p_name2.capitalize(), "'s Turn")
                    talk(p_name2+" Turn")
                    f=0
                    while f==0:  
                        try:
                            talk("Enter Coordinate to fire missile: ")
                            [x,y] = input("Enter Coordinate to fire missile: ").split(",")
                            
                        except ValueError:
                            print("ERROR: Invalid coordinate format. Should be of format x,y where x=row number, y=column nuber")
                            print("ERROR: Invalid coordinate format. Should be of format x,y where x=row number, y=column nuber")
                            talk()
                        else:
                            try:
                                x=int(x)
                                y=int(y)
                            except ValueError:
                                print("ERROR: The Corrdinates should be natural Numbers")
                                talk("ERROR: The Corrdinates should be natural Numbers")
                                print()
                            else:
                                if [x,y] in l2:
                                    print("You Had already Fired there. Enter another Coordinate")
                                    print("You Had already Fired there. Enter another Coordinate")
                                    talk()
                                elif x<1 or y<1 or x>n or y>n:
                                    talk("Coordinate not found in grid. Enter Again.")
                                    print("Coordinate not found in grid. Enter Again.")
                                    print()
                                else:
                                    l2.append([x,y])
                                    f=1
                    t=0
                    for no in range(ship_no):
                        if [x,y] in ships1[no]:
                            print("A Direct Hit ")
                            talk("A Direct Hit ")
                            ships1[no].remove([x,y])
                            gridB[x-1][y-1]="X"
                            t=1
                            if len(ships1[no])==0:
                                print("A ship is sunk")   
                                talk("A ship is sunk")
                    if t==0:
                        print("You Missed")
                        talk("You Missed")
                        gridB[x-1][y-1]="-"
                    chance+=1
                    talk("Press Enter to Countinue")
                    extra=input("Press Enter to Countinue")
                for m in range(ship_no):
                    if len(ships1[m])==0:
                        p1+=1
                        ships1[m]=["over","over"]
                    if len(ships2[m])==0:
                        p2+=1
                        ships2[m]=["over","over"]
        if p2==ship_no:
            print()
            print(p_name1.upper()," WON. CONGO ..")
            talk(p_name1.upper()+" WON. CONGO ..")
        else:
            print()
            print(p_name2.upper()," WON. CONGO ..")
            talk(p_name2.upper()," WON. CONGO ..")
        talk("Press c for credits ")
        credit=input("Press c for credits ")
        
        if credit.lower()=="c":
            x='''Made by: Tanmay Mittal
         Class: XI-C
    Special Thanks: Smriti Maam'''
            print()
            print(x) 
            talk('''Made by: Tanmay Mittal
         Class: 11th-C
    Special Thanks: Smriti Maam''')
        truthness=False
    
    
    if x.lower()=="i":
        clear()
        print("INSTRUCTIONS:  ")
        talk("INSTRUCTIONS")
        print('''Objective: First to sink all the opponent's ships wins the game''')
        talk('''Objective: First to sink all the opponent's ships wins the game''')
        i=input("Press Enter")
        
        print()
        print('''Game initialization: Enter the player's name and select the grid size (atleast 3) and number of ships in the game
    
Prepare for battle: Each player takes turn to hide the ship in their grid, without the other player looking. Each ship is of length 3X1
    
To place the ship- Enter the middle coordinate of ship in the format row,column that is number on the left,number on top
Select if you want your ship to be horizontal or vertical.
    
After both the players have placed their ships, let the game begin.''')
        talk('''Game initialization: Enter the player's name and select the grid size (atleast 3) and number of ships in the game
    
Prepare for battle: Each player takes turn to hide the ship in their grid, without the other player looking. Each ship is of length 3X1
    
To place the ship- Enter the middle coordinate of ship in the format row ,column that is number on the left, number on top
Select if you want your ship to be horizontal or vertical.
    
After both the players have placed their ships, let the game begin.''')
        i=input("Press Enter ")
        print()
        print('''Call Your shot: Guess where the opponent ship is. Enter the coordinate(row, column) where you want to fire the missile
    
You Miss: Enemy Ship was not there
    
A Direct Hit: A part of enemy's ship has been hit
    
A ship has sunk: All of the ship's coordinate has been hit and one of the ship has sunk.''')
        talk('''Call Your shot: Guess where the opponent ship is. Enter the coordinate(row,column) where you want to fire the missile
    
You Miss: Enemy Ship was not there
    
A Direct Hit: A part of enemy's ship has been hit
    
A ship has sunk: All of the ship's coordinate has been hit and one of the ship has sunk.''')
        i=input("Press Enter")
        print()
        print('''How to win: Each player alternately fires missiles until all the enemy ship has sunk. When that happens the game ends.
    
HOPE YOU ENJOY THE GAME''')
        talk('''How to win: Each player alternately fires missiles until all the enemy ship has sunk. When that happens the game ends.
    
HOPE YOU ENJOY THE GAME''')
        i=input("Press Enter")
    else:
        print("INVALID SELECTION")
        talk("INVALID SELECTION")
        extra=input("Press Enter")
