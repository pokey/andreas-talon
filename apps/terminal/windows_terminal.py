from talon import Module, Context, actions

key = actions.key
insert = actions.insert
ctx = Context()
mod = Module()


mod.apps.windows_terminal = """
os: windows
and app.name: WindowsTerminal.exe
os: windows
and app.exe: WindowsTerminal.exe
"""

ctx.matches = r"""
app: windows_terminal
"""


@ctx.action_class("app")
class AppActions:
    def window_open():
        key("ctrl-shift-n")

    def tab_open():
        key("ctrl-shift-t")

    def tab_close():
        key("ctrl-shift-w")

    def tab_previous():
        key("ctrl-shift-tab")

    def tab_next():
        key("ctrl-tab")

    def preferences():
        key("ctrl-,")


@ctx.action_class("edit")
class EditActions:
    def copy():
        key("ctrl-shift-c")

    def paste():
        key("ctrl-shift-v")

    def find(text: str = None):
        key("ctrl-shift-f")
        if text:
            actions.insert(text)


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        """Jumps to the specified tab"""
        key(f"ctrl-alt-{number}")

    def tab_final():
        actions.user.tab_jump(1)
        actions.app.tab_previous()

    def tab_duplicate():
        key("ctrl-shift-d")
