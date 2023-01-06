import importlib
from time import perf_counter
from private import proutils

# In this file change only the group_id

### CHANGE HERE ###
group_id = 23
OPTIONAL_TEST = True


test_counter = 0
completed_counter = 0

def test_final(gid : int, filename : str, corr_threshold : float, stock : str, corr_level : int):
    global test_counter, completed_counter
    g = importlib.import_module('group{}.project'.format(gid))
    start = perf_counter()
    g.prepare(filename, corr_threshold)
    end = perf_counter()
    print('Prepare: {}ms'.format(round(1000 * (end - start))))

    # query
    start = perf_counter()
    res = g.query(stock, corr_level)
    end = perf_counter()
    print('Query: {}ms'.format(round(1000 * (end - start))))
    error, msg = proutils.check_stats_solution(gid, filename, corr_threshold, corr_level, stock, res)
    print(msg)
    test_counter += 1
    if not error:
        completed_counter += 1
    
    if OPTIONAL_TEST:
        start = perf_counter()
        res = g.num_connected_components()
        end = perf_counter()
        print('Optional query: {}ms'.format(round(1000 * (end - start))))
        error, msg = proutils.check_stats_solution_optional(gid,  filename, corr_threshold, corr_level, stock, res)
        print(msg)
        test_counter += 1
        if not error:
            completed_counter += 1
        
    importlib.reload(g)
    
### automatic tests ###
SMALL_TEST = [
    (0.04, "GOOGL", 1),
    (0.04, "GOOGL", 4),
    (0.04, "AAPL", 1),
    (0.04, "AAPL", 2),
    (0.04, "AAPL", 4),
    (0.08, "AAPL", 2)
]
print("Starting small dataset test...")
for test in SMALL_TEST:
    test_final(group_id, "data/small_dataset.txt", *test)


MEDIUM_TEST = [ 
    (0.06, "AAPL", 2),
    (0.1, "TSLA", 5)
]
print("Starting medium dataset test...")
for test in MEDIUM_TEST:
    test_final(group_id, "data/medium_dataset.txt", *test)

LARGE_TEST = [
    (0.05, "PEP", 5)
]
print("Starting large dataset test...")
for test in LARGE_TEST:
    test_final(group_id, "data/large_dataset.txt", *test)


print("----"*30)
print("Final result: {} / {} correct solutions!".format(completed_counter, test_counter))
