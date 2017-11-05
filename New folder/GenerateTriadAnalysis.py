from music21 import chord, stream
from Tonalities_v3 import *

#arbitrary pitch for the moment
Root = "A4"

stream1 = stream.Stream()
triads = []

#Create a tonal structure to select pitches from
for member in Triad.__members__.items():
    triads.append(scale.ConcreteScale(pitches = member[1].network.realizePitch(Root)))

for triad in triads:
    pitches = triad.getPitches()
    inversions = [chord.Chord(pitches[0:3]), chord.Chord(pitches[1:4]), chord.Chord([pitches[2], pitches[3], pitches[1].transpose('p8')])]
    #lets cycle through the inversions now and decompose them into the intervals
    for i in range(3):
        c = inversions[i]
        c.annotateIntervals(stripSpecifiers=False)
        measure1 = stream.Measure()
        measure1.append(c)
        for j in range(1, len(c.pitches)-1):
            c2 = chord.Chord(c.pitches[j:len(c.pitches)])
            c2.annotateIntervals(stripSpecifiers=False)
            measure1.append(c2)
        stream1.append(measure1)
stream1.show()
