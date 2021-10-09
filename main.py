# the code must contain the def keyword
# otherwise return "missing def"
# the code must contain the : symbol
# otherwise return "missing :"
# the code must contain ( and ) for the parameter list
# otherwise return "missing paren"
# the code must not contain ()
# otherwise return "missing param"
# the code must contain four spaces for indentation
# otherwise return "missing indent"
# the code must contain validate
# otherwise return "wrong name"
# the code must contain a return statement
# otherwise return "missing return"

def validate(code):
  if "def" not in code:
    return "missing def"
  elif ":" not in code:
    return "missing :"
  elif "(" not in code and ")" not in code:
    return "missing paren"
  elif "()" in code:
    return "missing param"
  elif "    " not in code:
    return "missing indent"
  elif "validate" not in code:
    return "wrong name"
  elif "return" not in code:
    return "missing return"


  validate(validate)