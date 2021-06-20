mode: user.mouse_grid
-

<user.letter> <user.letter>:       user.mouse_grid_jump(letter_1, letter_2)

grid {user.mouse_direction}:       user.mouse_grid_move_grid(mouse_direction)
small {user.mouse_direction}:      user.mouse_grid_move(mouse_direction, "small")
[medium] {user.mouse_direction}:   user.mouse_grid_move(mouse_direction, "medium")
large {user.mouse_direction}:      user.mouse_grid_move(mouse_direction, "large")

click [left]:
	user.hide()
	mouse_click(0)

click right:
	user.hide()
	mouse_click(1)

click (middle | mid):
	user.hide()
	mouse_click(2)

click double:
	user.hide()
	mouse_click(0)
	mouse_click(0)