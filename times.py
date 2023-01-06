import importlib
from time import perf_counter
from private import proutils, solutions
import sys, os
import random 

# put here your group id
your_group = 23

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

#-------------------------------------------# Proj v1 #-------------------------------------------#

def test_final(gid : int, filename : str, corr_threshold : float, stock : str, corr_level : int):
    g = importlib.import_module('group{}.project'.format(gid))
    start = perf_counter()
    g.prepare(filename, corr_threshold)
    end = perf_counter()
    prep_time = round(1000 * (end - start))

    # query
    start = perf_counter()
    res = g.query(stock, corr_level)
    end = perf_counter()
    run_time = round(1000 * (end - start))
    importlib.reload(g)
    return prep_time, run_time

def test_perf_project_full(gid=0):
    blockPrint()
    random.seed(10)
    prep_time, run_time = 0, 0
    thresholds = [x / 100 for x in range(1, len(solutions.STOCKS_TO_TEST))]
    for tr, stock in zip(thresholds, solutions.STOCKS_TO_TEST):
        corr_level = random.randint(1,10)
        tmp_prep_time, tmp_run_time = test_final(gid, "data/small_dataset.txt", tr, stock, corr_level)
        run_time += tmp_run_time
        prep_time += tmp_prep_time
        tmp_prep_time, tmp_run_time = test_final(gid, "data/medium_dataset.txt", tr, stock, corr_level)
        run_time += tmp_run_time
        prep_time += tmp_prep_time

    enablePrint()
    print('Loading and Building data - Time: {}ms'.format(prep_time))
    print('Query - Time: {}ms'.format(run_time))

if __name__ == "__main__":
    test_perf_project_full(gid=your_group)
