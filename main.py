import signup           #import from signup file                 
import login            #import from login file
import game         #import from game file

status = False
print("HACHY'S SUDOKU GAME, Are you new? Y/N")
ans = input()
if ans == "Y":          
    print("enter a username")       #enter the username you wish to use and password
    user = input()
    print("enter a password")
    password = input()
    signup.signup_function(user,password)           #uses the sign up function imported to document your credentials
    status = True

    pass

if ans == "N":
    print("OKAY! enter your username")
    user = input()      #enter your user name and password so they can be verified by the login function that is imported
    print("password")
    password = input()
    if login.login_function(user,password) == True:     #if the credentials match the documented credentials then status is true
        print("welcome player")
        status = True
    else:
        print("username or password incorrect, please try again")       #if the credentials are incorrect this message will print and you wont be allowed to proceed further because status is FALSE
        status = False
    pass

if status == True:
    print("Press enter to start game")
    resp = input()
    if resp == "":
        game.playgame()
        pass