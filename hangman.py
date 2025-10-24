import random
stages = ['''
   ------
   |    |
   O    |
  /|\   |
  / \   |
        |
        |
   ======
''','''
   ------
   |    |
   O    |
  /|\   |
  /     |
        |
        |
   ======
''','''
   ------
   |    |
   O    |
  /|\   |
        |
        |
        |
   ======
''','''
   ------
   |    |
   O    |
  /|    |
        |
        |
        |
   ======
''','''
   ------
   |    |
   O    |
   |    |
        |
        |
        |
   ======
''','''
   ------
   |    |
   O    |
        |
        |
        |
        |
   ======
''','''
   ------
   |    |
        |
        |
        |
        |
        |
   ======
''']
fruits = ["apple","mango","grape","guava","berry","banana","orange"]
countries = ["india","france","russia","america","africa","germany","canada","srilanka"]
occupations = ["doctor","teacher","lawyer","actor","painter","singer","driver"]
print("Welcome to Hangman game !!!")
print("If you guess the word before hangman forms you win or else  you lose")
while True:
    choice = input("Enter your choice of words to be asked fruits or countries or occupations: ")
    if choice.lower() == "fruits":
        selected = fruits
        break
    elif choice.lower() == "countries":
        selected = countries
        break
    elif choice.lower() == "occupations":
        selected = occupations
        break
    else:
        print("Select only from given choices!!!")
chosen = random.choice(selected)
lives = 6
display = []
for i in range(len(chosen)):
    display.append("_")
gameover = False
while not gameover:
    print(display)
    match lives:
        case 1:
            print(stages[1])
        case 2:
            print(stages[2])
        case 3:
            print(stages[3])
        case 4:
            print(stages[4])
        case 5:
            print(stages[5])
        case 6:
            print(stages[6])
    guess = input("Guess the letter: ").lower()
    if guess in display:
        print("Already entered !! Lost one life")
        lives -= 1
        if lives == 0:
            gameover = True
            print(stages[0])
            print("You Lose !!!")
    else:
        for  i in range(len(chosen)):
            letter = chosen[i]
            if guess == letter:
                display[i] = guess
    if guess not in chosen:
        print("Wrong guess !! Lost one life")
        lives -= 1
        if lives == 0:
            gameover = True
            print(stages[0])
            print("You Lose !!!")
    if "_" not in display:
        gameover = True
        print(f"You Win !!! The word is {chosen}")