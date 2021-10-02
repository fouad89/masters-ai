# --------------------------------------------------------
#
# PYTHON PROGRAM DEFINITION
#
# The knowledge a computer has of Python can be specified in 3 levels:
# (1) Prelude knowledge --> The computer has it by default.
# (2) Borrowed knowledge --> The computer gets this knowledge from 3rd party libraries defined by others
#                            (but imported by us in this program).
# (3) Generated knowledge --> The computer gets this knowledge from the new functions defined by us in this program.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer first processes this PYTHON PROGRAM DEFINITION section of the file.
# On it, our computer enhances its Python knowledge from levels (2) and (3) with the imports and new functions
# defined in the program. However, it still does not execute anything.
#
# --------------------------------------------------------

import sys
import codecs

# ------------------------------------------
# 1. FUNCTION parse_in
# ------------------------------------------
def parse_in(input_file_name):
    m = []
    with open(input_file_name,'r') as f:
        r, c = f.readline().split()
        for line in f:
            m.append(line.split()) 



    return r, c , m


# ------------------------------------------
# 2. FUNCTION parse_out
# ------------------------------------------
# producing output file
def parse_out(output_file_name, num_rows, num_columns, sol_matrix):
    with open(output_file_name, 'w+') as f_out:
        f_out.writelines(f'{num_rows} {num_columns}')
        for row in sol_matrix:
            f_out.writeline(f'{row}')

# ------------------------------------------
# 3. FUNCTION solve
# ------------------------------------------

# conversions: looking at the neighbors (squares around). how many x's around the target square and change o into a number representing the number of x's

# conditions1 = (matrix[i][j] == 'o') and (i==0) and (j!=0) and (j!=num_columns) # i+1, j-1, j+1
# conditions2 = (matrix[i][j] == 'o') and (i==num_rows) and (j!=0) and (j!=num_columns) # i-1, j-1, j+1

# conditions3 = (matrix[i][j] == 'o') and (j==0) and (i!=0) and (i!=num_rows) # j+1, i-1, i+1
# conditions4 = (matrix[i][j] == 'o') and (j==num_columns) and (i!=0) and (i!=num_rows) # i-1, j-1, j+1

# corner1 = (matrix[i][j] == 'o') and (i==0) and (j==0) # i+1, j+1
# corner2 = (matrix[i][j] == 'o') and (i==0) and (j==num_columns) # i+1, j-1
# corner3 = (matrix[i][j] == 'o') and (i==num_rows) and (j==0) # i-1, j+1
# corner4 = (matrix[i][j] == 'o') and (i==num_rows) and (j==num_cols) # i-1, j-1

def solve(num_rows, num_columns, matrix):
    m_out = []
    conditions1 = (matrix[i][j] == 'o') and (i==0) and (j!=0) and (j!=num_columns) # i+1, j-1, j+1
    conditions2 = (matrix[i][j] == 'o') and (i==num_rows) and (j!=0) and (j!=num_columns) # i-1, j-1, j+1

    conditions3 = (matrix[i][j] == 'o') and (j==0) and (i!=0) and (i!=num_rows) # j+1, i-1, i+1
    conditions4 = (matrix[i][j] == 'o') and (j==num_columns) and (i!=0) and (i!=num_rows) # i-1, j-1, j+1

    corner1 = (matrix[i][j] == 'o') and (i==0) and (j==0) # i+1, j+1
    corner2 = (matrix[i][j] == 'o') and (i==0) and (j==num_columns) # i+1, j-1
    corner3 = (matrix[i][j] == 'o') and (i==num_rows) and (j==0) # i-1, j+1
    corner4 = (matrix[i][j] == 'o') and (i==num_rows) and (j==num_cols) # i-1, j-1
    for i in range(num_rows+1):
        for j in range(num_columns+1):
            if matrix[i][j] == 'x':
                m_out[i][j] = 'x'
            elif condition1:
                counter=0
                for in
                if matrix[i+1][j+1] == ''
                
                

# ------------------------------------------
# FUNCTION my_main
# ------------------------------------------
def my_main(input_file_name, output_file_name):
    # 1. We do the parseIn from the input file
    (num_rows, num_columns, matrix) = parse_in(input_file_name)

    # 2. We do the strategy to solve the problem
    sol_matrix = solve(num_rows, num_columns, matrix)

    # 3. We do the parse out to the output file
    parse_out(output_file_name, num_rows, num_columns, sol_matrix)

# --------------------------------------------------------
#
# PYTHON PROGRAM EXECUTION
#
# Once our computer has finished processing the PYTHON PROGRAM DEFINITION section its knowledge is set.
# Now its time to apply this knowledge.
#
# When launching in a terminal the command:
# user:~$ python3 this_file.py
# our computer finally processes this PYTHON PROGRAM EXECUTION section, which:
# (i) Specifies the function F to be executed.
# (ii) Define any input parameter such this function F has to be called with.
#
# --------------------------------------------------------
if __name__ == '__main__':
    # 1. We use as many input arguments as needed
    input_file_name = "Big Data Processing/Lab01/input_files/input_1.txt"
    output_file_name = "Big Data Processing/Lab01/results/output5.txt"

    if (len(sys.argv) > 1):
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]

    # 2. We solve the problem
    my_main(input_file_name, output_file_name)

    ## debugging
    c, r, m = parse_in(input_file_name)
    print(f"Number of columns{c}, Number of rows{r}")
    print(m)