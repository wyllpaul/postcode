import pdb; pdb.set_trace()
format = ['.isalpha()', '.isalpha()', '.isdigit()', '.isalpha()', '.isspace()', '.isdigit()', '.isalpha()', '.isalpha()']
postcode = "AA9A 9AA"

for x, y in zip(format, postcode):
	if not eval("'%s'"%y+x):
		print('error')

	

