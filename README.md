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
├── group
│   ├── project.py
│   └── utils.py
├── main.py
├── times.py  
└── private
    ├── proutils.py
    └── solutions.py
```

The input datasets are inside the data folder (e.g., data/small_dataset.txt). You should not change the main file, except for the variable group_id (as specified below).
Change the name of folder group0 to match the group id that we will assign you after the
registration on Luiss Learn, and also change the group_id value in main.py.

Implement your code in file groupid/project.py, that contains three functions (you can add more functions, if needed, but you must at least implement these ones). 

- Function prepare is called once to load the dataset. it can be used to prepare and read the input file (e.g., data/small_dataset.txt), and store the relevant information in suitable global data structures of your choice. 

- Function query implements the algorithm. It receives as input the stock name (e.g., AAPL) and a correlation level. It outputs the ordered list of correlated stocks. 

- Function num_connected_components, returns the number of connected components in the correlation graph: a connected component is a set of stocks that are linked (correlated) to each other.   

## Libraries
The code is tested with python3.9.1, libraries and packages used are:

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


