# Week 06 Prove: Assignment - Adventure Game
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse110-course/lesson05/prove.html

line = "\n**********************************************\n"

# STRETCH - Dictionary with scenarios
## It's possible change the whole history changing the dictionary of scenarios without changing any other line of code

# CORE REQUIREMENTS - You need to have at least three levels of scenarios with possible choices.
## The min level that user can reach is three

# CORE REQUIREMENTS - At least one of your scenarios must have more than two possible choices.
## At scenario 2.1 there is three posssible choice.
scenarios = {
    "1" : {
        "prompt" : "\nIt's 10 PM, you are watching a TV show on your cell phone, and it's starting the season's final episode. \nThe battery is about to die, and you are feeling a little tired, so you can go to SLEEP or WATCH the final episode. \nWhat do you want to do? ",
        "answers" : ["SLEEP", "WATCH"],
        "nextScenario" : {
            "SLEEP" : "2.1",
            "WATCH" : "2.2"
        }
    },
    "2.1" : {
        "prompt" : "\nYou put the cell phone to charge, set up the alarm clock, and go to bed. \nIt\'s 6:30 AM, the alarm clock is ringing, you can RISE from bed, SNOOZE the alarm clock for a few minutes, or just TURN OFF the alarm. \nWhat do you want to do? ",
        "answers" : ["RISE", "SNOOZE", "TURN OFF"],
        "nextScenario" : {
            "RISE" : "3.1",
            "SNOOZE" : "3.2",
            "TURN OFF" : "3.3"
        }
    },
    "2.2" : {
        "prompt" : "\nYou fell asleep before the episode ended. It's 9 AM, you wake up scared, your cell phone has no battery, and you think \"I'm late to work\". \nYou can try to CHARGE a little of the battery or RUN to the work and charge it there. \nWhat do you do now? ",
        "answers" : ["CHARGE", "RUN"],
        "nextScenario" : {
            "CHARGE" : "3.4",
            "RUN" : "3.5"
        }
    },
    "3.1" : {
        "prompt" : "\nYou rise up from bed, take a breakfast while you watch the final episode of the TV show. \nYou meet your friends at the soccer field, everybody is talking about the episode, and you enjoy the match. \nNow you can go home to WASH your clothes or take an ICE CREAM with your friends. \nWhat do you do? ",
        "answers" : ["WASH", "ICE CREAM"],
        "nextScenario" : {
            "WASH" : "4.5",
            "ICE CREAM" : "4.6"
        }
    },
    "3.2" : {
        "prompt" : "\nYou wake up and realize that is a little late, so you just take a bread and run to the soccer field. \nEverybody is having fun and talking about the episode. \nAccidentally, you hear how the episode ended. You think to yourself, \"It could be better if I had not snoozed the alarm\".",
        "answers" : []
    },
    "3.3" : {
        "prompt" : "\nYou wake up with the cell phone ringing, your friends are at the soccer field and the match is starting. \nYou run as fast as you can, but when you get there, the match ends. \nYour stomach is growling, you can go BACK home or talk with your FRIENDS. \nWhat do you do? ",
        "answers" : ["BACK", "FRIENDS"],
        "nextScenario" : {
            "BACK" : "4.3",
            "FRIENDS" : "4.4"
        }
    },
    "3.4" : {
        "prompt" : "\nThe cell phone turns on after plugged in to the charge. You have a lot of messages, you take a look and remember that it's Saturday. \nYou miss the soccer match, you think to yourself, \"At least I can watch the final episode now\".",
        "answers" : []
    },
    "3.5" : {
        "prompt" : "\nYou ran to your job and nobody was there. You are confused, you put the phone to charge while the computer is turning on. \nAbruptly you remember, \"Oh no, today is Saturday. What a mess I made\". \nYour friends are at the soccer field, you can try to CALL them or just go HOME. \nWhat do you want to do? ",
        "answers" : ["CALL", "HOME"],
        "nextScenario" : {
            "CALL" : "4.1",
            "HOME" : "4.2"
        }
    },
    "4.1" : {
        "prompt" : "\nYou unsuccessfully tried to call your friends, they already are playing. \nYou see the security guard, you can TALK with him or sneak out to AVOID embarrassment. \nWhat do you do? ",
        "answers" : ["TALK", "AVOID"],
        "nextScenario" : {
            "TALK" : "5.1",
            "AVOID" : "5.2"
        }
    },
    "4.2" : {
        "prompt" : "\nYou walk sadly to your home, when you get there you change your clothes and after thinking a while about the mess you made, you decide to watch the final episode and enjoy it.",
        "answers" : []
    },
    "4.3" : {
        "prompt" : "\nYou walk back home to have breakfast, after which you decide to watch the final episode and it was so fun.",
        "answers" : []
    },
    "4.4" : {
        "prompt" : "\nYou are so hungry, but you meet your friends. \nYou are talking and a friend gives a spoiler about the final episode, you murmur: \"Oh man, it\'s a terrible Saturday\".",
        "answers" : []
    },
    "4.5" : {
        "prompt" : "\nAfter playing soccer with your friends, you go home and wash the clothes and now have some time to rest before your next appointment. \nFurthermore, you think to yourself, \"This Saturday will be perfect\".",
        "answers" : []
    },
    "4.6" : {
        "prompt" : "\nYou have ice cream and spend some time with your friends having a lot of fun. \nWhen you come home it starts raining and now you can't wash your clothes. \nYou think to yourself \"Oh no, it will slow me down. Well, at least the ice cream was really good.\".",
        "answers" : []
    },
    "5.1" : {
        "prompt" : "\nYou talk with the security guard and have some fun talking about your mistake. \nFinally, you go home and laugh at yourself while you enjoy the final episode.",
        "answers" : []
    },
    "5.2" : {
        "prompt" : "\nYou sneak out and nobody notices you have made a mistake. \nYou decide to stop at a grocery store and buy some popcorn, while you are in the line you hear some spoiler about how the final episode ends.",
        "answers" : []
    }
}

print(f"{line}*       Welcome to the Adventure Game        *{line}")

scenario = "1" # Start Game
end_game = False

# STRETCH - The entire game run in a LOOP using a dynamic list of questions and answers
while not end_game:
    
    # If has possible answers, it's not the end game, so do a question.
    if scenarios.get(scenario).get("answers"):
        # CORE REQUIREMENTS - When checking the users responses, you should match on the keyword, 
        # regardless of the uppercase/lowercase used in the response
        choice = input(scenarios.get(scenario).get("prompt")).upper()

        # CORE REQUIREMENTS - Choices should only work for the correct question. 
        if scenarios.get(scenario).get("answers").count(choice) > 0:
            # CORE REQUIREMENTS - Choices should only work for the correct question. 
            scenario = scenarios.get(scenario).get("nextScenario").get(choice)
        else:
            # CORE REQUIREMENTS - For each question, you should provide an "else" clause to handle the case that
            # the user tries to type something other than the possible choices.
            print(f"\nLet's try again, type one of follows: {scenarios.get(scenario).get('answers')}\n")
    else:
        end_game = True
        print(scenarios.get(scenario).get("prompt"))

print(f"{line}*   Thanks for play the the Adventure Game   *{line}")