#### CMPT 120 - D200
#### Jaekang Lee #301314388
#### Jeff Wang #301309384



#1. TEXT (localList)
def read_string_list_from_file(the_file):  
    fileRef = open(the_file,"r") 
    localList=[]
    for line in fileRef:
        string = line[0:len(line)-1]                       
        localList.append(string)  
    fileRef.close()  
    return localList 



#2. BOARD LISTS (listall)
def create_lists_board(listStrings): 
    listall = []
    for i in range(len(listStrings)):
        listsome = []
        st = ""
        for k in range(len(listStrings[i])):
            if(listStrings[i][k].isdigit()):
                st = st + listStrings[i][k]
            else:    
                listsome.append(int(st))
                st = ""
        listsome.append(int(st))
        listall.append(listsome)
    return(listall) 



#3. SHOW LIST (print)
def show_board(li,title,ast): ##Recieves integer list, title, and astronaut position
    print ("\nShowing board... " + title)
    print ("\n The board at this point contains...")
    print("    Planet#   CivLevel    Fuel    Rocks")
    for i in range(len(li)):
        print(" "*6,i," "*(10-len(str(i))), end="")
        for k in range(len(li[i])):
            print(str(li[i][k]) +" "*(8-len(str(li[i][k]))), end="")
        if(pythonP !=0 and pythonP ==i and PythonP==True):
            print("<=== PythonPlanet ", end="")
        if(ast == i):
            print("<--- Astronaut", end="")
        print()
    return()



#4. TITLE MESSAGE (print)
def show_ast(title): 
    print ("\nShowing astronaut ... " + title)
    print("\nThe astronaut", name, "has civilization level", CivLevel)
    print("is in  position:", Place)
    print("currently has:", FuelLevel, "fuel liter(s)")
    print("and collected until and including this turn", Rock, "rock specimen(s)")
    #Game ended due to turns
    if(title == "end of game"):
        print("So... he is...very alive!!!")
        print("and he cannot move anymore since the game ended!")
    #Game ended due to fuel
    elif(title == "end of game "):                                
        print("So... he is...stranded or dead ... oh no!!!")
        print("and he cannot move anymore since the game ended!")
    #Game ended due to python planet
    elif(title == "end of game  "):                               
        print("So... he is...very alive!!!")
        print("and also he reached PythonPlanet, so he won!!!")
    #Game ended due to explosion
    elif(title=="end of game    "):                                                       
        print("So he died")
    #Game doesnt end, keeps going
    else:
        print("So... he is...very alive!!!")
        print("and also ready to keep moving!")
    return()


#5. END OF TURN (print)
def show_end(message,num): 
    print("\n RESULTS END OF GAME")
    print("\nThe game number", AllGames, "just took place")
    print(message)
    show_board(biglist,"end of game",Place)
    if(num == 1):
        show_ast("end of game")
    elif(num == 2):
        show_ast("end of game ")
    elif(num == 3):
        show_ast("end of game  ")
    elif(num == 4):
        show_ast("end of game    ")
    return()



#6. GAME OVER  (print)
def show_GameOver():
    rocklist = getRock()
    binarylist = getBinary(rocklist)
    dec = convert_binary(binarylist)
    print("\n RESULTS END OF ALL GAMES...........")
    print("\n The user played", AllGames, "game(s) in total\n of those, the astonaut won", wins)
    print(" To conclude, the program will do a conversion from binary to decimal!\n taking as source the  list of rock specimens in the last game board")
    print("\n  List with rock specimens:", rocklist)
    print("  Corresponding Binary:", binarylist)
    print("  which converted to decimal is:", dec)
    print("\n\nBye....")
    return()



#7. ROCK (rocks)
def getRock():
    rocks = []
    for i in range(len(biglist)):
        rocks.append(biglist[i][2])
    return(rocks)



#8. ROCK 2 (res)
def getBinary(li):
    res = []
    for i in range(len(li)):
        res.append(li[i]%2)
    return(res)


#9.0 BINARY LIST
def convert_binary(ls):
    res=0
    for i in range(len(ls)):
        if ls[i]==1:
            value=2**(len(ls)-i-1)
            res=res+value
    return res


#9. BINARY LIST (val)
def getDec(binary_as_list):
	val = 0
	for i in range(0,len(binary_as_list)):
		val = val + binary_as_list[i]*pow(2,(len(binary_as_list) -1- i))
	return val



#10. Y/N (T/F)
def checkTwo(message,a,b):
    choice = input(message)
    while (choice.upper() != a and choice.upper() != b):
        print("What you typed is not what is expected, please retype ")
        choice = input(message)
    return(choice.upper() == a) 



