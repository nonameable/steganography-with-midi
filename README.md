# steganos-with-midi=

Python, for all its amazing ability out of the box, does not provide you with
an easy means to hide information in MIDI files. This is an attempt to do just that.

There are multiple ways to hide information in a MIDI file so that it is not 
noticeable to the human ear. 

Both modules make use of the python-midi libraries located 
here: https://raw.githubusercontent.com/vishnubob/python-midi
## Features

* A module to hide information
* A module to reveal hidden information


## Run it

The code is written in Python 2.7. You must have Python 2.x installed in your machine or in a
conda environment. You could also use a virtual environment. That is up to you.

As said before, you must install in your environment https://raw.githubusercontent.com/vishnubob/python-midi.
The have instructions for that on their repo.

After everything is set up, to run it you need to be in the same directory as midistegano.py. Then you should
place two different files in that same directory


1. A cool MIDI file. I have already added a cool one for you to play with: `avicii.mid`. You can find more cool files
here: http://www.cool-midi.com/

2. A file containing the message you want to hide in a MIDI dile. I have also added one for you: `hola`

To run it you just need to enter into the terminal:


```
python midistegano.py -hide avicii.mid hola
```

This command will generate a file called `secret_in_avicii.mid`. Every file you generate using the `-hide` flag will 
create a new file containing the hidden information with the name: `secret_in_oldFileName.mid`

Now, to reveal the hidden information you just need to change the flag to: `-reveal`:

```
python midistegano.py -reveal secret_in_avicii.mid
```

This command will generate a file containing the secret message named `hidden_message_in_secret_in_avicii`. 