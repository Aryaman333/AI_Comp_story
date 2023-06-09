﻿
$player = ""

$import renpy.video

# Server details 
init python:
    import requests
    import json
    BASE_URL = 'http://localhost:8081/'
    headers = {
        'Content-Type': 'application/json',
    }


# The following is the label for John's questionaire
label john_question():
    # Shows the character
    $john = Character("John", image="john.jpg")
    scene hall1:
        xzoom 2.0
        yzoom 1.5
    play music r'audio/audio_john.mp3' loop
    show john:
        xalign 0.0
        yalign 1.0
    
    john " Hi [player] Let me give you a quick room tour before I jump to the questions, hope you have forgiven me for being rude to you on first day of college, I was having a bad day!"
    #displays the character's hall
    $renpy.movie_cutscene("house1.webm")
    john "Hope you liked the place lets jump to the questions real quick"
    john "How often do you clean your room in general?"
    menu:       
        "Everyday after work, I cant focus in a messy room":
            # call the corresponding cif action 
            call call_action("IncScoreJohn")
            call call_action("IncScoreJohn")
            jump after

        "Twice in a week, I am mostly engaged in work but I cant work sitting in a mess, so i clean often":
            # call the corresponding cif action  
            call call_action("IncScoreJohn")
            jump after           
      
        "Rarely(once in a week), I stay outdoors most of the time, Anyways we have to use the room mostly for sleeping":
            # call the corresponding cif action  
            call call_action("DecScoreJohn")
            jump after         

    label after:
        "Got it!"


    john "Do you smoke btw?"
    menu:       
        "No, I don’t smoke, I’m actually allergic to it and can’t imagine living with someone who does smoke":
            # call the corresponding cif action  
            
            call call_action("IncScoreJohn")
            jump after1

        "I smoke occasionally, I am not addicted to it, I just enjoy it occasionally as in a party or something ":
            # call the corresponding cif action  
            jump after1           
        
        "Yeah, I’m a chain smoker, I totally understand if anyone living with me is uncomfortable with it, tho i don’t smoke in the shared space.  ":
            # call the corresponding cif action  
            call call_action("DecScoreJohn")
            jump after1        
            
    label after1:
        john"Good to know!"

    john "What are your thoughts about Private Space"
    menu:       
        "I am a very private person and respect people who know the value of it.":
            call call_action("IncScoreJohn")
            # call the corresponding cif action  
            jump after2

        "I respect privacy when there is work going on, Usually tho I like getting along with my  roommate and would like living with someone who is outgoing ":
            # call the corresponding cif action  
            call call_action("IncScoreJohn")
            jump after2           
        
        "I am an extroverted person and would like to live when me and my roommate can support each other in work and organize some parties.":
            # call the corresponding cif action  
            call call_action("DecScoreJohn")
            jump after2        
            
    label after2:
        john "Thanks for answering that, that very important for me"


    john "What are your thoughts about Respectfulness"
    menu:       
        " I value mutual respect and would always avoid unnecessary arguments and prefer peacefully sorting out even if something happens":
            # call the corresponding cif action  
            call call_action("IncScoreJohn")
            jump after3

        "I obviously value mutual respect, I don’t cause any trouble to anyone as long as they are not bothering me, However, if there is some argument sometime, I like to make things clear with my expectations to avoid the same in future.":
            # call the corresponding cif action  
            call call_action("IncScoreJohn")
            call call_action("IncScoreJohn")
            jump after3           
      
            
    label after3:
        john "Got it"

    john "How do you feel about noise levels in the apartment?"
    menu:       
        "I don't mind some background noise, and I'm always up for having a good time with my roommate and their friends.":
            # call the corresponding cif action  
            call call_action("DecScoreJohn")
            jump after4

        "I prefer a quieter living environment and would appreciate it if my roommate kept noise levels down, especially late at night.":
            # call the corresponding cif action  
            call call_action("IncScoreJohn")
            jump after4

        "As long as the noise is reasonable and respectful of others' needs, I don't have a strong preference either way.":
            call call_action("IncScoreJohn")
            jump after4           
      
            
    label after4:
        john "Hmmm... Interesting"

    john " How do you feel about splitting household chores with your roommate?"
    menu:       
        " I am happy to divide chores equally and make a schedule so that everything gets done efficiently and fairly.":
            # call the corresponding cif action 
            call call_action("IncScoreJohn")
            call call_action("IncScoreJohn")

            jump after5

        "I prefer to take care of my own messes and would rather not be responsible for my roommate's chores or vice versa.":
            # call the corresponding cif action  
            call call_action("DecScoreJohn")
            jump after5

        " I am open to discussing chore responsibilities with my roommate and finding a system that works for both of us.":
            call call_action("IncScoreJohn")
            jump after5           
      
            
    label after5:
        john "Okkk.. "

    john " What is your stance on having pets in the apartment?"
    menu:       
        "  I love animals and would be open to having a pet in the apartment, as long as my roommate is comfortable with it and we both agree on the type and care of the pet.":
            # call the corresponding cif action 
            call call_action("IncScoreJohn") 
            jump after6

        "I am not a pet person and would prefer not to have any pets in the apartment.":
            # call the corresponding cif action
            call call_action("DecScoreJohn")  

            jump after6

        " I am open to discussing the possibility of having a pet in the apartment with my roommate and finding a solution that works for both of us.":
            call call_action("IncScoreJohn")
            jump after6           
      
            
    label after6:
        john "Ahh.. nicee"

    hide hall1
    hide john
    show ucdavis:
        xzoom 1  
        yzoom 1
    return 


