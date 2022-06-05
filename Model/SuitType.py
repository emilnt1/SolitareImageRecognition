from enum import Enum


class SuitType(Enum):
    H = 1
    S = 2
    D = 3
    C = 4

def concludeFromString(string):
    if string == "H":
        return SuitType.H
    elif string == "S":
        return SuitType.S
    elif string == "D":
        return SuitType.D
    elif string == "C":
        return SuitType.C

