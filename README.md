# Algorithms A.Y. 2021/22 
## Software project : A Stock Market Analyzer 

Final Release - Market Stock Correlation


## Project structure 
The project has the following structure:
```bash
.
├── README.md
├── data
│   └── small_dataset.txt
├── group0
│   ├── project.py
│   └── utils.py
├── main.py
├── times.py  
└── private
    ├── proutils.py
    └── solutions.py
```

We are providing you a skeleton of the code. You can modify the code we provide, adding the
missing parts (mostly inside group0/project.py). 

In the project folder, you will find two python scripts to execute your project:
- a file main.py, which is used to run some simple tests for your project and check if your solution is correct 
- a file times.py, which is used to evalute the efficiency of your approach

The input datasets are inside the data folder (e.g., data/small_dataset.txt). You should not change the main file, except for the variable group_id (as specified below).
Change the name of folder group0 to match the group id that we will assign you after the
registration on Luiss Learn, and also change the group_id value in main.py.

Implement your code in file groupid/project.py, that contains three functions (you can add more functions, if needed, but you must at least implement these ones). 

- Function prepare will be called once to load the dataset: it can be used to prepare and read the input file (e.g., data/small_dataset.txt), and store the relevant information in suitable global data structures of your choice. 

- Function query should implement your query algorithm, as
described in the project pdf. It receives as input the stock name (e.g., AAPL) and a correlation level. It outputs the ordered list of correlated stocks. Thus, the order of the output is important! The list should be in an alphabetical order! 

- Function num_connected_components is optional (not mandatory to implement), and it should returns the number of connected components in the correlation graph: a connected component is a set of stocks that are linked (correlated) to each other.   

You can use additional files, if needed, but all of them have to be in the group folder. There is a file utils.py where, if you want, you can implement auxiliary algorithms and data structures.

You can use Python lists, dictionaries, and string functions, but no specific algorithm from any Python library! You can't directly use external libraries, if you need an external tool you have to ask by email. If you need any algorithm (e.g., for searching, sorting, or selection) you have to implement your own version from scratch. If in doubt, just ask.

When you run the main.py script you receive a textual feedback about your solution (e.g., wrong or correct, and expected results).
Moreover, at the end of the execution you receive a feedback on how many tests you completed:
E.g.,:
Final result: 18 / 18 correct solutions!

## Libraries
The code is tested with python3.9.1, you may need to execute the following commands to install libraries and packages:

```bash
pip install pandas
pip install seaborn
pip intsall numpy
pip install matplotlib
```

## Execution

```bash
python3 main.py
python3 times.py
```

## Contacts
For further information contact Andrea Coletta at **acoletta[AT]luiss.it**; 
Irene Finocchi   **finocchi[AT]luiss.it**.

