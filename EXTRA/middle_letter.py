def mid(mid_let):
  num_let = len(mid_let)
  if num_let % 2 == 1:
      result = num_let // 2
      answer = mid_let[result]
      return answer
  else:
      return ""

mid("abcy")
