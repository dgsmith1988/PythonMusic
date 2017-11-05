import random
from enum import Enum, unique
from Tonalities import *
from music21 import *

@unique
class Direction(Enum):
    Ascending = 0
    Descending = 1

class Question():
    def __init__(self, direction, tonality, degree1, degree2)
        self.direction = direction
        self.tonality = tonality
        self.degree1 = degree1
        self.degree2 = degree2

directions = ("ascending", "descending")
questions = []
chords = []

#chords.append((pitch.Pitch("B-6"), chordTypes[0]))
#chords.append((pitch.Pitch("E-6"), chordTypes[0]))
#chords.append((pitch.Pitch("F6"), chordTypes[0]))
#chords.append((pitch.Pitch("A-6"), chordTypes[0]))
chords.append((pitch.Pitch("C#6"), chordTypes[16]))

def getIntervalAnswer(question):
    degree1Index = question.tonality.formula.index(question.degree1)
    degree2Index = question.tonality.formula.index(question.degree2)

    if degree1Index < degree2Index:
        if question.direction == Question.Ascending:
            intervalAnswer = interval.add(question.tonality.network.realizeIntervals()[degree1Index:degree2Index])
        else:
            intervalAnswer = interval.add(question.tonality.network.realizeIntervals()[degree1Index:degree2Index]).complement
    else:
        if question.direction == Question.Descending:
            intervalAnswer = interval.add(question.tonality.network.realizeIntervals()[degree2Index:degree1Index]).complement
        else:
            intervalAnswer = interval.add(question.tonality.network.realizeIntervals()[degree2Index:degree1Index])
    return intervalAnswer

#lets generate all possible combinations of scale degrees and directions, there's a more efficient way to do this using python libraries
for x in Dim7Formula:
        temp = Dim7Formula.copy()
        temp.remove(x)
        for y in temp:
                questions.append((x, y ,directions[0]))
                questions.append((x, y ,directions[1]))

#lets test the answering functionality
##for x in questions:
##        print("The interval from %s to %s %s is %s" % (x[0], x[1], x[2], getIntervalAnswer(x).simpleName))
 

#now that we have all the questions generated lets randomize these bitches...
loop = True
while(loop):
    questionsToBeAsked = questions.copy()
    random.shuffle(questionsToBeAsked)
    #now lets take a question and ask it to ourselves...
    while len(questionsToBeAsked) != 0:
        currentQuestion = questionsToBeAsked.pop()
        print("What is the interval from %s to %s %s?" % (currentQuestion[0], currentQuestion[1], currentQuestion[2]))
        #lets find the answer to the current question
        input()
        print(getIntervalAnswer(currentQuestion).simpleName)
        chordSelection = random.choice(chords)
        print("Apply this to %s %s" % (chordSelection[0].name, chordSelection[1]))
        input()
        Dim7Chord = Dim7Net.realizePitch(chordSelection[0])
        index1 = Dim7Formula.index(currentQuestion[0])
        index2 = Dim7Formula.index(currentQuestion[1])
        print("%s to %s" % (Dim7Chord[index1].name, Dim7Chord[index2].name) )
        reply = input("Press enter for another question, type stop to exit: ")
        if reply == "stop":
            loop = False
            break
    print("Out of questions, reshuffling...")
