import random as r 

START = 1
END = 10

def get_num():
    return r.randint(START, END)

def start():
    if input("[Enter] to start the game [q] to quit.: ").lower() == "q":
        return False
    else:
        random_num = get_num()
        print(random_num)
        return True, random_num
        


def main():
    on, random_num = start()
    count = 0

    while on:
        num = int(input(f"Guess the Number that between: {START} - {END} : "))

        if num > random_num:
            count += 1
            print("It's Lower: ")
            continue
        elif num < random_num:
            count += 1
            print("It's Higher: ")
            continue
        else:
            count += 1
            print(f"You got it right in your {count} attempt number is {random_num} ")
            on, random_num = start()    
            if on:
                count = 0
                continue
            else:
                break

        

if __name__ == '__main__':
    main()
