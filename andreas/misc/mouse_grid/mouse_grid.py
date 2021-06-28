from talon import Context, Module, actions, ctrl, canvas, app, ui
from user.util import cycle
import math

mod = Module()
ctx = Context()

mod.mode("mouse_grid")

mod.list("mouse_direction", desc="List of mouse directions")
ctx.lists["user.mouse_direction"] = {
    "up", "down", "left", "right"
}

setting_color = mod.setting(
    "mouse_grid_color",
    type=str,
    default="d3d3d3",
    desc="Color of the mouse grid",
)
setting_color_selected = mod.setting(
    "mouse_grid_color_selected",
    type=str,
    default="00ff00",
    desc="Color of the mouse grid selected letter",
)
should_draw_labels = mod.setting(
    "mouse_grid_draw_labels",
    type=bool,
    default=True,
    desc="If true draw labels on the mouse grid",
).get()

_canvas = None
screen = None
x_index = None

def on_draw(canvas):
    paint = canvas.paint
    def_color = setting_color.get()
    w, h = get_cell_size()

    for i in range(26):
        x = i * w
        y = i * h

        if i > 0:
            paint.color = def_color
            canvas.draw_line(x, 0, x, canvas.height)
            canvas.draw_line(0, y, canvas.width, y)

        paint.color = setting_color_selected.get() if i == x_index else def_color
        text = chr(ord("A") + i)
        text_rect = canvas.paint.measure_text(text)[1]
        canvas.draw_text(text, x + w / 2- text_rect.width / 2, text_rect.height)
        paint.color = def_color
        canvas.draw_text(text, 0, y + h / 2 + text_rect.height / 2)

    if should_draw_labels:
        draw_labels(canvas, w, h)

def draw_labels(canvas, w, h):
    paint = canvas.paint
    color = setting_color.get()
    for i in range(1, 26):
        color_x = setting_color_selected.get() if i == x_index else color
        x = i * w
        text_x = chr(ord("A") + i)
        rect_x = canvas.paint.measure_text(text_x)[1]

        for j in range(1, 26):
            y = j * h
            text_y = chr(ord("A") + j)
            rect_y = canvas.paint.measure_text(text_y)[1]
            rect = canvas.paint.measure_text(text_x + text_y)[1]

            paint.color = color_x
            canvas.draw_text(text_x,
                x + w / 2 - rect.width / 2,
                y + h / 2 + rect.height / 2
            )
           
            paint.color = color
            canvas.draw_text(text_y,
                x + w / 2 + rect.width / 2 - rect_y.width,
                y + h / 2 + rect.height / 2
            )

def get_cell_size():
    return screen.width / 26, screen.height / 26

def jump(x: int, y: int):
    w, h = get_cell_size()
    x = x * w + w / 2
    y = y * h + h / 2 
    ctrl.mouse_move(x, y)

@mod.action_class
class Actions:
    def mouse_grid_toggle():
        """Toggle mouse grid"""
        global _canvas, screen, x_index
        if _canvas:
            actions.user.mouse_grid_hide()
        else:
            x_index = None
            screen = ui.main_screen()
            _canvas = canvas.Canvas.from_screen(screen)
            _canvas.register("draw", on_draw)
            _canvas.freeze()
            actions.mode.disable("command")
            actions.mode.enable("user.mouse_grid")

    def mouse_grid_hide():
        """Hide mouse grid"""
        global _canvas
        actions.mode.disable("user.mouse_grid")
        actions.mode.enable("command")
        _canvas.unregister("draw", on_draw)
        _canvas.close()
        _canvas = None

    def mouse_grid_letter(l: str):
        """Select letter. Move cursor on second letter to the specified cell"""
        global x_index
        if x_index:
            jump(
                x_index,
                ord(l) - ord("a")
            )
            x_index = None
        else:
            x_index = ord(l) - ord("a")
        _canvas.freeze()

    def mouse_grid_move(direction: str, size: str):
        """Move mouse cursor"""
        x, y = ctrl.mouse_pos()

        if size == "small":
            diff = 1
        elif size == "medium":
            diff = 10
        elif size == "large":
            diff = 20

        if direction == "up":
            y -= diff
        elif direction == "down":
            y += diff
        elif direction == "left":
            x -= diff
        elif direction == "right":
            x += diff
        ctrl.mouse_move(x, y)

    def mouse_grid_move_grid(direction: str):
        """Move mouse cursor by grid"""
        w, h = get_cell_size()
        x, y = ctrl.mouse_pos()
        x = math.trunc(x / w)
        y = math.trunc(y / h)

        if direction == "up":
            y -= 1
        elif direction == "down":
            y += 1
        elif direction == "left":
            x -= 1
        elif direction == "right":
            x += 1

        jump(
            cycle(x, 0, 25),
            cycle(y, 0, 25),
        )

    def mouse_grid_labels():
        """Toggle labels"""
        global should_draw_labels
        should_draw_labels = not should_draw_labels
        _canvas.freeze()