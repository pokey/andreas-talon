from talon import Context, Module, actions, ctrl, canvas, app, ui

mod = Module()
ctx = Context()

mod.list("mouse_direction", desc="List of mouse directions")
ctx.lists["user.mouse_direction"] = {
    "up", "down", "left", "right"
}

_canvas = None
screen = None

def on_draw(canvas):
    paint = canvas.paint
    paint.color = "d3d3d3"
    w = canvas.width / 26
    h = canvas.height / 26
    x = 0
    y = 0
    c = ord("A")

    for i in range(26):
        if i > 0:
            canvas.draw_line(x, 0, x, canvas.height)            
            canvas.draw_line(0, y, canvas.width, y)

        text = chr(c)
        text_rect = canvas.paint.measure_text(text)[1]
        canvas.draw_text(text, x + w / 2, text_rect.height)
        canvas.draw_text(text, 0, y + h / 2 + text_rect.height / 2)
           
        x += w
        y += h
        c += 1


@mod.action_class
class Actions:
    def mouse_spread_grid():
        """Toggle mouse spread grid"""
        global _canvas, screen
        if _canvas:
            _canvas.unregister("draw", on_draw)
            _canvas.close()
            _canvas = None
        else:
            screen = ui.main_screen()
            _canvas = canvas.Canvas.from_screen(screen)
            _canvas.register("draw", on_draw)
            _canvas.freeze()

    def mouse_spread_jump(x: str, y: str):
        """Move cursor to the specified cell"""
        x = ord(x) - ord("a")
        y = ord(y) - ord("a")
        w = screen.width / 26
        h = screen.height / 26
        x = x * w + w / 2
        y = y * h + h / 2 
        ctrl.mouse_move(x, y)

    def mouse_spread_move(direction: str):
        """Move mouse cursor"""
        print(direction)
        x, y = ctrl.mouse_pos()
        diff = 10
        if direction == "up":
            y -= diff
        elif direction == "down":
            y += diff
        elif direction == "left":
            x -= diff
        elif direction == "right":
            x += diff
        ctrl.mouse_move(x, y)


# _canvas.register('mousemove', on_draw)
    # paint.style = paint.Style.STROKE
    # paint.stroke_width = 2