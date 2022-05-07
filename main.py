def inp():
    with open("input", "r") as file:
        data = [int(n) for n in file.read().split()]
        hrosi = data[0]
        rada = data[2::]
    return hrosi, rada

def output(reseni, cesta):
    with open("output", "w") as file:
        cesta = [str(n) for n in cesta]
        vystup = str(reseni) + "\n" + "\n".join(cesta)
        file.write(vystup)

def cubic_solution(hrosi, rada):
    data = [[float("-inf")]*len(rada) for _ in range(hrosi)]
    data[0] = [float("inf") for _ in rada]
    predci = [[None]*len(rada) for _ in range(hrosi)]
    for hroch in range(1, hrosi):
        predek = hroch - 1
        for pozice in range(hroch, len(rada)):
            minimum = float("-inf")
            for pozice_predka in range(hroch - 1, pozice):
                if (minimum < min(rada[pozice] - rada[pozice_predka], data[predek][pozice_predka])):
                    minimum = min(rada[pozice] - rada[pozice_predka], data[predek][pozice_predka])
                    predci[hroch][pozice] = pozice_predka
            data[hroch][pozice] = minimum
    return max(data[-1]), predci

def get_solution(predci, pos):
    cesta = []
    for predek in reversed(predci):
        cesta.append(pos)
        pos = predek[pos]
    return cesta[::-1]

def binary_search(hrosi, rada):
    down_limit = 0
    up_limit = rada[-1]
    while(True):
        minimum = (down_limit + up_limit)// 2
        actual = check_solution(hrosi, rada, minimum)
        ancestor = check_solution(hrosi, rada, minimum - 1)
        if (actual == False) and (ancestor):
            return minimum - 1, ancestor
        elif(actual == False):
            up_limit = minimum
        else:
            down_limit = minimum

def check_solution(hrosi, rada, minimum):
    cesta = []
    predchozi = float("-inf")
    for key, prvek in enumerate(rada):
        vzdalenost = prvek - predchozi
        if (hrosi == 0):
            break
        if (vzdalenost >= minimum):
            cesta.append(key)
            predchozi = prvek
            hrosi -= 1

    if (hrosi == 0):
        return cesta
    else:
        return False
hrosi, rada = inp()
minimum, cesta = binary_search(hrosi, rada)
output(minimum, cesta)