# 读 n, sumU, Tmax
def readbase(filename):
    base = []
    with open(filename, 'r') as f:
        line = f.readline()
        line = line.split()
        for i in line:
            base.append(float(i))
    return base


# 读 C[], D[], T[]
def readsample(filename):
    C = []
    D = []
    T = []
    with open(filename, 'r') as f:
        temp = f.readline()
        while True:
            line = f.readline()
            if not line:
                break
            line = line.split()
            print(line)
            C.append(float(line[0]))
            D.append(float(line[1]))
            T.append(float(line[2]))
    return C, D, T


if __name__ == '__main__':
    C, D, T = readsample("aurg.txt")
    n, sumU, Tmax = readbase("aurg.txt")
    print(C, D, T)
