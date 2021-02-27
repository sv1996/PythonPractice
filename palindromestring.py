S1 = "madaM"

S1 = S1.lower()

revStr=reversed(S1)

if list(S1) == list(revStr):
    print("Given String is Palindrome")
else:
    print("Given String is not Palindrome")