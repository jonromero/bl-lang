from vm import VM, put, step

def main():
	print "bl starting"
	line = "Nothing"
	while(line):
		line = input()
		tokenize_and_add(line, VM)
		step(VM)

def tokenize_and_add(sentence, VM):
	# search for delimiter
	# when delim is found
	# split and count the first member
	# do the same for the next part
	# PS: whitespaces don't count
	
	delim = find_delim_in_string(sentence)

	if not delim:
		code = len(sentence.replace(" ", ""))
		put(code, VM)
		return
	
	tokenized = sentence.split(delim)
	tokenized_part = tokenized[0]
	rest = tokenized[1]

	# ignore whitespaces
	code = len(tokenized_part.replace(" ", ""))
	put(code, VM)

	tokenize_and_add(rest, VM)

# FIXME: index is throwing an exception
def find_delim_in_string(sentence):
	#delim = [",", ".", "\n"]
	delim = [","]
	#delim_priority = map(lambda x: {x:sentence.index(x)}, delim)

	return delim[0] if delim[0] in sentence else None

	
main()

