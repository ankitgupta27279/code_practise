### 23. Count vowels and consonants

def get_counts(test_str: str) -> dir:
	count_dir={"vowels_count": 0, "consonants_count":0}
	for c in test_str:
		if c in ['a', 'e', 'i', 'o', 'u']:
			count_dir["vowels_count"]+=1
		else:
			count_dir["consonants_count"]+=1
	return count_dir


s="the quick brown fox jumps over the lazy dog"
_count=get_counts(s)
print(f"vowels count--->{_count["vowels_count"]}")
print(f"consonants count--->{_count["consonants_count"]}")