from fileIO import FileIO
from hiding import Hider
from unraveling import Unraveler
import sys
from os import path  

intention=sys.argv[1]
midi_file_name=sys.argv[2]
name = None

if intention=="-hide":
    message_file_name = sys.argv[3]
    if path.isfile(midi_file_name):
        if path.isfile(message_file_name):
            parts=midi_file_name.split(".")
            extension=parts[-1]
            if extension != "mid":
                print "The file must have a .mid extension"
            else:
                fileIO = FileIO()
                message = fileIO.get_text_from(message_file_name)
                hider = Hider()
                hider.hide(midi_file_name,message)
                print "The output file name will be: " "secret_in_"+ midi_file_name  
        else:
            print "You must put the message file in the same directory as midistegano.py" 

        
    else:
        print "You must put the .mid file in the same directory as run.py" 

elif intention=="-reveal":
    if path.isfile(midi_file_name):
        parts=midi_file_name.split(".")
        name = parts[0];
        extension=parts[-1]
        if extension != "mid":
            print "The file must have a .mid extension"
        else:
            unraveler = Unraveler()
            hidden_message = unraveler.get_hidden_message(midi_file_name)
            print "The hidden message is: %s" % hidden_message
            fileIO = FileIO()
            fileIO.print_to_file('hidden_message_in_' + name, hidden_message)
    else:
        print "The midi file you entered does not exist. Please enter a valid midi filename" 

else:
    error_message = intention + " is not a midistegano valid flag. Write either -hide or -reveal"
    print error_message


