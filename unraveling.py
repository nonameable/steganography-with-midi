import midi

class Unraveler:

	def __init__(self):
		print 'Unraveler created'

	def get_hidden_message(self, secret_misi_filename):
		pattern = self.get_pattern(secret_misi_filename)
		message_as_numbers = []
		flag = 0
		for event in pattern[0]:
				if isinstance(event, midi.ChannelAfterTouchEvent) and flag == 1: # for some reason, ProgramChangeEvents are transfored into ChannelAfterTouchEvents...
					message_as_numbers.append(event.data[0])
				elif isinstance(event, midi.NoteOnEvent) and event.get_pitch() == 43 and event.get_velocity() == 0 and event.tick == 0 and event.channel == 0:
					flag = 1
				elif isinstance(event, midi.NoteOffEvent) and event.get_pitch() == 43 and event.tick == 73 and event.channel == 0:
					if flag == 1:
						flag = 2
						print "about to exit"
						break

		message_list = [chr(x) for x in message_as_numbers][::-1]
		message = ''
		for letter in message_list:
			message = message + letter
		return message

	def get_pattern(self, midi_file_name):
		return midi.read_midifile(midi_file_name)