import time
import sys

while True:

    time.sleep(1)

    def max_val_calc(array_data):
        """
        This function finds the maximum value of an array. It checks for any values that are not floats or
        integers and will raise an error if this condition is not met. Otherwise, it will return the
        corresponding maximum value.
        """
        # smallest integer size to ensure proper max value is found from the data set
        max_val = -sys.maxsize
        index = -1

        for elem in array_data:
            index += 1
            data_type = isinstance(elem, (float, int))
            # conditional check to see if the data at the current index is valid.
            if data_type is True:
                if elem > max_val:
                    max_val = elem
            else:
                print("The element at index", index, "is of the wrong type. Please check your dataset and try again.")
                raise TypeError("Only integers and floats are allowed")
        return max_val


    with open("array-data.txt", "r") as array_data_f:
        data = array_data_f.read()
        data_strings = data.split(" ")
        try:
            # convert all elements from the user input to float values
            data_array = [float(elem) for elem in data_strings]
            max_val = max_val_calc(data_array)

            with open("max-val.txt", "w") as max_val_f:
                max_val_f.write(str(max_val))

        except ValueError:
            with open("max-val.txt", "w") as max_val_f:
                max_val_f.write("Something went wrong when converting your data to a list. Please make sure you only have floats and integers in your data set.")
