import  random

def play_game():
    lucky_num = random.randint(1,50)

    while True:
        user_num=int(input("guess the lucky number :"))
        if user_num==lucky_num:
         print("you won. game over!!")
         break
        elif user_num < lucky_num:
           print("too low.")
        else:
            print("too high.")
    print("thank you for playing the game.")

play_game()