# The following is the Anya's questionaire
label anya_question():
    play music r'audio/audio_anya.mp3' loop
    #displaying character's image
    $anya = Character("Anya", image='anya.jpg')
    scene hall2:
        xzoom 5
        yzoom 4
    show anya:
        xalign 0.0
        yalign 1.0
    anya "Hi buddy welcome to my humble aboard, hopefully you like it, seeing you after such a long time brings back so many highschool memories let me ask some routine questions you know how it is, so here goes"
    anya " Let me give you a quick room tour before I jump to the questions"
    $renpy.movie_cutscene("guitar.webm")
    anya "Ok that was my place hope you liked it lets get started then..."
    anya "What time do you usually go to bed and wake up?"
    # Menu for showing questions
    menu:       
        "I like to get to bed early and wake up early, so I'm usually asleep by 10 pm and up by 6 am.":
            # call the corresponding cif action  
            call call_action("IncScoreShubh")
            call call_action("IncScoreShubh")
            jump after7

        "I'm a bit of a night owl and usually stay up until midnight or later, but I can keep the noise down if my roommate goes to bed earlier.":
            # call the corresponding cif action  
            call call_action("IncScoreShubh")
            jump after7 
            

        "I don't have a set sleep schedule, it varies depending on my workload and social plans.":
            # call the corresponding cif action 
            call call_action("decScoreShubh") 
            jump after7
                          

    label after7:
        anya"That was a little personal, but that information helps"


    anya "How do you feel about having guests over?"
    menu:       
        "I love having friends over and hosting small gatherings occasionally, but I always give my roommate a heads up and make sure they are comfortable with it.":
            # call the corresponding cif action  
            
            call call_action("IncScoreShubh")
            jump after8

        " I don't like having guests over very often and would prefer to keep the apartment a more private space for just my roommate and me.":
            # call the corresponding cif action  
            call call_action("decScoreShubh") 
            jump after8           
        
        "I'm okay with having guests over occasionally, but I prefer to keep things low-key and not have big parties or events.":
            # call the corresponding cif action
            call call_action("IncScoreShubh")  
            jump after8        
            
    label after8:
        anya"Thanks for letting me know"

    anya "How often do you clean up after yourself?"
    menu:       
        "I like to keep things neat and tidy and clean up after myself as I go along throughout the day.":
            # call the corresponding cif action
            call call_action("IncScoreShubh")
            call call_action("IncScoreShubh")
            jump after9

        " I tend to be a bit messy, but I always make sure to clean up after myself before going to bed.":
            # call the corresponding cif action  
            call call_action("IncScoreShubh")
            jump after9           
        
        "I don't have a set cleaning schedule, but I always make sure to clean up after myself when things start to get messy.":
            # call the corresponding cif action  
            call call_action("decScoreShubh")
            call call_action("decScoreShubh")
            jump after9        
            
    label after9:
        anya "Got it!"


    anya "What are some of your hobbies?"
    menu:       
        "I enjoy going to the gym and staying active, so I often go for runs or work out in the apartment.":
            # call the corresponding cif action
            call call_action("IncScoreShubh") 
            jump after10

        "I'm a bit of a homebody and enjoy watching movies and TV shows in my free time.":
            # call the corresponding cif action
            call call_action("IncScoreShubh")  
            jump after10

        "I like to play music and write songs, but I always use headphones so as not to disturb my roommate.":
            # call the corresponding cif action 
            call call_action("IncScoreShubh") 
            call call_action("IncScoreShubh")
            jump after10                
      
            
    label after10:
        anya "Wow that sounds really interesting, you seem to be good company "

    anya "How do you feel about noise levels in the apartment?"
    menu:       
        "I don't mind some background noise, and I'm always up for having a good time with my roommate and their friends.":
            # call the corresponding cif action  
            call call_action("IncScoreShubh")
            jump after11

        "I prefer a quieter living environment and would appreciate it if my roommate kept noise levels down, especially late at night.":
            # call the corresponding cif action
            call call_action("decScoreShubh")
            jump after11

        "As long as the noise is reasonable and respectful of others' needs, I don't have a strong preference either way.":
            call call_action("IncScoreShubh")
            jump after11           
      
            
    label after11:
        anya "Hmmmm....."

    anya "How do you feel about sharing food or cooking together?"
    menu:       
        " I love cooking and would be happy to share meals or cook together with my roommate.":
            # call the corresponding cif action  
            call call_action("IncScoreShubh")
           
            jump after12

        "I prefer to cook for myself and wouldn't want to share food, but I'm okay with occasionally cooking at the same time.":
            # call the corresponding cif action
            
            jump after12

        " I don't cook very often and usually just order takeout, so I don't have a strong preference either way.":
            call call_action("decScoreShubh")
            jump after12           
      
            
    label after12:
        anya "Ahh I see.."

    hide hall2
    hide anya
    show ucdavis:
        xzoom 1  
        yzoom 1
    return 
     
