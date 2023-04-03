import random

print("Totally Random One-Million-To-One")
print("Guess a number between 1 to 1 million")

i = 0
answer = random.randint(1, 1000000)

while True:
  i += 1
  guess = int(input("What is your guess?: "))
  if guess == answer:
    print("Correct!")
    print("It took you", i, "guess to get it correct!")
    break
  elif guess < answer and guess > 0:
    print("Too low")
    continue
  elif guess > answer:
    print("Too high")
    continue
  elif guess < 0:
    print("REALLY??")
    exit()
  else:
    print("Err.. I think you put the wrong input")
    continue