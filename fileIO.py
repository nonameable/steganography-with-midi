class FileIO:

	def get_text_from(self, file_name):
		text = None
		with open(file_name, 'r') as f:
			read_data = f.read()
			text = read_data
		f.closed
		return text

	def print_to_file(self, file_name_to_write, text):
		f=open('./'+ file_name_to_write, 'w+')
		f.write(text +  '\n')
		f.close()