# Rahul's questionnaire
label rahul_question():
    # Audio for characters background
    play music r'audio/Don2.mp3' loop
    $rahul = Character("Rahul", image='rahul.jpg')
    scene hall3:
        xzoom 1.5
        yzoom 1.5
    show rahul:
        xalign 0.0
        yalign 0.9

    rahul "Heyy..[player] thanks for coming  "
    rahul "Let me give you a quick house tour"
    $renpy.movie_cutscene("house3.webm")
    rahul "The leasing rate for the room will be USD 1000. Are you okay with the cost?"

    menu:       
        "Yes sure no problem sounds fine":
            # call the corresponding cif action 
            call call_action("IncScoreRahul") 
            call call_action("IncScoreRahul") 
            jump after13

        "Yea about that , can I get a slight reduction in that if possible.":
            # call the corresponding cif action 
            call call_action("IncScoreRahul")  
            jump after13 

        "Oh that seems really high and out of my budget can you please give an exemption like for the first few months.":
            # call the corresponding cif action 
            call call_action("decScoreRahul")  
            jump after13               

    label after13:
        "Okk.."
        


    rahul "Who is your favorite actor?"
    menu:       
        "Obviously not even a question it has to be Shahrukh Khan, the King, his wit his charm his range of expressions, his versatility is of top class":
            # call the corresponding cif action  
            call call_action("IncScoreRahul")
            call call_action("IncScoreRahul")  
            jump after14

        "I dont watch a lot of movies, I am boring that way.":
            call call_action("decScoreRahul") 
            # call the corresponding cif action  
            jump after14 
        
        "Dont have particular preference, I like good production over good actors.":
            # call the corresponding cif action  
            jump after14        
            
    label after14:
        rahul"That may sound a dumb question but thats something really important for me as I am a film student & a huge SRK fan"

    rahul "How often do you party and mind patries in your household?"
    menu:       
        "I love parties , I party every weekend sometimes for 2-3 days straight":
            # call the corresponding cif action  
            call call_action("IncScoreRahul") 
            call call_action("IncScoreRahul") 
            
            jump after15

        "I like them,never hosted one but always up for one.":
            # call the corresponding cif action
            call call_action("IncScoreRahul")   
            jump after15           
        
        "I usually dont party that much I like studying at night and prefer silence while doing so.":
            # call the corresponding cif action 
            call call_action("decScoreRahul")  
            jump after15        
            
    label after15:
        rahul "Interesting"


    rahul "How often do you cook ?"
    menu:       
        "I usually dont cook that much.":
            # call the corresponding cif action
            call call_action("decScoreRahul")   
            jump after16

        "I love cooking now and then":
            # call the corresponding cif action  

            jump after16

        "I only eat home cooked food and we can even cook together":
            # call the corresponding cif action  
            call call_action("IncScoreRahul") 
            jump after16                
      
            
    label after16:
        rahul "Is it so..."

    rahul "Is cleanliness important for you "
    menu:       
        "Yea i keep my room very clean and expect the house to be clean as well and will regularly clean the house":
            # call the corresponding cif action  
            call call_action("decScoreRahul") 
            jump after17

        "Yeah I am a person who is not very particular but will keep my things clean.":
            # call the corresponding cif action 
            call call_action("IncScoreRahul") 
            call call_action("IncScoreRahul")  
            jump after17

        "We can hire a maid":
            call call_action("decScoreRahul") 
            jump after17           
      
            
    label after17:
        rahul "Uhh huh.."

    rahul "Do you own a vehicle"
    menu:       
        "Yes I have a car that I will use to commute to college":
            # call the corresponding cif action
            call call_action("IncScoreRahul") 
            jump after18

        "I have a bike":
            # call the corresponding cif action  
            jump after18

        "I don’t currently, I haven’t figured out how i will commute to college yet":
            jump after18           
      
            
    label after18:
        rahul "Ohh wow"

    rahul "How long are you thinking of leasing the apartment?"
    menu:       
        "3 months":
            # call the corresponding cif action  
            call call_action("decScoreRahul") 
            jump after19

        "4 years":
            # call the corresponding cif action  
            call call_action("IncScoreRahul") 
            jump after19

        "1 year":
            # call the corresponding cif action 
            call call_action("IncScoreRahul") 
            call call_action("IncScoreRahul") 
            jump after19          
      
            
    label after19:
        rahul "Got it!"    

    hide hall3

    hide rahul
    stop music
    show ucdavis:
        xzoom 1  
        yzoom 1
    return         

