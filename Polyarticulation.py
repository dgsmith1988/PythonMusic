from music21 import stream, pitch, note, duration, articulations, spanner
import random
from Tonalities import *

ql = .25

#for now this will only take a list of two pitches
def addPhraseToMeasure(pitches, measure):
    notes = [note.Note(pitches[0], quarterLength=ql),
             note.Note(pitches[1], quarterLength=ql),
             note.Note(pitches[0], quarterLength=ql)]
    
    notes[0].articulations.append(articulations.Accent())

    for n in notes:
        measure.append(n)

    #add a different articulation to mix it up a bit
    slur = spanner.Slur(notes)
    measure.insert(0, slur)


def createPhrase(pitches):
    notes = [note.Note(pitches[0], quarterLength=ql),
             note.Note(pitches[1], quarterLength=ql),
             note.Note(pitches[0], quarterLength=ql)]

    notes[0].articulations.append(articulations.Accent())

    phrase = stream.Stream()
    for n in notes:
        phrase.append(n)

    #add a different articulation to mix it up a bit
    slur = spanner.Slur(notes)
    phrase.insert(0, slur)
    return phrase


#create a score to hold all the parts
s = stream.Score(id='mainScore')
            
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

#lets create the phrases that will make up the measures
measure1 = stream.Measure()
addPhraseToMeasure([pitch1, pitch2], measure1)
addPhraseToMeasure([pitch3, pitch4], measure1)
addPhraseToMeasure([pitch1, pitch2], measure1)
addPhraseToMeasure([pitch3, pitch4], measure1)
addPhraseToMeasure([pitch1, pitch2], measure1)
lastNote = note.Note(pitch3, quarterLength=ql)
lastNote.articulations.append(articulations.Accent())
measure1.append(lastNote)
part1 = stream.Part(id="part1")
part1.repeatAppend(measure1, 3)
s.insert(0, part1)


#Next steps: figure out how to generate each sucessive part and organize them
#into a more coherent/organized forms (i.e. score->parts->measure)
#Also, how will you generate the other parts? Create one form and then shift everything?
#Create a function to generate each variation? Also there might be a way to organize the tonalities
#on a larger scale (or more generally the shape/contour of the piece) to be able to more dynamically
#generate a whole piece of music...

#How are we going to do this? Is it possible to create one container and then modify each part from within that?
#Or do we dynamically build up the score as we go along? I think this is the way to go. What's the next step in the
#procedure? It looks like I'll need to be creating those functions now... how to do this? Have them take a measure
#refere and modify it or return an entirely new measure (or part) to begin with. It's probably better to keep everything
#consistent so lets have all the functions return parts...

#the outline of the each function will look something like this:
# data = musicGenrativeFucntionCall()
# embed data in the larger part
#
#

s.show()
