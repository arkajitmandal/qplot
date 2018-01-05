# Global Colors 
cyan = '\033[96m'
pink = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yeollow = '\033[93m'
red = '\033[91m'
norm = '\033[0m'

colors = [green,red,blue,yeollow,pink,cyan]


def echo(msg, color = 0, colorset = colors) :
    """
    msg with
    a color choice
    """
    ENDC = '\033[0m'
    return colorset[color] + msg + ENDC


def getSize():
    """
    get terminal size
    return [height, width]
    """
    import os
    dat = os.popen("stty size").read()
    return [int(i) for i in dat.split()]

def read(filename):
    """
    read a file with n columns
    example : 
    1 0.123 0.11 0.11 0.23
    2 0.573 0.16 0.19 0.20
    3 0.511 0.13 0.01 0.26
    return 1d array for all
    columns
    """
    fob = [i.replace("\n","").split() for i in open(filename).readlines()]
    columns = len(fob[0])
    rows = len(fob)
    data = []
    for i in range(columns):
        data.append([])
        for j in range(rows):
            data[-1].append(fob[j][i])
    return data

def plot(x, y) :
    """
    x and y are arrays
    """
    import os
    size = getSize()
    if size[0] < 25 :
        print colors[2] + "Your Terminal height is too low!"
    if size[0] < 100 :
        print colors[2] + "Your Terminal width is too low!"
    # Clear Screen
    os.system("clear")