# Function to call john's introduction
label john_intro():
    $john = Character("John", image='john.jpg')
    show john:
        xalign 0.0
        yalign 1.0
  
        



    #Intro of the character
    "{size=-5}John is a recent graduate and has just landed his first job in a new city.
    He is looking for a roommate to share expenses with and make the transition to a new city smoother. He was a little rude to you on the first day of college, when you were confused and asked him about which room to go{/size} "
    john "Hello [player] how are you doing today, I am really excited to meet you "

    # hide john
    return
# Function to call Rahul's introduction
label rahul_intro():
    $rahul = Character("Rahul", image='rahul.jpg')

    show rahul:
        xalign 0.5
        yalign 0.5
    


#Intro of the character
    "{size=-8}Meet Rahul Raichand, he is a senior at UC Davis studying filmmaking. A born performer he always had a penchant for art , movies specifically. Hence he decided to study Film making,.
    He is a passionate, caring human being and is also a bit of womanizer. He is currently dating Anjali from his class but the rumor is he is also interested Dean’s daughter Tina Malhotra. 
    He is currently looking for a roommate who can take the other spare room and be a part of his fun and adventurous life {/size}"


    rahul "Hello [player]  I am Rahul, you must have heard my name I am quite famous, Lets finish this up quickly I have to meet Anjali my girlfriend"

    # hide rahul
    return
# Function to call Anya's introduction
label anya_intro():
    $anya = Character("Anya", image='anya.jpg')

    show anya:
        xalign 1.0
        yalign 0.8



#Intro of the character
    "{size=-8}Anya is an international student at UC davis. She just moved from her home country(India) to UC Davis to pursue his graduate studies. 
    Its her first international travel and happens to be a long one. Finding the ideal roommate who can keep a productive environment around
    her is a concern for her. She was in the same school as you in India, you even had a little crush on her back in the day.{/size} "


    anya "Yo [player]  how is it hanging, Hope you are not a phsycopath like the the last guy I interviewed, lets get started shall we"

    # hide anya
    return
   

#main function to start the game
label start:


    #inctroduction 
    $renpy.movie_cutscene("intro.webm")
    show ucdavis:
        xzoom 1  
        yzoom 1


    #background music
    play music r'audio/audio-piku.mp3' loop

 
 
    "{b}Welcome to the Roomate Finder Game, lets find a roomate real fast, 
    the next quarter is upon us you dont want to be stuck at your aunt's place do you !!!{/b}"


    #taking player's name as input
    $player = renpy.input("Enter your name:")

    "Welcome [player] !! lets get started"

    "Its time to meet the characters"



