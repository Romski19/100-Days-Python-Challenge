def is_anagram(word_a, word_b):
    return sorted(word_a) == sorted(word_b)
      
is_anagram("typhoon", "opython")