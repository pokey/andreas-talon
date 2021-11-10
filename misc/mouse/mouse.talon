settings():
    user.scroll_step = 200

# Buttons
mouse {user.mouse_click}:       user.mouse_click(mouse_click)
mouse drag:                     user.mouse_drag()

# Scroll
scroll up [<number_small>]:     user.mouse_scroll("up", number_small or 1)
scroll down [<number_small>]:   user.mouse_scroll("down", number_small or 1)

climb:                          user.mouse_scrolling("up")
drop:                           user.mouse_scrolling("down")

mouse speed show:               user.mouse_scroll_speed_notify()
mouse speed <number_small>:     user.mouse_scroll_speed_set(number_small)
mouse speed up:                 user.mouse_scroll_speed_increase()
mouse speed down:               user.mouse_scroll_speed_decrease()

mouse gaze:                     user.mouse_gaze_scroll()

# Modes
^mouse calibrate$:              user.mouse_calibrate()
^mouse control$:                user.mouse_toggle_control_mouse()
^mouse zoom$:                   user.mouse_toggle_zoom_mouse()

# Misc
mouse center:                   user.mouse_center_window()

#TODO cursor
^cursor show$:                  user.mouse_show_cursor()
# ^cursor hide$:                  user.mouse_hide_cursor()