#calling all the introduction of characters
    call john_intro()
    call anya_intro()
    call rahul_intro()
    $choice=0
    
    
 

    #inputting the choice from the user 
    $choice = renpy.input(" You can now choose which roomate you  1: John  2:Anya  3:Rahul")
    
    $npc = {'1':'John', '2': 'Anya', '3': 'Rahul'}

    hide john
    hide rahul
    hide anya

    # "Cool, you chose option [choice] "


    #calling the appropriate character questions
    label x:
        if choice=='1':
            call john_question()
            $npc.pop('1')
        elif choice=='2':
            call anya_question()
            $npc.pop('2')
        elif choice=='3':
            call rahul_question()
            $npc.pop('3')
        else:
            
            $choice = renpy.input("Hey come on now! these people are not that bad, they seem to be nice please enter a valid choice(1/2/3) Note - You cannot enter the same choice again")
            jump x

    #choosing second character
    $choice = renpy.input("That was nice onto the next one, You have the following roommate interviews left please select one of them(1/2/3) Note - You cannot enter the same choice again")


        #label y:
    label y:
        if choice=='1':
            $boo=choice in npc
            if boo==True:
                call john_question()
                $npc.pop('1')
            else:
                $choice = renpy.input("Hey come on now! these people are not that bad, they seem to be nice please enter a valid choice(1/2/3) Note - You cannot enter the same choice again")
                jump y
            
        elif choice=='2':
            $boo=choice in npc
            if boo==True:
                call anya_question()
                $npc.pop('2')
            else:
                $choice = renpy.input("Hey come on now! these people are not that bad, they seem to be nice please enter a valid choice(1/2/3) Note - You cannot enter the same choice again")
                jump y
            
        elif choice=='3':
            $boo=choice in npc
            if boo==True:
                call rahul_question()
                $npc.pop('3')
            else:
                $choice = renpy.input("Hey come on now! these people are not that bad, they seem to be nice please enter a valid choice(1/2/3) Note - You cannot enter the same choice again")
                jump y

            
        else:           
            $choice = renpy.input("Hey come on now! these people are not that bad, they seem to be nice please enter a valid choice(1/2/3) Note - You cannot enter the same choice again")
            jump y
            
    #choosing the third character

    $choice = renpy.input("Phew !! 2 interviews down one last to go, You are almost there champ keep going, Davis's good weather awaits ")

    label z:
        if choice=='1':
            $boo=choice in npc
            if boo==True:
                call john_question()
                $npc.pop('1')
            else:
                $choice = renpy.input("Hey come on now! these people are not that bad, they seem to be nice please enter a valid choice(1/2/3) Note - You cannot enter the same choice again")
                jump z
            
        elif choice=='2':
            $boo=choice in npc
            if boo==True:
                call anya_question()
                $npc.pop('2')
            else:
                $choice = renpy.input("Hey come on now! these people are not that bad, they seem to be nice please enter a valid choice(1/2/3) Note - You cannot enter the same choice again")
                jump z
            
        elif choice=='3':
            $boo=choice in npc
            if boo==True:
                call rahul_question()
                $npc.pop('3')
            else:
                $choice = renpy.input("Hey come on now! these people are not that bad, they seem to be nice please enter a valid choice(1/2/3) Note - You cannot enter the same choice again")
                jump z

            
        else:           
            $choice = renpy.input("Hey come on now! these people are not that bad, they seem to be nice please enter a valid choice(1/2/3) Note - You cannot enter the same choice again")
            jump z

    #Retrieving the scores from server that are updated by cif
    call get_attribute("ScoreJohn", "score", "Player", "John")
    $s1 = score
    call get_attribute("ScoreShubh", "score", "Player", "Shubh")
    $s2 = score
    call get_attribute("ScoreRahul", "score", "Player", "Rahul")
    $s3=score

    # "The final scores are John [s1]  Anya [s2]  Rahul [s3]"

    show ucdavis
    play music r'audio/drums.mp3' loop
    $fin = max(max(s1,s2),s3)


    # Checking which character won 
    "{b} Its time to reveal who will be crowned as the winner of Roomate Roulette and who is going to be your future flatmate {\b}"
    if fin==s1:
        $john = Character("John", image='john.jpg')
        "The winner is John with [s1] points" 
        show john:
            xalign 0.5
            yalign 0.5
    
    elif fin==s2:
        $anya = Character("anya", image='anya.jpg')
        "The winner is Anya with [s2] points"      
        show anya:
            xalign 0.5
            yalign 0.5

    else:
        $rahul = Character("Rahul", image='Rahul.jpg')
        "The winner is Rahul with [s3] points"       
        show rahul:
            xalign 0.5
            yalign 0.5
    
    "The final points were John:[s1]  Anya :[s2]  Rahul :[s3]"

    "Thank you for playing the game"

    return


    
# Function to retrieve final compatibility score from cif Server
label get_attribute(types="", cl="", first="", second=""):
    python:
        import requests
        import json
        rec = requests.post(BASE_URL + 'getAttribute', headers=headers, json={
            "class": cl,
            "type": types,
            "first": first,
            "second": second
        })
        res = json.loads(rec.text)
        score = res[0]["value"]




# Function to post a given action to cif
label call_action(action=""):
    python: 
        import requests
        requests.post(BASE_URL+'performAction',headers=headers, json={
            'action': action
        })

