def rec_generate(s, prefix=""):
	if len(s) == 0:
		return [prefix]
	permutations = []
	for i in xrange(len(s)):
		suffixes = rec_generate(s[:i] + s[i+1:], s[i])
		for suffix in suffixes:
			permutations.append(prefix + suffix)
	return permutations

def test_rec_generate():
	print rec_generate("LSE")

# test_rec_generate()