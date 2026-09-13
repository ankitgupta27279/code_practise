### 29. Find the longest word in a sentence.

def get_longest_word_1(test_str: str) -> str:
    _len=float('-inf')
    _word=""
    for word in test_str.split():
        if len(word)>_len:
            _len=len(word)
            _word=word
    return _word

def get_longest_word_2(test_str: str) -> str:
    temp_list=test_str.split()
    # temp_list.sort(key=lambda x: len(x), reverse=True)
    temp_list.sort(key=len, reverse=True)
    return temp_list[0]


if __name__=="__main__":
    test_str="welcome to grasshopper the jungle"
    print(get_longest_word_2(test_str))
