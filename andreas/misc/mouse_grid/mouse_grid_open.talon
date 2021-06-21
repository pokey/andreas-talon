mode: user.mouse_grid
-

(mouse grid | stop | esc | escape):   user.mouse_grid_hide()

<user.letter>:                        user.mouse_grid_letter(letter)

grid {user.mouse_direction}:          user.mouse_grid_move_grid(mouse_direction)
small {user.mouse_direction}:         user.mouse_grid_move(mouse_direction, "small")
[medium] {user.mouse_direction}:      user.mouse_grid_move(mouse_direction, "medium")
large {user.mouse_direction}:         user.mouse_grid_move(mouse_direction, "large")

(show | hide) labels:                 user.mouse_grid_labels()

click [left]:
	user.mouse_grid_hide()
	mouse_click(0)

click right:
	user.mouse_grid_hide()
	mouse_click(1)

click (middle | mid):
	user.mouse_grid_hide()
	mouse_click(2)

click double:
	user.mouse_grid_hide()
	mouse_click(0)
	mouse_click(0)