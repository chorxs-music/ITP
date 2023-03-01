midiNote = 120

if midiNote <  64:
    print("The note value entered is smaller than 64")
    if midiNote == 48:
        print(f"The MIDI note name for {midiNote} is C2")
    elif midiNote == 40:
        print(f"The MIDI note name for {midiNote} is E1")
else:
    print("MIDI note number is greater or equal to 64 or is invalid")
