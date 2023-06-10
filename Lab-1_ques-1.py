#Write a program that asks the user to enter their name and their age. 
#Print out a message that greets them and that tells them the year that they will turn 100 years old.

user_name = input("enter Your name")
current_age = int(input("enter Your age"))
tobe_hundred_years= int(100 - current_age)
hundredyears_in = str(2023 + tobe_hundred_years)
print("Hai "+user_name+", you will be hundred years old in thr year "+hundredyears_in)