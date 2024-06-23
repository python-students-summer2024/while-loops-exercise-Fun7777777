def get_starting_number():
    while True:
        try:
            n = int(input("How many bottles of beer on the wall? "))
            if n >= 1:
                return n
            else:
                print("Please enter a number 1 or greater.")
        except ValueError:
            print("Please enter a valid integer.")

def sing(starting_bottles):
    for i in range(starting_bottles, 0, -1):
        if i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall!\n")
        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            if i - 1 == 1:
                print("Take one down and pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.\n")
