import random
from music21 import *

chords = []

directions = ("ascending", "descending")
chordTypes = ["Dom7"]

Dom7MapKeys = ["1", "3", "5", "b7"]
Dom7KeysToIndex = {"1":1, "3":2, "5":3, "b7":4}
Bb_Dom7 = scale.ConcreteScale(pitches = ["B-3", "D4", "F4", "A-4"])
Eb_Dom7 = scale.ConcreteScale(pitches = ["E-3", "G3", "B-3", "D-4"])
F_Dom7 = scale.ConcreteScale(pitches = ["F3", "A3", "C4", "E-4"])
Ab_Dom7 = scale.ConcreteScale(pitches = ["A-3", "C4", "E-4", "G-4"])

chords.append((Bb_Dom7, Dom7KeysToIndex, Dom7MapKeys, chordTypes[0]))
chords.append((Eb_Dom7, Dom7KeysToIndex, Dom7MapKeys, chordTypes[0]))
chords.append((F_Dom7, Dom7KeysToIndex, Dom7MapKeys, chordTypes[0]))
chords.append((Ab_Dom7, Dom7KeysToIndex, Dom7MapKeys, chordTypes[0]))

for chord in chords:
        for tonalFunction1 in sorted(chord[1]):
                print(chord[0].pitchFromDegree(chord[1][tonalFunction1]))
        print("----")
print("")

while(True):
        chord = random.choice(chords)
        chordTone1 = random.choice(chord[2])
        smallerList = chord[2].copy()
        smallerList.remove(chordTone1)
        chordTone2 = random.choice(smallerList)
        direction = random.choice(directions)
        print("What is the interval from", chordTone1, "-", chordTone2, direction, "?")
        input()
        if(chord[1][chordTone1] < chord[1][chordTone2]):
                if(direction == directions[0]):
                        intervalBetweenTones = chord[0].intervalBetweenDegrees(chord[1][chordTone1], chord[1][chordTone2]) 
                else:
                        #use the inverse of the interval
                        intervalBetweenTones = chord[0].intervalBetweenDegrees(chord[1][chordTone1], chord[1][chordTone2]).complement
        elif(chord[1][chordTone1] > chord[1][chordTone2]):
                if(direction == directions[0]):
                        intervalBetweenTones = chord[0].intervalBetweenDegrees(chord[1][chordTone1], chord[1][chordTone2]).complement 
                else:
                        #use the inverse of the interval
                        intervalBetweenTones = chord[0].intervalBetweenDegrees(chord[1][chordTone1], chord[1][chordTone2])

        print(intervalBetweenTones.simpleName, "=" , intervalBetweenTones.semitones, "semitones")
        print("Apply this to", chord[0].tonic.name, chord[3])
        input()
        print(chord[0].pitchFromDegree(chord[1][chordTone1]), chord[0].pitchFromDegree(chord[1][chordTone2]))
        reply = input("Press enter for another example, type stop to exit: ")
        if reply == "stop":
                break
