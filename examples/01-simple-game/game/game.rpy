default gender = None
label start:
  "Hello"
  menu:
    "Are you a boy or a girl?"
    "A boy":
      $ gender = 0b0
    "A girl":
      $ gender = 0b1
    "Both":
      $ gender = 0b10
    "Neither":
      $ gender = 3
