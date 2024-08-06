# Longest substring without repeating characters

def longest_substring_without_repeating_character(s):

    char_set = set()
    max_len = 0
    current_len = 0
    l = 0
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        current_len = r-l+1
        # if current_len > max_len:
        #     max_len = current_len
        max_len = max(max_len, r-l+1)
    return max_len

s = "abcabcdbbbb"

print(longest_substring_without_repeating_character(s))