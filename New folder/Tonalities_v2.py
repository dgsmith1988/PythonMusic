from enum import Enum, unique
from music21 import scale

@unique
class Tonality(Enum):
    #Chord formula defintions to be used in conjunction with music21 applications
    Maj = (["M3", "m3"], ["1", "3", "5"])
    Min = (["m3", "M3"], ["1", "b3", "5"])
    Dim = (["m3", "m3"], ["1", "b3", "b5"])
    Sus2 = (["M2", "P4"], ["1", "2", "5"])
    Sus4 = (["P4", "M2"], ["1", "4", "5"])
    Aug = (["M3", "M3"], ["1", "3", "#5"])
    Majb5 = (["M3", "m3", "M3"], ["1", "3", "b5"])
    Maj7 = (["M3", "m3", "M3"], ["1", "3", "5", "7"])
    Maj7s5 = (["M3", "M3", "m3"], ["1", "3", "#5", "7"])
    Maj7b5 = (["M3", "d3", "A3"], ["1", "3", "b5", "7"])
    Maj7sus2 = (["M2", "P4", "M3"], ["1", "2", "5", "7"])
    Maj7sus4 = (["P4", "M2", "M3"], ["1", "4", "5", "7"])
    Maj6 = (["M3", "m3", "M2"], ["1", "3", "5", "6"])
    Dom7 = (["M3", "m3", "m3"], ["1", "3", "5", "b7"])
    Dom7s5 = (["M3", "M3", "d3"], ["1", "3", "#5", "b7"])
    Dom7b5 = (["M3", "d3", "M3"], ["1", "3", "b5", "b7"])
    Dom7sus2 = (["M2", "P4", "m3"], ["1", "2", "5", "b7"])
    Dom7sus4 = (["P4", "M2", "m3"], ["1", "4", "5", "b7"])
    Min7 = (["m3", "M3", "m3"], ["1", "b3", "5", "b7"])
    Min7s5 = (["m3", "A3", "d3"], ["1", "b3", "#5", "b7"])
    Min7b5 = (["m3", "m3", "M3"], ["1", "b3", "b5", "b7"])
    MinMaj7 = (["m3", "M3", "M3"], ["1", "b3", "5", "7"])
    Min6 = (["m3", "M3", "M2"], ["1", "b3", "5", "6"])
    Dim7 = (["m3", "m3", "m3"], ["1", "b3", "b5", "bb7"])
    def __init__(self, edgeList, formula):
        self.edgeList = edgeList
        self.formula = formula
        self.network = scale.intervalNetwork.IntervalNetwork()
        self.network.fillBiDirectedEdges(self.edgeList)
    def __str__(self):
        if self == Tonality.Maj7s5:
            return "Maj7#5"
        elif self == Tonality.Dom7s5:
            return "Dom7#5"
        elif self == Tonality.Min7s5:
            return "Min7#5"
        else:
            return self.name
