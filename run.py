# Write your code to expect a terminal of 80 characters wide and 24 rows high
#1234567891123456789212345678931234567894123456789512345678961234567897123456789

def welcome_to_game():
    print("\nWelcome to Space and Beyond!")
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

def chapter_one():
    
    
    

welcome_to_game()

