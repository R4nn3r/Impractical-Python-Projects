import random 

def get_guess(list):
    return random.choice(list)


def main():
    num = 4
    r_y = int(input("Enter Highest bound: "))   

    list = []
    for i in range(r_y):
        list.append(i)

    guess = get_guess(list)
    print(guess)
    while True:
        if num == guess:
            break
        else:
            list.remove(guess)
            guess = get_guess(list)
            print(guess)

        
    print(f"Got it right: {guess} = {num} ")
    print(list)

if __name__ == '__main__':
    main()