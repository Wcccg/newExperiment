class Task:
    def __init__(self):
        self.C = 0
        self.D = 0
        self.T = 0

# 读 n, sumU, Tmax
def readbase(filename):
    base = []
    with open(filename, 'r') as f:
        line = f.readline()
        line = line.split()
        for i in line:
            i = float(i)
            if i >= 1:
                i = int(i)
            base.append(i)
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
            C.append(float(line[0]))
            D.append(float(line[1]))
            T.append(float(line[2]))
    return C, D, T


def readTask(filename):
    task = []
    with open(filename, 'r') as f:
        temp = f.readline()
        while True:
            line = f.readline()
            if not line:
                break
            line = line.split()
            temp = Task()
            temp.C = float(line[0])
            temp.D = float(line[1])
            temp.T = float(line[2])
            task.append(temp)
    return task
