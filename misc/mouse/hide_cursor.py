from talon import Module, actions, app, ctrl
import os


app.register("ready", lambda: actions.user.mouse_show_cursor())

default_cursor = {
    "AppStarting": r"%SystemRoot%\Cursors\aero_working.ani",
    "Arrow": r"%SystemRoot%\Cursors\aero_arrow.cur",
    "Hand": r"%SystemRoot%\Cursors\aero_link.cur",
    "Help": r"%SystemRoot%\Cursors\aero_helpsel.cur",
    "No": r"%SystemRoot%\Cursors\aero_unavail.cur",
    "NWPen": r"%SystemRoot%\Cursors\aero_pen.cur",
    "Person": r"%SystemRoot%\Cursors\aero_person.cur",
    "Pin": r"%SystemRoot%\Cursors\aero_pin.cur",
    "SizeAll": r"%SystemRoot%\Cursors\aero_move.cur",
    "SizeNESW": r"%SystemRoot%\Cursors\aero_nesw.cur",
    "SizeNS": r"%SystemRoot%\Cursors\aero_ns.cur",
    "SizeNWSE": r"%SystemRoot%\Cursors\aero_nwse.cur",
    "SizeWE": r"%SystemRoot%\Cursors\aero_ew.cur",
    "UpArrow": r"%SystemRoot%\Cursors\aero_up.cur",
    "Wait": r"%SystemRoot%\Cursors\aero_busy.ani",
    "Crosshair": "",
    "IBeam": "",
}

hidden_cursor = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), r"HiddenCursor.cur"
)

mod = Module()

@mod.action_class
class Actions:
    def mouse_show_cursor():
        """Shows the cursor"""
        show_cursor_helper(True)

    def mouse_hide_cursor():
        """Hides the cursor"""
        show_cursor_helper(False)

def show_cursor_helper(show):
    """Show/hide the cursor"""
    if app.platform == "windows":
        import ctypes
        import winreg
        import win32con

        try:
            Registrykey = winreg.OpenKey(
                winreg.HKEY_CURRENT_USER, r"Control Panel\Cursors", 0, winreg.KEY_WRITE
            )

            for value_name, value in default_cursor.items():
                if show:
                    winreg.SetValueEx(
                        Registrykey, value_name, 0, winreg.REG_EXPAND_SZ, value
                    )
                else:
                    winreg.SetValueEx(
                        Registrykey, value_name, 0, winreg.REG_EXPAND_SZ, hidden_cursor
                    )

            winreg.CloseKey(Registrykey)

            ctypes.windll.user32.SystemParametersInfoA(
                win32con.SPI_SETCURSORS, 0, None, 0
            )

        except WindowsError:
            print("Unable to show_cursor({})".format(str(show)))
    else:
        ctrl.cursor_visible(show)