import time

while True:
    print("Follow the prompts to find the maximum value from your list")
    user_choice = input("Enter yes to continue or no to exit.")
    if user_choice == "yes" or user_choice == "Yes":
        user_data = input("Type your list of numbers separated by empty spaces.")
        user_data_strings = user_data.split()

        with open("array-data.txt", "w") as array_data_f:
            array_data_f.write(user_data)
            print("Converting list to text file...")

        time.sleep(3)

        with open("maxVal.py", "r") as max_val_py:
            max_val_code = max_val_py.read()
            print("Calculating your maximum value...")

        time.sleep(3)

        with open("max-val.txt", "r") as max_val_f:
            max_val = max_val_f.read()
            print(max_val)

    elif user_choice == "no" or user_choice == "No":
        print("Exiting program...")
        break
    else:
        print("Your input is invalid, please try again.")
