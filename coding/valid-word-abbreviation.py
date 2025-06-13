class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if not word or not abbr:
            return False

        i = j = 0

        while i < len(abbr) and j < len(word):
            if abbr[i].isdigit():
                if abbr[i] == '0':
                    return False # leading zero
                skip = 0

                while i < len(abbr) and abbr[i].isdigit():
                    skip = 10*skip + int(abbr[i])
                    i += 1
                
                j += skip

                if j > len(word):
                    return False
            else:
                if abbr[i] != word[j]:
                    return False
                i += 1
                j += 1
        
        # return True INCORRECT
        return i == len(abbr) and j == len(word)


def test_valid_word_abbreviation():
    sol = Solution()

    # Test Case 1: Example from the prompt
    assert sol.validWordAbbreviation("internationalization", "i12iz4n") == True

    # Test Case 2: Abbreviation is too short
    assert sol.validWordAbbreviation("apple", "a2e") == False

    # Test Case 3: Exact match without abbreviation
    assert sol.validWordAbbreviation("dog", "dog") == True

    # Test Case 4: Abbreviation with numbers
    assert sol.validWordAbbreviation("substitution", "s10n") == True

    # Test Case 5: Invalid number format (leading zero)
    assert sol.validWordAbbreviation("word", "w02d") == False

    # Test Case 6: Empty abbreviation
    assert sol.validWordAbbreviation("hello", "") == False

    # Test Case 7: Full number abbreviation
    assert sol.validWordAbbreviation("hello", "5") == True

    print("All test cases passed!")


# Uncomment the following to run tests
test_valid_word_abbreviation()