#11. RETYPE (choice)
def checkRange(message,small,big): 
    choice = input(message)
    while (choice.isdigit() == False or int(choice) < small or int(choice) > big):
        if (choice.isdigit() == False):
            print("What you typed is not a positive integer, please retype")
        else:
            print("The value is not within the required range, retype")
        choice = input(message)
    return(int(choice)) 



#12. DICE (newplace)
def RollDice():
    roll = random.randint(1, 6)
    print("\n\nthe die was...", roll)
    print("the previous position was...", Place)
    newplace = Place + roll
    if(newplace>=len(biglist)):
        newplace = newplace-len(biglist)
    print("and the next position is...", newplace)
    print()
    return(newplace) 



#13. COLLECTING (fuel)
def onPlanet(fuelhave): 
    fuel = fuelhave
    rand = random.randint(1,FuelLevel)
    gains = 0
    print("\nThere are aliens in this planet!! with civilization level", biglist[Place][0])
    #player>alien
    if(CivLevel>biglist[Place][0]):   
        rand = 0
        if(biglist[Place][1]>0):
            gains = random.randint(1,biglist[Place][1])           
        biglist[Place][1] = biglist[Place][1] - gains
        print("Great! the astronaut is more civilized than the aliens!")
        print("The astronaut won", gains, "fuel liter(s)")
        print("the planet",Place, "now has",biglist[Place][1] , "fuel liter(s)")
    #player=alien
    elif(CivLevel==biglist[Place][0]):
        print("Oh well... the astronaut is equally civilized as the aliens")
        rand = rand//2
        print("  but lost", rand, "fuel liter(s)")
    #player<alien
    else:
        print("\nOh No! the astronaut is less civilized than the aliens and lost", rand, "fuel liter(s) !")
    fuel = fuel - rand + gains 
    print("\nThe astronaut now has", fuel, "fuel liter(s)")
    #fuel=0
    if(fuel < 1):
        print("\nOh! The astronaut is stranded so he does not collect rocks")
    #alien=0
    else:
        collected = biglist[Place][2]//3
        biglist[Place][2] = biglist[Place][2] - biglist[Place][2]//3
        Rock.append(collected)
        print("\nYey!!...  the astronaut collected", collected, "rock(s)")
        print("\nhis rock collection is now", Rock)
        print("the planet", Place, "now has", biglist[Place][2], "rock(s)")    
    return(fuel)


#14. TURTLE (STAR)
def star(length):
    for i in range (5):
        t.fd(length)
        t.rt(144)
    t.fd(length)

        
#15. TURTLE (STAR WITH COLOR)
def star_color(length,color):
    t.fillcolor(color)
    t.begin_fill()
    star(length)
    t.end_fill()
    return


#16. TURTLE (BOARD)
def draw_board(length,color,L):
    for i in range(L):
        star_color(length,color)
    t.rt(180)
    t.fd(75*(len(biglist)-pythonP))
    t.lt(180)
    if PythonP==True:
        star_color(75,'light blue')
    t.home()
    t.penup()
    t.right(90)
    t.fd(100)
    t.lt(90)

#18. TURTLE (POS 0)
def draw_player(n):
    t.fd(75/2+75*(n+1))
    t.pendown()
    t.pencolor('green')
    t.circle(25)
    t.penup()
    t.pencolor('black')
    t.home()
    return
    

#18. TURTLE (PLAYER POSITION2)
def draw_player2(n):
    if n>len(biglist)-1:
        n=n-1
    t.fd(75/2+75*(n))
    t.pendown()
    t.pencolor('green')
    t.circle(25)
    t.penup()
    t.pencolor('black')
    t.home()
    return


#19. MILD EXPLOSION
def milda(n):
    if n>2:
        biglist[n-1][2]=biglist[n-2][2]+biglist[n-1][2]
        biglist[n-2][2]=biglist[n-1][2]+biglist[n][2]
    if n==1:
        biglist[len(biglist)-1][2]=biglist[len(biglist)-1][2]+biglist[1][2]
    return biglist
        

#####################
##### TOP LEVEL #####
#####################


import random 
import turtle as t          
print(" Welcome to the Planet, Aliens and Explosions CMPT 120 Game!")
print("="*61)


draw=checkTwo("\nDo you want to draw the board (for all games)? (y/n): ","Y","N")

