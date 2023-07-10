# Write your code to expect a terminal of 80 characters wide and 24 rows high
#1234567891123456789212345678931234567894123456789512345678961234567897123456789

def welcome_to_game():
    print("\nWelcome to Space and Beyond!")
    print("           -------------" )
    art = '''
                _____
             ,-"     "-.
            / o       o \\
           /   \\     /   \\
          /     )-"-(     \\
         /     ( 6 6 )     \\
        /       \\ " /       \\
       /         )=(         \\
      /   o   .--"-"--.   o   \\
     /    I  /  -   -  \\  I    \\
 .--(    (_}y/\\       /\\y{_)    )--.
(    ".___l\\/__\\_____/__\\/l___,"    )
 \\                                 /
  "-._      o O o O o O o      _,-"
      `--Y--.___________.--Y--'
         |==.___________.==| hjw
         `==.___________.==' `97
    '''
    print(art)
    start_game()


def start_game():
    art = '''
     ~+

                 *       +
           '                  |
       ()    .-.,="``"=.    - o -
             '=/_       \     |
          *   |  '=._    |
               \     `=./`,        '
            .   '=.__.=' `='      *
   +                         +
        O      *        '       .

    '''
    print("You are a space explorer on a mission to discover hidden galaxies \n on the outer reaches of the universe...\n")
    print("You will be presented with numerous challenges and choices...")
    print("\nYour decisions will determine your fate...so choose wisely\n Good Luck!")
    print("           -------------" )
    print(art)
    chapter_one()

def chapter_one():
    print("Chapter 1: The Strange Galaxy")
    print("           -------------" )
    print("\nYou wake from hypersleep to find yourself in a strange galaxy")
    print("Your navigation system is malfunctioning- you need to act fast!\n You have two choices: \n")
    print("1. Head towards the rainbow star cluster.")
    print("2. Follow the gravitational pull of a nearby planet.\n")
    choice = input("Enter your choice (1 or 2):")
    
    if choice == "1":
        print("You have chosen to direct the craft towards the rainbow star cluster\n")
        chapter_2()

    elif choice == "2":
        print("You follow the gravitational pull of a nearby monster planet\n")
        print("As you near the planet you realize with horror that it is a black hole!\n")
        print("Your ship has been sucked into oblivion")
        game_over()
    else:
        print(f"You entered {choice}. This is an invalid choice, please choose either 1 or 2!\n")
        chapter_one()

def chapter_2():
    print("You have reached chapter 2\n The Mysterious Planet")
    print("You arrive at the star cluster and find a lush planet, covered in vegetation")
    print("You can choose to:")
    print("\n1. Explore the forest")
    print("\n2. Search the plains for signs of intelligent life")
    choice = input("Enter your choice (1 or 2):")

    if choice == "1":
        print("You have chosen to explore the forest\n")
        print("After several hours of searching you become disoriented and lost/n")
        print("Your remains are found by an explorer from the planet Zlog many aeons later")
        game_over()
    elif choice == "2":
        print("You set off in search of intelligent life\n")
        print("You encounter an ancient temple and manage to decipher the entry code\n")
        print("The heavy stone doors grind open")
        chapter_3()
    else:
        print(f"You entered {choice}. This is an invalid choice, please choose either 1 or 2!\n")
        chapter_2()

def game_over():
    art = '''
  _____          __  __ ______    ______      ________ _____  
 / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
| |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
| | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
| |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
 \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
    '''
    print(art)
    restart = input("Would you like to try again? : (y or n)\n")
    if restart.lower() == "y":
        print("You have decided to try again- godspeed!\n ")
        start_game()
    else:
        print("Thank you for playing Space and Beyond!")
        print("\n May we meet again somewhere sometime in space and beyond!!")
    



welcome_to_game()

