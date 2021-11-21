#Love_Calculator ! "TRUE LOVE"
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2

lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

Love_score = int(str(true) + str(love))

if (Love_score < 10) or (Love_score > 90):
    print(f"Your lovescore is {Love_score}, you go together like coke and mentos.")

elif (Love_score >= 40) and (Love_score <= 50):
    print(f"Your lovescore is {Love_score}, you are alright together.")

else:
    print(f"Your Lovescore is {Love_score}")


