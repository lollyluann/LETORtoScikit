# LETORtoScikit
A Python based converter for LETOR formatted data to data compatible with scikit-learn

# How to Use
This script is importable using the following Python code:
    ```import sys
       import os
       sys.path.append("C:/Users/lolly/Documents/GitHub/LETORtoScikit") #directory should be to this repository
       import LtoSKL
       
       os.chdir("C:/Users/lolly/PycharmProjects/testingarea") #directory should be to wherever your input files are
       LtoSKL.convert('input.txt', 'listOfClasses.txt') ```
      
The convert() function is the only function that should be called.
    The first parameter is the name of your LETOR formatted input file.
    The second parameter is the name of your file with all the class names comma-delimited in one line.
        e.g. `setosa,virginica,versicolor`
        
The script will write to two .csv files.
    The first file will be "whateveryourinputwasnamed-attr.csv" and will contain a list of all the non-class attributes of the data.
            This information is saved because conversion from LETOR to skikit-learn is a lossy process that loses attribute names.
    The second file will be "whateveryourinputwasnamed-converted.csv" and will contain the data in scikit-learn compatible format.
