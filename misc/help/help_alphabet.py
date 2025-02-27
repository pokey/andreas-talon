from talon import Module, actions, Module, registry
from ...imgui import imgui

mod = Module()
mod.mode("help_alphabet", "Mode for showing the alphabet help gui")


@imgui.open()
def gui(gui: imgui.GUI):
    gui.header("Alphabet")
    gui.line(bold=True)
    alphabet = registry.lists["user.letter"][0]
    for key, val in alphabet.items():
        gui.text(f"{val}:  {key}")
    gui.spacer()
    if gui.button("Hide"):
        actions.user.help_alphabet_toggle()


@mod.action_class
class Actions:
    def help_alphabet_toggle():
        """Toggle help alphabet gui"""
        if gui.showing:
            actions.mode.disable("user.help_alphabet")
            gui.hide()
        else:
            actions.mode.enable("user.help_alphabet")
            gui.show()
