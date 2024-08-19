
define _game_menu_screen = 'saves'

style centered_grid is grid:
    align (0.5, 0.5)
    spacing 30
style centered_hbox is hbox:
    align (0.5, 0.5)
    spacing 10
style centered_vbox is vbox:
    align (0.5, 0.5)
    spacing 10
style centered_button is button:
    align (0.5, 0.5)
style centered_button_text is text:
    align (0.5, 0.5)
    insensitive_color "#888"
    idle_color "#c00"
    hover_color "#f00"
style centered_label is label:
    align (0.5, 0.5)

label main_menu:
    while True:
        call screen main_menu()

screen main_menu():
    tag menu
    style_prefix "centered"
    vbox:
        textbutton "Start":
            action Start()
        textbutton "Load":
            action ShowMenu("saves")

screen saves():
    tag menu
    style_prefix "centered"
    grid 3 4:
        for i in range(12):
            $ slot = "save-{}".format(i)
            vbox:
                label __("Save slot {}").format(i)
                hbox:
                    textbutton "Load":
                        action FileLoad(slot)
                    textbutton "Save":
                        action FileSave(slot.format(i, confirm=False))
    vbox:
        align (0., 0.)
        textbutton "Return":
            xalign 0.
            action Return()
        if not main_menu:
            textbutton "Main menu":
                xalign 0.
                action MainMenu()

screen yesno_prompt(message="", yes_action=None, no_action=None):
    style_prefix "centered"
    add "black":
        alpha 0.8
    vbox:
        label message
        textbutton "Yes" action yes_action
        textbutton "No" action no_action
