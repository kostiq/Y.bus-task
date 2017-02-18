def list_format(input_list):
	start = True
	empty = False
	for string in input_list:
		if string:
			if empty:
				empty = False
				yield ''
			yield string
		elif not start:
			empty = True
			continue
		else:
			start = False
			continue
