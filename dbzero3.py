### dbzero3.py
answer = input("Do you want to divide by zero? (y/n) ")
if answer[0] == "y":
    x = 42
    q = x / 0
    print(q)
else:
    print("Good call!  I didn't want to do that either.")
