# string concatination (aka how to put strings together)
# suppose we want to creat a string that says "subscribe to _______"
youtuber = "Ethio News" # some string variable

# a few ways to do this
# print("suscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It make me so exited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
