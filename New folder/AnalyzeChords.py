from music21 import chord, stream
from Tonalities_v2 import *

#arbitrary pitch for the moment
Root = "A4"

stream1 = stream.Stream()
tonalities = []

#Create a tonal structure to select pitches from
for member in Tonality.__members__.items():
    tonalities.append(scale.ConcreteScale(pitches = member[1].network.realizePitch(Root)))
#tonalities.append(scale.ConcreteScale(pitches = Tonality.MinMaj7.network.realizePitch(Root)))
#tonalities.append(scale.ConcreteScale(pitches = Tonality.Dim7.network.realizePitch(Root)))


for tonality in tonalities:
    pitches = tonality.getPitches()
    measure1 = stream.Measure()
    for i in range(len(pitches)-2):
        c = chord.Chord(pitches[i:len(pitches)-1])
        c.annotateIntervals(stripSpecifiers=False)
        measure1.append(c)
        #c.show()
    stream1.append(measure1)
stream1.show()
