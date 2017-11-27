# LETORtoScikit
A Python based converter for LETOR formatted data to data compatible with scikit-learn</br>
Luann Jung 2017

# How to Use
This script can be run in a command line (if your Python interpreter is already in your %PATH) with</br> 
`python.exe LtoS.py inputdata.txt inputclasses.txt`
      
* The first parameter is the name of your LETOR formatted input file.</br>
* The second parameter is the name of your file with all the class names comma-delimited in one line.</br>
      * e.g. `setosa,virginica,versicolor`</br>
        
* The script will write to two .csv files.</br>
    * The first file will be "*whateveryourinputwasnamed-attr.csv*" and will contain a list of all the non-class attributes of the data.</br>
        * This information is saved because conversion from LETOR to skikit-learn is a lossy process that loses attribute names.</br>
    * The second file will be "*whateveryourinputwasnamed-converted.csv*" and will contain the data in scikit-learn compatible format.
