# PyChat 2K17

import random

def start():
    pass

def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup", "yep"]:
            return True
        elif answer in ["n", "no", "nope", "nah"]:
            return False
   
def has_keyword(statement, keywords):

    statement = " " + statement
    
    for word in keywords:
        word = " " + word
        if word in statement:
            return True

    return False

def get_random_response():
    responses = ["Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?", "That's crazy, dude.", "So how has your day been?" ]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()
    
    family_words = [" mother", " father", " brother", " sister"]
    teacher_words = ["cooper"]
    animal_words = [ " pet " "pets", "dogs", "cats", "birds", "dog ", "cat ", "fish ", "elephant"]
    event_words = [ "today ", "yesterday ", " last year ", "last week", "sometimes", "one time", "time"]
    you_words = ["you are ", "you is ", "u are ", "u r"]
    greeting_words = ["hey", "hi", "hello", "sup"]
    agreement_words = ["yep", "yes", "definetly", "absolutely", "duh"]
    school_words = ["school", "class", "teacher", "grades"]
    
    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword (statement, animal_words):
        response = "Wow those things can be crazy"
    elif has_keyword (statement, event_words):
        response = "Good Job! That's Awesome!"
    elif has_keyword (statement, you_words):
        response = "Well you need to chil out."
    elif has_keyword (statement, greeting_words):
        response = "Hi. What is your favorite animal?"
    elif has_keyword (statement, agreement_words):
        response = "Yay! We agree!"
    elif has_keyword (statement, school_words):
        response = "School is sooo stressful."
    
    else:
        response = get_random_response()

    return response

def play():
    talking = True
    name = "Chatterbot345"

    print("Hello! I'm Chatterbot345!")
    human_name = input("What is your name?")

    while talking:
        statement = input(">>" + human_name + ": ")

        if statement == "Goodbye":
            talking = False
        else:
            response = get_response(statement)
            print(name + ": " + response)

    print("Goodbye. It was nice talking to you, " + human_name +".")


start()

print()
print("  / ____| |         | | | |          | |         | | |___ \| || | | ____| |")
print(" | |    | |__   __ _| |_| |_ ___ _ __| |__   ___ | |_  __) | || |_| |__ | |")
print(" | |    | '_ \ / _` | __| __/ _ \ '__| '_ \ / _ \| __||__ <|__   _|___ \| |")
print(" | |____| | | | (_| | |_| ||  __/ |  | |_) | (_) | |_ ___) |  | |  ___) |_|")
print("  \_____|_| |_|\__,_|\__|\__\___|_|  |_.__/ \___/ \__|____/   |_| |____/(_)")


playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
