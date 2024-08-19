define fruit_jar = Jar()
label start:
  menu:
    "You have [fruit_jar.count] items"
    "Add one":
      $ fruit_jar.add(1)
    "Take one":
      $ fruit_jar.take(1)
    "Quit":
      $ renpy.quit()
  jump start
