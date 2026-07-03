score = 0
answer=input('What is the largest hot desert in the world? ').strip().lower()
if answer=='sahara' or answer=='sahara desert':
    print("correct")
    score+=1
else:
    print("Wrong answer")
answer=input("Which animal is called as 'Ship of Desert'? ").strip().lower()
if answer=='camel':
    print("correct")
    score+=1
else:
    print("Wrong answer")
answer=input("Which planet in our solar system is known as 'Red planet'? ").strip().lower()
if answer=='mars':
    print("correct")
    score+=1
else:
    print("Wrong answer")
answer=input("What is the name of largest ocean in the world? ").strip().lower()
if answer=='pacific' or answer=='pacific ocean':
    print("correct")
    score+=1
else:
    print("Wrong answer")

print(f"Your score is {score}")