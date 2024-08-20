default fruit_jar = Jar(maximum = 10)
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
