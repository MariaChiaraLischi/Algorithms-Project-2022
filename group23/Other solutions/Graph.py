graph = {}
stocks = []
r = 0

def prepare(filename : str, threshold : float):
    global graph
    global stocks
    global r
    prep = {}

    with open(filename, 'r') as dataset:
        for line in dataset:
            row = line[0:-1].split(',')
            
            if row[0] in prep.keys():
                
                if int(row[1]) > prep[row[0]][1]:
                    prep[row[0]][1] = int(row[1])
                    prep[row[0]][3] = float(row[2])
                    
                elif int(row[1]) < prep[row[0]][0]:
                    prep[row[0]][0] = int(row[1])
                    prep[row[0]][2] = float(row[2])
                    
            else:
               prep[row[0]] = [0,0,0,0]
               prep[row[0]][0], prep[row[0]][2] = int(row[1]), float(row[2])
               prep[row[0]][1], prep[row[0]][3] = int(row[1]), float(row[2])
        
    for stock in prep.keys():
            
        if prep[stock][2] > 0:
            prep[stock] = (prep[stock][3]-prep[stock][2])/prep[stock][2]
        else:
            prep[stock] = 1
        
    for stock1 in prep.keys():
        graph[stock1] = [[]]
        stocks.append(stock1)

        for stock2 in prep.keys():

            if stock1 != stock2 and -1*threshold < prep[stock1]-prep[stock2] < threshold:
                graph[stock1][0].append(stock2)
    
    # r = len(stocks)-2
    
    if r > 0:
        for stock1 in stocks:
            stks = stocks[:]
            stks.remove(stock1)
            for stock2 in graph[stock1][0]:
                stks.remove(stock2)
            for i in range(r):
                graph[stock1].append([])
                for stock2 in graph[stock1][i]:
                    for stock3 in graph[stock2][0]:
                        if stock3 in stks:
                            graph[stock1][i+1].append(stock3)
                            stks.remove(stock3)

def query(stock : str, corr_level : int) -> list:
    global graph
    global stocks
    global r
    
    if corr_level <= r+1:
        graph[stock][corr_level-1].sort()
        return graph[stock][corr_level-1]
    
    stks = stocks[:]
    stks.remove(stock)
    for i in range(r+1):
        for stock2 in graph[stock][i]:
            stks.remove(stock2)
    
    for i in range(r,corr_level-1):
        
        if len(stks) == 0 or len(graph[stock][i]) == 0:
            return []
        
        graph[stock].append([])
                
        for stock2 in graph[stock][i]:
            for stock3 in graph[stock2][0]:
                if stock3 in stks:
                    graph[stock][i+1].append(stock3)
                    stks.remove(stock3)
    
    graph[stock][corr_level-1].sort()
    return graph[stock][corr_level-1]

# Optional!
def num_connected_components() -> int:
    global graph
    global stocks
    global r
    
    sol = 0
    stks1 = stocks[:]
    for stock1 in stocks:
        if stock1 in stks1:
            
            sol += 1
            stks2 = stocks[:]
            stks2.remove(stock1)
            stks1.remove(stock1)
            
            for i in range(r+1):
                for stock2 in graph[stock1][i]:
                    if stock2 in stks2:
                        stks2.remove(stock2)
                        
            for i in range(r, len(stocks)-2):
                                        
                if len(stks2) == 0 or len(graph[stock1][i]) == 0:
                    break
                        
                graph[stock1].append([])

                for stock2 in graph[stock1][i]:
                    for stock3 in graph[stock2][0]:
                        if stock3 in stks2:
                            graph[stock1][i+1].append(stock3)
                            stks2.remove(stock3)
                            
            for i in range(len(graph[stock1])):
                for stock2 in graph[stock1][i]:
                    if stock2 in stks1:
                        stks1.remove(stock2)        

    return sol
