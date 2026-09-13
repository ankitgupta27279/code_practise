### 30. Compress a string (e.g., "aaabbc" → "a3b2c1").

def get_compressed_string(test_str: str) -> str:
    new_str=""
    new_temp_str=""
    for i in range(len(test_str)):
        if i==0:
            new_temp_str=test_str[i]
        else:
            if test_str[i]==test_str[i-1]:
                new_temp_str+=test_str[i]
            else:
                new_str+=test_str[i-1]+str(len(new_temp_str))
                new_temp_str=test_str[i]
    new_str+=test_str[i]+str(len(new_temp_str))
    return new_str


if __name__=="__main__":
    sample_string="abbbccdbbcf"
    print(get_compressed_string(sample_string))
