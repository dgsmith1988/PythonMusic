from music21 import *

Dom7EdgeList = ["M3", "m3", "m3", "M2"]
Dom7Formula = ["1", "3", "5", "b7"]

Dom7Net = scale.intervalNetwork.IntervalNetwork()
Dom7Net.fillBiDirectedEdges(Dom7EdgeList)

chords = [(pitch.Pitch("B-6"), "Dom7"), (pitch.Pitch("E-6"), "Dom7"), (pitch.Pitch("F6"), "Dom7"), (pitch.Pitch("A-6"), "Dom7")]

def getIntervalAnswer(question):
    degree1Index = Dom7Formula.index(question[0])
    degree2Index = Dom7Formula.index(question[1])

    if degree1Index < degree2Index:
        if question[2] == "ascending":
            intervalAnswer = interval.add(Dom7Net.realizeIntervals()[degree1Index:degree2Index])
        else:
            intervalAnswer = interval.add(Dom7Net.realizeIntervals()[degree1Index:degree2Index]).complement
    else:
        if question[2] == "ascending":
            intervalAnswer = interval.add(Dom7Net.realizeIntervals()[degree2Index:degree1Index]).complement
        else:
            intervalAnswer = interval.add(Dom7Net.realizeIntervals()[degree2Index:degree1Index])
    return intervalAnswer


degree1 = "3"
degree2 = "b7"
direction = "ascending"

testQuestion = (degree1, degree2, direction)

response = getIntervalAnswer(testQuestion)
print(response.simpleName)

BbDom7 = Dom7Net.realizePitch('b-2')

BbDom7[Dom7Formula.index(testQuestion[0])]
BbDom7[Dom7Formula.index(testQuestion[1])]
