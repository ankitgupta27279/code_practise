### Reverse a string without slicing ([::-1]).

def get_reverse_string_list_reverse(s: str) -> str:
    list_str=list(s)
    list_str.reverse()
    return "".join(list_str)

def get_reverse_string_list_reversed(s: str) -> str:
    return "".join(list(reversed(list(s))))

def get_reverse_string_slicing(s: str) -> str:
    return s[::-1]

def get_reverse_string_list(s: str) -> str:
    return "".join(list(s)[::-1])

def get_reverse_string(s: str) -> str:
    rev_str=""
    for i in range(len(s)-1, -1, -1):
        rev_str+=s[i]
    return rev_str


test_str="welcome"
print(get_reverse_string(test_str))
