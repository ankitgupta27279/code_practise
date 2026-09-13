### print all permutations of a given string

set_permutations=set()

def get_permutations(s, i=0):
	if i==len(s):
		set_permutations.add("".join(s))

	for j in range(i, len(s)):
		words=[word for word in s]
		words[i], words[j]=words[j], words[i]
		get_permutations(words, i+1)
		words[i], words[j]=words[j], words[i]

	return set_permutations

s="abcefghi"
print(get_permutations(s))
print(len(get_permutations(s)))