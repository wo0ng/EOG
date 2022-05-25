# 홀짝게임
import random 
import os

life = 5
score = 0

while True:
    print("="*30)
    print("♥ "*life + "♡ "*(5-life))
    print("="*30)
    
    com = random.randint(1,9)
    user = input("홀(1)? 짝(0)?")

    if str(com % 2) == user:
        print("맞췄습니다.")
        score += 100
    else:
        print("틀렸습니다.")
        life -= 1

        if life == 0:
            print(f"니점수 {score}")
            break
    input("\n\nENTER")
    os.system("cls")
