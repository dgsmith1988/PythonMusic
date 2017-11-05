import random
from enum import Enum, unique
from Tonalities import *
from music21 import pitch, interval

#Select the chords you want to practice here
tonalitiesToDrill = [
                    #(pitch.Pitch("C4"), Tonality.Dom7),
                    #(pitch.Pitch("C#4"), Tonality.Dim7),
                    (pitch.Pitch("A4"), Tonality.Dom7),
                    (pitch.Pitch("E4"), Tonality.Dom7)
                    ]

@unique
class Direction(Enum):
    Ascending = 0
    Descending = 1

class Question():
    def __init__(self, direction, tonality, degrees):
        self.direction = direction
        self.tonality = tonality
        self.degrees = degrees
    def __repr__(self):
        return "What is the interval from %s to %s %s?" % (self.degrees[0], self.degrees[1], self.direction.name)
        
        
def getIntervalAnswer(question):
    degree1Index = question.tonality.formula.index(question.degrees[0])
    degree2Index = question.tonality.formula.index(question.degrees[1])

    if degree1Index < degree2Index:
        if question.direction == Direction.Ascending:
            intervalAnswer = interval.add(question.tonality.network.realizeIntervals()[degree1Index:degree2Index])
        else:
            intervalAnswer = interval.add(question.tonality.network.realizeIntervals()[degree1Index:degree2Index]).complement
    else:
        if question.direction == Direction.Ascending:
            intervalAnswer = interval.add(question.tonality.network.realizeIntervals()[degree2Index:degree1Index]).complement
        else:
            intervalAnswer = interval.add(question.tonality.network.realizeIntervals()[degree2Index:degree1Index])
    return intervalAnswer

loop = True
while(loop):
    for tonality in tonalitiesToDrill:
        #we want to generate all possible interval combinations in both directions for the given tonality
        questions = []
        for degree1 in tonality[1].formula:
            for degree2 in tonality[1].formula:
                if degree1 != degree2:
                    questions.append(Question(Direction.Ascending, tonality[1], (degree1, degree2)))
                    questions.append(Question(Direction.Descending, tonality[1], (degree1, degree2)))

        #randomize the questions for this particular tonality
        random.shuffle(questions)
        for q in questions:
            print(q)
            input()
            print(getIntervalAnswer(q).simpleName)
            print("Apply this to %s %s" % (tonality[0].name, tonality[1]))
            input()
            concreteTonalStructure = tonality[1].network.realizePitch(tonality[0])
            index1 = tonality[1].formula.index(q.degrees[0])
            index2 = tonality[1].formula.index(q.degrees[1])
            print("%s to %s" % (concreteTonalStructure[index1].name, concreteTonalStructure[index2].name) )
            reply = input("Press enter for another question, type stop to exit: ")
            if reply == "stop":
                loop = False
                break
    print("!\nOut of questions, reshuffling...\n!")
        
#lets test the question functionality        
##for q in questions:
##    print(q)

#lets test the answering functionality
##for q in questions:
##    print("%s %s" % (q, getIntervalAnswer(q).simpleName))

#now that we have all the questions generated lets randomize these bitches...
##loop = True
##while(loop):
##    questionsToBeAsked = questions.copy()
##    random.shuffle(questionsToBeAsked)
##    #now lets take a question and ask it to ourselves...
##    while len(questionsToBeAsked) != 0:
##        currentQuestion = questionsToBeAsked.pop()
##        print("What is the interval from %s to %s %s?" % (currentQuestion[0], currentQuestion[1], currentQuestion[2]))
##        #lets find the answer to the current question
##        input()
##        print(getIntervalAnswer(currentQuestion).simpleName)
##        chordSelection = random.choice(chords)
##        print("Apply this to %s %s" % (chordSelection[0].name, chordSelection[1]))
##        input()
##        Dim7Chord = Dim7Net.realizePitch(chordSelection[0])
##        index1 = Dim7Formula.index(currentQuestion[0])
##        index2 = Dim7Formula.index(currentQuestion[1])
##        print("%s to %s" % (Dim7Chord[index1].name, Dim7Chord[index2].name) )
##        reply = input("Press enter for another question, type stop to exit: ")
##        if reply == "stop":
##            loop = False
##            break
##    print("Out of questions, reshuffling...")
