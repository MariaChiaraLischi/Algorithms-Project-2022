from . import utils

ordr = [[],[]]
t = -1

def prepare(filename : str, threshold : float):
    global ordr
    global t
    prep = {}
    rend = [[],[]]

    t = threshold

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
        rend[0].append(stock)

        if prep[stock][2] > 0:
            rend[1].append((prep[stock][3]-prep[stock][2])/prep[stock][2])
        else:
            rend[1].append(1)

    ordrr = utils.MergeSort(rend[1], rend[0])
    ordr = [ordrr[1],ordrr[0]]

def query(stock : str, corr_level : int) -> list:
    global ordr
    global t
    sol = []

    ind = ordr[0].index(stock)

    maxx = ordr[1][ind]
    imax = ind
    flag = True
    for i in range(corr_level):
        maxx += t
        imaxp = imax
        while ordr[1][imax] < maxx:
            if imax < len(ordr[1])-1:
                imax += 1
            else:
                imax += 1
                break
        imax -= 1
        maxx = ordr[1][imax]
        if imax == imaxp:
            flag = False
            break

    if flag:
        for j in range(imaxp+1,imax+1):
            sol.append(ordr[0][j])

    minn = ordr[1][ind]
    imin = ind
    flag = True
    for i in range(corr_level):
        minn -= t
        iminp = imin
        while ordr[1][imin] > minn:
            if imin > 0:
                imin -= 1
            else:
                imin -= 1
                break
        imin += 1
        minn = ordr[1][imin]
        if imin == imaxp:
            flag = False
            break
        
    if flag:
        for j in range(imin,iminp):
            sol.append(ordr[0][j])
    
    sol = utils.AlphaMergeSort(sol)
    return sol

def num_connected_components() -> int:
    global ordr
    global t
    
    sol = 0
    stks = ordr[0][:]
    for stock in ordr[0][:]:
        if stock in stks:
            
            sol += 1

            ind = ordr[0].index(stock)

            maxx = ordr[1][ind]
            imax = ind
            for i in range(len(ordr[0][:])-1):
                maxx += t
                imaxp = imax
                while ordr[1][imax] < maxx:
                    if imax < len(ordr[1])-1:
                        imax += 1
                    else:
                        imax += 1
                        break
                imax -= 1
                maxx = ordr[1][imax]
                if imax == imaxp:
                    break

            for j in range(ind,imax+1):
                stks.remove(ordr[0][j])

            minn = ordr[1][ind]
            imin = ind
            for i in range(len(ordr[0][:])-1):
                minn -= t
                iminp = imin
                while ordr[1][imin] > minn:
                    if imin > 0:
                        imin -= 1
                    else:
                        imin -= 1
                        break
                imin += 1
                minn = ordr[1][imin]
                if imin == iminp:
                    break

            for j in range(imin,ind-1):
                stks.remove(ordr[0][j])

    return sol
