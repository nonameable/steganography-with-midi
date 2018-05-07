import midi

class Hider:

	def __init__(self):
		print 'Hider created'	

	def hide(self, midi_file_name, message):

		result = None
		pattern  = self.get_pattern(midi_file_name)
		number_of_tracks = len(pattern);
		
		# in case the midi file has no tracks (that means, no music)
		# we add one so we can add the hidden data there
		# this track will not have any Note events, so it will not add sound
		# If it does have one, we work with that track
		if number_of_tracks == 0:
			# Instantiate a MIDI Track (contains a list of MIDI events)
			track = midi.Track()
			# Append the track to the pattern
			pattern.append(track)


		# Now we need to add a termination line, so we know we need to stop reading
		# Instantiate a MIDI note off event, append it to the track
		off = midi.NoteOffEvent(tick=73, pitch=midi.G_3)
		pattern[0].insert(0, off)

		# Insert the hidden messages as Program change events at the start of the list.
		# (you could also add them at the end as the user will not detect them since
		# no sound would be comming out .... but it has one problem
		# If you want to verify the insertion
		# You have to scroll to the end of the file and check. If the midi file 
		# is really big, this could be really time consuming) 
		# 
		# We cannot add them in the middle, since the change of instruments could be
		# noticeable

		channelToAlter = 16 # This channel might not even be used by any other event
		for char in message:
			number = ord(char)
			change_program = midi.ProgramChangeEvent(tick=0, channel=channelToAlter, data=[number])
			pattern[0].insert(0, change_program)

		on = midi.NoteOnEvent(tick=0, velocity=0, pitch=midi.G_3)
		pattern[0].insert(0, on)

		new_midi_file_name = "secret_in_"  + midi_file_name
		self.save_midi_file(pattern, new_midi_file_name)

		


	def get_pattern(self, midi_file_name):
		return midi.read_midifile(midi_file_name)

	def save_midi_file(self, pattern, new_midi_file_name):
		midi.write_midifile(new_midi_file_name, pattern)