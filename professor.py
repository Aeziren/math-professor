import random
import sys

def main():
    level = get_level()
    points = 0

    for i in range(10):

        n1 = generate_integer(level)
        n2 = generate_integer(level)

        result = n1 + n2
        trie = 1
        while True:
            if trie > 3:
                print(f"{n1} + {n2} = {result}")
                break

            answer = get_int(f"{n1} + {n2} = ")
            if answer == result:
                points += 1
                break
            else:
                print("EEE")
                trie += 1

    print(f"Points: {points}")


def get_level():
    while True:
        try:
            num = int(input("Level: "))
            if 1 <= num <= 3:
                return num
            else:
                raise ValueError
        except:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


def get_int(message):
    try:
        return int(input(message))
    except EOFError:
        sys.exit()
    except:
        pass

if __name__ == "__main__":
    main()
