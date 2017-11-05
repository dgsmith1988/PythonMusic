from music21 import stream, pitch, note, duration, articulations, spanner
import random
from Tonalities import *

ql = .25

#for now this will only take a list of two pitches
def createPhrase(pitches, length):
    notes = []
    for i in range(0, length):
        notes.append(note.Note(pitches[i%2], quarterLength=ql))

    if length != 1:
        notes[0].articulations.append(articulations.Accent())

    phrase = stream.Stream()
    for n in notes:
        phrase.append(n)

    #add a different articulation to mix it up a bit
    if length != 1:
        slur = spanner.Slur(notes)
        phrase.insert(0, slur)
    return phrase

def createPart1(pitches):
    #lets create the phrases that will make up the measures
    phrase1 = createPhrase(pitches[0:2], 3)
    phrase2 = createPhrase(pitches[2:4], 3)
    phrase3 = stream.Stream()
    phrase3.append(phrase1)
    phrase3.append(phrase2)
    #now lets put them in a measure
    measure1 = stream.Measure()
    measure1.repeatAppend(phrase3, 2)
    measure1.append(phrase1)
    measure1.append(createPhrase(pitches[2:3], 1))
    part1 = stream.Part(id="part1")
    part1.repeatAppend(measure1.flat, 3)
    return part1

def createPart2(pitches):
    #lets create the phrases that will make up the measures
    phrase1 = createPhrase(pitches[0:2], 3)
    phrase2 = createPhrase(pitches[2:4], 3)
    phrase3 = stream.Stream()
    phrase3.append(phrase1)
    phrase3.append(phrase2)
    measure1 = stream.Measure()
    measure1.append(createPhrase(pitches[2:4], 2))
    measure1.repeatAppend(phrase3, 2)
    measure1.append(createPhrase(pitches[0:2], 2))
    part2 = stream.Part(id="part2")
    part2.repeatAppend(measure1.flat, 3)
    return part2

def createPart3(pitches):
    #lets create the phrases that will make up the measures
    phrase1 = createPhrase(pitches[0:2], 3)
    phrase2 = createPhrase(pitches[2:4], 3)
    phrase3 = stream.Stream()
    phrase3.append(phrase1)
    phrase3.append(phrase2)
    measure1 = stream.Measure()
    measure1.append(createPhrase(pitches[2:3], 1))
    measure1.repeatAppend(phrase3, 2)
    measure1.append(phrase1)
    part3 = stream.Part(id="part3")
    part3.repeatAppend(measure1.flat, 3)
    return part3

#create a score to hold all the parts
s = stream.Score(id='mainScore')
#s = stream.Stream(id='mainScore')
            
#arbitrary pitch for the moment
Root = "C4"

#Create a tonal structure to select pitches from
CMinMaj7 = scale.ConcreteScale(pitches = Tonality.MinMaj7.network.realizePitch(Root))

#create 3 measures of the first part
#there are several ways to go about selecting the starting pitch but for now lets do it randomly
pitch1 = CMinMaj7.pitchFromDegree(random.randint(1, CMinMaj7.getDegreeMaxUnique()))
pitch2 = CMinMaj7.next(pitch1)
pitch3 = CMinMaj7.pitchFromDegree(random.randint(1, CMinMaj7.getDegreeMaxUnique()))
#lets ensure that the two starting pitches are different (for now at least...)
while(pitch3 == pitch1):
    pitch3 = CMinMaj7.pitchFromDegree(random.randint(1, CMinMaj7.getDegreeMaxUnique()))
pitch4 = CMinMaj7.next(pitch3)

part1 = createPart1([pitch1, pitch2, pitch3, pitch4])
part2 = createPart2([pitch4, pitch3, pitch2, pitch1])
part3 = createPart3([pitch3, pitch4, pitch1, pitch2])
s.insert(0, part1)
s.insert(0, part2)
s.insert(0, part3)
#part1.show()
#part2.show()
#part3.show()
#s.show('text')
s.show()
