# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")

# $john = Character("John", image='C:\Users\HP\Downloads\Test_file\game\images\john.jpg')
# The game starts here.
$player = ""



label john_question():
    $john = Character("John", image='C:\Users\HP\Downloads\Test_file\game\images\john.jpg')
    show john at left
    john "How often do you clean your room in general?"
    menu:       
        "Everyday after work, I cant focus in a messy room":
            # call the corresponding cif action  
            jump after

        "Twice in a week, I am mostly engaged in work but I cant work sitting in a mess, so i clean often":
            # call the corresponding cif action  
            jump after           
      
        "Rarely(once in a week), I stay outdoors most of the time, Anyways we have to use the room mostly for sleeping":
            # call the corresponding cif action  
            jump after         

    label after:
        "Got it!"


    john "Do you smoke btw?"
    menu:       
        "No, I don’t smoke, I’m actually allergic to it and can’t imagine living with someone who does smoke":
            # call the corresponding cif action  
            jump after1

        "I smoke occasionally, I am not addicted to it, I just enjoy it occasionally as in a party or something ":
            # call the corresponding cif action  
            jump after1           
        
        "Yeah, I’m a chain smoker, I totally understand if anyone living with me is uncomfortable with it, tho i don’t smoke in the shared space.  ":
            # call the corresponding cif action  
            jump after1        
            
    label after1:
        john"Got it!"

    john "What are your thoughts about Private Space"
    menu:       
        "I am a very private person and respect people who know the value of it.":
            # call the corresponding cif action  
            jump after2

        "I respect privacy when there is work going on, Usually tho I like getting along with my  roommate and would like living with someone who is outgoing ":
            # call the corresponding cif action  
            jump after2           
        
        "I am an extroverted person and would like to live when me and my roommate can support each other in work and organize some parties.":
            # call the corresponding cif action  
            jump after2        
            
    label after2:
        john "Got it!"


    john "What are your thoughts about Respectfulness"
    menu:       
        " I value mutual respect and would always avoid unnecessary arguments and prefer peacefully sorting out even if something happens":
            # call the corresponding cif action  
            jump after3

        "I obviously value mutual respect, I don’t cause any trouble to anyone as long as they are not bothering me, However, if there is some argument sometime, I like to make things clear with my expectations to avoid the same in future.":
            # call the corresponding cif action  
            jump after3           
      
            
    label after3:
        john "Got it!"

    john "How do you feel about noise levels in the apartment?"
    menu:       
        "I don't mind some background noise, and I'm always up for having a good time with my roommate and their friends.":
            # call the corresponding cif action  
            jump after4

        "I prefer a quieter living environment and would appreciate it if my roommate kept noise levels down, especially late at night.":
            # call the corresponding cif action  
            jump after4

        "As long as the noise is reasonable and respectful of others' needs, I don't have a strong preference either way.":
            jump after4           
      
            
    label after4:
        john "Got it!"

    john " How do you feel about splitting household chores with your roommate?"
    menu:       
        " I am happy to divide chores equally and make a schedule so that everything gets done efficiently and fairly.":
            # call the corresponding cif action  
            jump after5

        "I prefer to take care of my own messes and would rather not be responsible for my roommate's chores or vice versa.":
            # call the corresponding cif action  
            jump after5

        " I am open to discussing chore responsibilities with my roommate and finding a system that works for both of us.":
            jump after5           
      
            
    label after5:
        john "Got it!"

    john " What is your stance on having pets in the apartment?"
    menu:       
        "  I love animals and would be open to having a pet in the apartment, as long as my roommate is comfortable with it and we both agree on the type and care of the pet.":
            # call the corresponding cif action  
            jump after6

        "I am not a pet person and would prefer not to have any pets in the apartment.":
            # call the corresponding cif action  
            jump after6

        " I am open to discussing the possibility of having a pet in the apartment with my roommate and finding a solution that works for both of us.":
            jump after6           
      
            
    label after6:
        john "Got it!"

        return
    
    return 




label john_intro():
    $john = Character("John", image='C:\Users\HP\Downloads\Test_file\game\images\john.jpg')
    show john at left
    john "Hello [player] how are you doing today, I am really excited to meet you and talk to you"
    hide john
    return

label rahul_intro():
    $rahul = Character("Rahul", image='C:\Users\HP\Downloads\Test_file\game\images\rahul.jpg')

    show rahul at left
    rahul "Hello [player]  I am Rahul, you must have heard my name I am quite famous, Lets finish this up quickly I have to meet Anjali my girlfriend"

    hide rahul
    return

label shubh_intro():
    $shubh = Character("Shubhankar", image='C:\Users\HP\Downloads\Test_file\game\images\shubh.jpg')

    show shubh at left
    shubh "Yo [player]  how is it hanging, Hope you are not a phsycopath like the the last guy I interviewed, lets get started shall we"
    hide shubh
    return
   


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene hall1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    


    # These display lines of dialogue.

    "Welcome to the Roomate Finder Game, lets find a roomate real fast, 
    the next quarter is upon us you dont want to be stuck at your aunt's place do you !!!"

    # "What is your name"

    # "Welcome Piyush !! lets get started"
    # image john = "images/john.jpg"
    # init:
    #     $ john = Character("John", image=john, xpos=0.2, ypos=0.5)

    $ player = renpy.input("Enter your name:")

    "Welcome [player] !! lets get started"

    "Its time to meet the characters"



    


    # show rahul at left
    # rahul "Hello [player]  I am Rahul, you must have heard my name I am quite famous, Lets finish this up quickly I have to meet Anjali my girlfriend"

    # hide rahul

    # show shubh at left
    # shubh "Yo [player]  how is it hanging, Hope you are not a phsycopath like the the last guy I interviewed, lets get started shall we"

    # hide shubh

    call john_intro()
    call shubh_intro()
    call rahul_intro()
    $choice=0
    $choice = int(renpy.input(" You can now choose which roomate you "))
    
    
    "Cool, you chose option [choice] "
    call john_question()
    
    # if choice==1:
    #     show



    # This ends the game.

    return
