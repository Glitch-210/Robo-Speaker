import pyttsx3
if __name__ == '__main__':
    engine = pyttsx3.init()
    engine.say("Welcome!")
    engine.runAndWait()
    while True:
        x = input("Enter what do you want me to pronounce?")
        engine.say(x)
        engine.runAndWait()
        exi = input("Do you want to exit?\nPress 'q' to quit")
        if exi == 'q':
            engine.say("Bye bye!")
            break