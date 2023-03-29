import numpy as np
import math

global description1
global description2
global description3
global description4

description1 = "y = sin(x\u00B2+cosx)"
description2 = "y = x\u00B3 +4.81x\u00B2−17.37x + 5.38"
description3 = "y = 3x\u2075−5x\u2074−3.32x\u00B3+x\u00B2−7.234x+1"
description4 = "y = sin(4x) + cosx"

global eq1
global eq2
global eq3
global eq4

def eq1(x):
    return np.sin(x ** 2 + np.cos(x))


def eq2(x):
    return x ** 3 + 4.81 * x ** 2 - 17.37 * x + 5.38


def eq3(x):
    return 3 * x ** 5 - 5 * x ** 4 - 3.32 * x ** 3 + x ** 2 - 7.234 * x + 1


def eq4(x):
    return math.sin(x * 4) + math.cos(x)


equations = {
    1: eq1,
    2: eq2,
    3: eq3,
    4: eq4,
}
descriptions = {
    1: description1,
    2: description2,
    3: description3,
    4: description4,
}