if(checkTwo("\nDo you want to play? (y/n): ","Y","N") == True):
    AllGames = 0
    wins = 0
    Gameover = False

    #GAME
    while(Gameover == False):
        AllGames = AllGames + 1
        choice = input("\nType the name of board file including '.txt' or type d for default: ")
        if(choice == "d"):
            listStrings = read_string_list_from_file("planetsData1.txt")
        else:
            listStrings = read_string_list_from_file(choice)

        #BOARD
        biglist = create_lists_board(listStrings)
        Place = -1
        pythonP = 0
        show_board(biglist,"just created",Place)
        pythonP = checkRange("\nWhich position shall PythonPlanet be (0," +str(len(biglist)-1) +"), 0 no effect: ",0 ,len(listStrings)-1)
        turn=1
        PythonP=True

        #TURTLE (BEGINNING BOARD)
        run_once=0
        while run_once!=1:
            if run_once==0:
                t.clear()
                L=len(biglist)
                N=Place
                if draw:
                    draw_board(75,'pink',L)
                    draw_player(N)
            run_once=1
            
            
        #USER INPUT
        print("\nData for astronaut/player\n")
        name = input("Name? ")
        CivLevel = checkRange("Civilization level (0..3)? ",0 ,3 )
        FuelLevel = checkRange("Initial fuel liters (10..50)? ",10 ,50 )
        MaxTurns = checkRange("\nMaximum turn(s) this game? (1..10) ",1 ,10 )
        amazing=checkTwo("\nAllow that Amazing Explosions happen? (y/n): ","Y","N")
        if(amazing==False):
            mild=checkTwo("\nSince you do not want amazing explosions to happen would you allow that Mild Explosions happen? (y/n): ","Y","N")
        


        
        Place = 0
        Rock = []
        dead = False

        #NEXT TURN
        while(turn <= MaxTurns and dead == False): 
            show_board(biglist,str(turn),Place)
            show_ast("about to do turn num: " +str(turn))
            print("\n\n")

            #EXPLOSION THIS TURN?
            if (amazing or mild):
                A=len(biglist)
                kaboom=random.randint(1,A*5)
                if kaboom>0 and kaboom<A:
                    print("Oooooh!! A mild or amazing explosion is happening in planet #",kaboom)
                    print("the board will have more rock specimens!")
               


                   #AMAZING EXPLOSION
                    if  amazing:
                        print("Oh oh! An amazing explosion occured in planet#",kaboom)
                        print("This planet will dissapear! \n and the board shrunk")            
                        if kaboom==Place:
                            dead=True
                            print("and the astronaut was there!! and died!!")
                            show_end("Astronaut died on due to the explosion",4)
                            break
                        else:
                            print("but the astronaut was not there and it did not affect his position...")
                        milda(kaboom)
                        biglist.remove(biglist[kaboom])


                        #IF PYTHONPLANET = KABOOM
                        if pythonP==kaboom:
                            PythonP=False
                        else:
                            pythonP=pythonP-1

                        
                        print("Showing board... after amazing explosion, still in turn num:",turn)
                        if Place>kaboom:
                            Place=Place-1
                        show_board(biglist,str(turn),Place)
                        


                    #MILD EXPLOSION
                    if not amazing and mild:
                        print("Showing board... after mild explosion, still in turn num:",turn)
                        milda(kaboom)
                        show_board(biglist,str(turn),Place)
                        


                #NO EXPLOSION THIS TURN
                else:
                    print ("There was an amazing explosion, but in another galaxy \n Nothing happened in our board")

            
                #TURTLE  (AFTER AMAZING EXPLOSION + BEFORE PLAYER MOVES)
                if draw and amazing and kaboom>0 and kaboom<A:
                    t.home
                    t.clear()
                    L=len(biglist)
                    M=Place
                    t.pencolor('black')
                    draw_board(75,'pink',L)
                    draw_player2(M)
                    
                
            #DICE?
            if(checkTwo("\nRoll die, or user types next pos? (d/u): ","D","U")):
                Place = RollDice()
            else:
                Place = checkRange(" which planet should the astronaut go? (0.." +str(len(biglist)-1) +"): ", 0, len(biglist)-1)

            #PYTHON PLANET
            if(Place == pythonP and Place != 0):
                dead = True
                wins = wins + 1
                FuelLevel = 9999
                Rock = 9999
                print("\nAmazing! the player is in PythonPlanet and won the game!")
                show_end("The game ended because the astronaut won",3)

            #NORMAL PLANET
            else:
                FuelLevel = onPlanet(FuelLevel)
                turn = turn + 1

            #FUEL CHECK
            if(FuelLevel < 1):
                dead = True
                show_end("The game ended because the astronaut got stranded or died",2)

            #TURTLE  (END OF THE TURN)
            if draw:
                t.home
                t.clear()
                L=len(biglist)
                M=Place
                t.pencolor('black')
                draw_board(75,'pink',L)
                draw_player2(M)
                
        #NO TURNS LEFT
        if(turn > MaxTurns and FuelLevel > 0):
            show_end("The game ended because the max number of turns were played",1)

        #PLAY AGAIN?
        if(checkTwo("\nDo you want to play again? (y/n): ","Y","N")==False):
            Gameover = True
        
    #GAME OVER
    show_GameOver()


    
else:
    print("Maybe you will want to play some other time? \n\nBye...")
