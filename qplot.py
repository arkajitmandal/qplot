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
    """