"""longest-substring-without-repeating-characters 

Understand the Question:
I am given a string (s) and I want to return the length of a sequence that has highest number of (non-repeating) chars in a row

Clarifying questions:
1. Constraint on characters? will s contain letters? numbers? punctuation?  - INCLUDES letter, digits, characters, symbols and spaces
2. Is there a min or max length of s? (something that we can fit in memory)
3. Is there chance to have an empty string? YES

Examples
a -> 1
ab -> 2
aabbb -> 2
dvdfl -> 4
" " -> 1
"" = 0

Brainstorm ideas:
1. have an empty unique set, and a current_unique_char count, max_count loop 
through the string, check if  the current char in set, if not add that char to 
the set and add 1 to current count, if char is in the set, assign current_count 
to max count and empty the set - *this will fail because all chars are emptied
2. use a slide window and store the length of the window and check if max_len,
update if true, if duplicate char, slide the window to the right and **remove the 
duplicate (and any chars prior to the duplicate in ths list in s) from the set
and move the i (start) pointer to the right until the duplicate char is removed
basically closing the window past the duplicate
"""

def length_of_longest_substring(s: str) -> int:
        if not s:
            return 0
        
        unique = set()
        max_count = 0
        # create 2nd pointer to indicate the start of the sliding window
        i = 0

        for j in range(len(s)):
            # if this item is already in the set, remove the duplicate (and any
            #  chars prior to the duplicate in ths list in s) from the set and move
            #  the i (start) pointer to the right until the duplicate char is removed
            #basically closing the window past the duplicate
            while s[j] in unique:
                unique.remove(s[i])
                i += 1
            # adding a first seen char to the set to keep track of unique chars seen
            unique.add(s[j])
            
            max_count = max(max_count, len(unique))
            
        return max_count

def main():
    assert length_of_longest_substring("dvdf") == 3
    assert length_of_longest_substring("aabbb") == 2
    assert length_of_longest_substring("a") == 1
    assert length_of_longest_substring(" ") == 1
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("abcabcbb") == 3
    print("assertion tests passed!")


if __name__ == "__main__":
    main()


# Time: O(n)
# Space: O(m) where m = size of unique set