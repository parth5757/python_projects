from time import *
import random as ra
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error +1
        except :
            error = error + 1
    return error
def speeed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R  = round(time_delay, 2)
    speed = len(userinput)/time_R
    return round(speed)
if __name__ == '__main__':
    while True:
        ck = input("ready to test: yes/no: ")
        if ck == "yes":
            jokes = [
                "I'm reading a book about anti-gravity. It's impossible to put down.",
                "I wondered why the baseball was getting bigger. Then it hit me.",
                "The police station called me to say that my dog was chasing someone on a bike. My dog doesn't even own a bike.",
                "I waited my whole life to turn 18... and then it was very anti-climactic.",
                "What do you call a fake noodle? An Impasta.",
                "I wondered why the baseball was getting bigger. Then it hit me.",
                "What do you call a bear with no teeth? A gummy bear.",
                "What do you call a boomerang that doesn't come back? A stick.",
                "What do you call a fake Italian currency? Faux Dough.",
                "What do you call a fish wearing a bowtie? Sofishticated.",
                "What do you call a fish wearing a bowtie? Sofishticated.",
                "What do you call a group of killer whales playing instruments? A Whale Orchestra.",
                "What do you call a pig that does karate? A pork chop.",
                "What do you call a sheep with no legs? A cloud.",
                "What do you call a stolen calendar? A missing date.",
                "What do you call a tired bull? Bulldozer.",
                "What do you call a train carrying bubblegum? A chew-chew train.",
                "What do you call a very small valentine? A valentiny.",
                "What do you call an alligator in a vest? An investigator.",
                "What do you call an angry European? A furious European.",
                "What do you call an Italian chef who has passed away? Pasta way.",
                "What do you call cheese that's not yours? Nacho cheese.",
                "What do you call someone who loves math? A calculator.",
                "What do you call two avocados on a first date? Guacamole.",
                "What do you call two guys who love math? A calculator.",
                "What do you get when you cross a snowman with a vampire? Frostbite.",
                "What do you say to encourage a sick mushroom? You mushroom get well soon!",
                "What do you say to encourage a sick mushroom? You mushroom get well soon.",
                "What do you sayto a mushroom when it's sick? You mushroom get well soon!",
                "What do you throw a drowning writer? A buoyancy aid.",
                "What do you throw a drowning writer? A buoyancy aid.",
                "What do you want to be when you bubble up? A pop star.",
                "What do you want to be when you bubble up? A popstar.",
                "What do you when life gives you melons? You're dyslexic.",
                "What do you when life gives you melons? You're dyslexic.",
                "What do you when life gives you melons? You're dyslexic.",
                "What do you when life gives you melons? You're dyslexic.",
                "What do you when life gives you melons? You're dyslexic.",
                "What do you when life gives you melons? You're dyslexic.",
                "What do you when life gives you melons? You're dyslexic.",
                "What do you when life gives you melons? You're dyslexic.",
                "What do you when life gives you melons? You're dyslexic.",
                "What do you when life gives you melons? You're dyslexic.",
                "What do you when life gives you melons? You're dyslexic.",
            ]
            t1 = ra.choice(jokes)
            print("*****typing speed*****")
            print(t1)
            print()
            print()
            time_1 = time()
            tinput = input("Enter : ")
            time_2 = time()
            p1 = speeed_time(time_1,time_2,tinput)
            print('Speed: ', p1, "word/second")
            p2 = mistake(t1,tinput)
            print("Error :" , p2)
            
        else:
            
            print("byy")
