def palindrome(word):
   first = word[:1]
   last = word[-1:] 
   return first == last
palindrome("abc")