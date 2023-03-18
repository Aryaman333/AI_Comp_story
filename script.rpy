# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")

# $john = Character("John", image='C:\Users\HP\Downloads\Test_file\game\images\john.jpg')
# The game starts here.
$player = ""



label john_question():
    $john = Character("John", image='john.jpg')
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


label shubh_question():
    $shubh = Character("Shubh", image='shubh.jpg')
    show shubh at left
    shubh "What time do you usually go to bed and wake up?"

    menu:       
        "I like to get to bed early and wake up early, so I'm usually asleep by 10 pm and up by 6 am.":
            # call the corresponding cif action  
            jump after7

        "I'm a bit of a night owl and usually stay up until midnight or later, but I can keep the noise down if my roommate goes to bed earlier.":
            # call the corresponding cif action  
            jump after7 

        "I don't have a set sleep schedule, it varies depending on my workload and social plans.
":
            # call the corresponding cif action  
            jump after7               

    label after7:
        "Got it!"


    shubh "How do you feel about having guests over?"
    menu:       
        "I love having friends over and hosting small gatherings occasionally, but I always give my roommate a heads up and make sure they are comfortable with it.":
            # call the corresponding cif action  
            jump after8

        " I don't like having guests over very often and would prefer to keep the apartment a more private space for just my roommate and me.":
            # call the corresponding cif action  
            jump after8           
        
        "I'm okay with having guests over occasionally, but I prefer to keep things low-key and not have big parties or events.":
            # call the corresponding cif action  
            jump after8        
            
    label after8:
        shubh"Got it!"

    shubh "How often do you clean up after yourself?"
    menu:       
        "I like to keep things neat and tidy and clean up after myself as I go along throughout the day.":
            # call the corresponding cif action  
            jump after9

        " I tend to be a bit messy, but I always make sure to clean up after myself before going to bed.":
            # call the corresponding cif action  
            jump after9           
        
        "I don't have a set cleaning schedule, but I always make sure to clean up after myself when things start to get messy.":
            # call the corresponding cif action  
            jump after9        
            
    label after9:
        shubh "Got it!"


    shubh "What are some of your hobbies?"
    menu:       
        "I enjoy going to the gym and staying active, so I often go for runs or work out in the apartment.":
            # call the corresponding cif action  
            jump after10

        "I'm a bit of a homebody and enjoy watching movies and TV shows in my free time.":
            # call the corresponding cif action  
            jump after10

        "I like to play music and write songs, but I always use headphones so as not to disturb my roommate.":
            # call the corresponding cif action  
            jump after10                
      
            
    label after10:
        shubh "Got it!"

    shubh "How do you feel about noise levels in the apartment?"
    menu:       
        "I don't mind some background noise, and I'm always up for having a good time with my roommate and their friends.":
            # call the corresponding cif action  
            jump after11

        "I prefer a quieter living environment and would appreciate it if my roommate kept noise levels down, especially late at night.":
            # call the corresponding cif action  
            jump after11

        "As long as the noise is reasonable and respectful of others' needs, I don't have a strong preference either way.":
            jump after11           
      
            
    label after11:
        shubh "Got it!"

    shubh "How do you feel about sharing food or cooking together?"
    menu:       
        " I love cooking and would be happy to share meals or cook together with my roommate.":
            # call the corresponding cif action  
            jump after12

        "I prefer to cook for myself and wouldn't want to share food, but I'm okay with occasionally cooking at the same time.":
            # call the corresponding cif action  
            jump after12

        " I don't cook very often and usually just order takeout, so I don't have a strong preference either way.":
            jump after12           
      
            
    label after12:
        shubh "Got it!"

        return
    
    return 
label rahul_question():
    $rahul = Character("Rahul", image='rahul.jpg')
    show rahul at left
    rahul "The leasing rate for the room will be USD 1000. Are you okay with the cost?"

    menu:       
        "Yes sure no problem sounds fine":
            # call the corresponding cif action  
            jump after13

        "Yea about that , can I get a slight reduction in that if possible.":
            # call the corresponding cif action  
            jump after13 

        "Oh that seems really high and out of my budget can you please give an exemption like for the first few months.":
            # call the corresponding cif action  
            jump after13               

    label after13:
        "Got it!"


    rahul "Who is your favorite actor?"
    menu:       
        "Obviously not even a question it has to be Shahruk Khan, the king, his wit his charm his range of expressions, his versatility is of top class":
            # call the corresponding cif action  
            jump after14

        "I dont watch a lot of movies, I am boring that way.":
            # call the corresponding cif action  
            jump after14           
        
        "Dont have particular preference, I like good production over good actors.":
            # call the corresponding cif action  
            jump after14        
            
    label after14:
        rahul"Got it!"

    rahul "How often do you party and mind patries in your household?"
    menu:       
        "I love parties , I party every weekend sometimes for 2-3 days straight":
            # call the corresponding cif action  
            jump after15

        "I like them,never hosted one but always up for one.":
            # call the corresponding cif action  
            jump after15           
        
        "I usually dont party that much I like studying at night and prefer silence while doing so.":
            # call the corresponding cif action  
            jump after15        
            
    label after15:
        rahul "Got it!"


    rahul "How often do you cook ?"
    menu:       
        "I usually dont cook that much.":
            # call the corresponding cif action  
            jump after16

        "I love cooking now and then":
            # call the corresponding cif action  
            jump after16

        "I only eat home cooked food and we can even cook together":
            # call the corresponding cif action  
            jump after16                
      
            
    label after16:
        rahul "Got it!"

    rahul "Is cleanliness important for you "
    menu:       
        "Yea i keep my room very clean and expect the house to be clean as well and will regularly clean the house":
            # call the corresponding cif action  
            jump after17

        "Yeah I am a person who is not very particular but will keep my things clean.":
            # call the corresponding cif action  
            jump after17

        "We can hire a maid":
            jump after17           
      
            
    label after17:
        rahul "Got it!"

    rahul "Do you own a vehicle"
    menu:       
        "Yes I have a car that I will use to commute to college":
            # call the corresponding cif action  
            jump after18

        "I have a bike":
            # call the corresponding cif action  
            jump after18

        "I don’t currently, I haven’t figured out how i will commute to college yet":
            jump after18           
      
            
    label after18:
        rahul "Got it!"

    rahul "How long are you thinking of leasing the apartment?"
    menu:       
        "3 months":
            # call the corresponding cif action  
            jump after19

        "4 years":
            # call the corresponding cif action  
            jump after19

        "1 year":
            # call the corresponding cif action 
            jump after19          
      
            
    label after19:
        rahul "Got it!"    

        return
    
    return         




label john_intro():
    $john = Character("John", image='john.jpg')
    show john at left
    john "Hello [player] how are you doing today, I am really excited to meet you and talk to you"
    hide john
    return

label rahul_intro():
    $rahul = Character("Rahul", image='rahul.jpg')

    show rahul at left
    rahul "Hello [player]  I am Rahul, you must have heard my name I am quite famous, Lets finish this up quickly I have to meet Anjali my girlfriend"

    hide rahul
    return

label shubh_intro():
    $shubh = Character("Shubh", image='shubh.jpg')

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
    if choice == 1:
        call john_question()

    elif choice == 2:
        call shubh_question()
    elif choice == 3:
        call rahul_question()    

    
    
    # if choice==1:
    #     show



    # This ends the game.

    return
        
        

      






   

   
