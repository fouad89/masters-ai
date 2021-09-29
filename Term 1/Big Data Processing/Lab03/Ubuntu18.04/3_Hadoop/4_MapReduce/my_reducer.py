#!/usr/local/bin/python3.8
#
# --------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
# --------------------------------------------------------

import sys

# ------------------------------------------
# FUNCTION my_reduce
# ------------------------------------------
def my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters):
    # 1. We create a dictionary with all the different words in the file
    my_dict = {}

    # 2. We traverse the file content, to populate my_dict
    for line in my_input_stream:
        # 2.1. We get the info from the line
        line = line.replace("\n", "")
        info = line.split("\t")

        my_word = info[0]
        num_appearances = int(info[1][1:-1])

        # 2.2. We populate the dictionary with the words of the sentence
        if (my_word in my_dict):
            my_dict[my_word] = my_dict[my_word] + num_appearances
        else:
            my_dict[my_word] = num_appearances

    # 3. We write the content of the dict
    for key in my_dict:
        my_str = key + "\t(" + str(my_dict[key]) + ")\n"
        my_output_stream.write(my_str)

# ---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
# ---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We use as many input arguments as needed
    my_reducer_input_parameters = []

    # 2. We set the input and output streams
    my_input_stream = sys.stdin
    my_output_stream = sys.stdout

    # 3. We launch the Map program
    my_reduce(my_input_stream, my_output_stream, my_reducer_input_parameters)
