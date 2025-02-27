from talon import Context, Module, app, ui, actions
from talon.grammar import Phrase
import re
import time
from ...imgui import imgui


mod = Module()
ctx = Context()

mod.mode("focus")
mod.list("running_application", desc="all running applications")
ctx.lists["self.running_application"] = {}

# Mapping of current overrides
overrides = {}


def parse_name(name):
    if name.lower() in overrides:
        return overrides[name.lower()]
    # Remove executable file ending
    if name.endswith(".exe"):
        name = name.rsplit(".", 1)[0]
    # Remove the last `-` and everything after it
    if " - " in name:
        name = name.rsplit(" - ", 1)[0]
    # Remove numbers
    name = re.sub(r"\d", "", name)
    # Split on camel case
    name = re.sub(r"[^a-zA-Z]", " ", name)
    name = actions.user.de_camel(name)
    return name


def update_running():
    running = {}
    for app in ui.apps(background=False):
        name = parse_name(app.name)
        if name:
            running[name] = app.name
    ctx.lists["self.running_application"] = running


def update_overrides(csv_dict: dict):
    """Updates the overrides list"""
    global overrides
    overrides = {k.lower(): v for k, v in csv_dict.items()}
    update_running()

    # for i in sorted(overrides):
    #     print(f"{i}: {overrides[i]}")


def cycle_windows(app: ui.App, diff: int):
    active = app.active_window
    windows = list(
        filter(
            lambda w: w == active or is_valid_window(w),
            app.windows(),
        )
    )
    windows.sort(key=lambda w: w.id)
    current = windows.index(active)
    max = len(windows) - 1
    i = actions.user.cycle(current + diff, 0, max)

    while i != current:
        try:
            actions.user.focus_window(windows[i])
            break
        except:
            i = actions.user.cycle(i + diff, 0, max)


def focus_name(name: str):
    app = actions.user.get_app(name)
    # Focus next window on same app
    if app == ui.active_app():
        cycle_windows(app, 1)
    # Focus app
    else:
        actions.user.focus_app(app)


@ctx.action_class("app")
class AppActionsWin:
    def window_previous():
        cycle_windows(ui.active_app(), -1)

    def window_next():
        cycle_windows(ui.active_app(), 1)


@mod.action_class
class Actions:
    def focus_name(name: str, phrase: Phrase = None):
        """Focus application by name"""
        focus_name(name)
        actions.user.focus_hide()
        if phrase:
            actions.sleep("300ms")
            actions.user.rephrase(phrase)

    def focus_names(names: list[str], phrases: list[Phrase]):
        """Focus applications by name"""
        for n, p in zip(names, phrases):
            actions.user.focus_name(n, p)

    def focus_index(index: int):
        """Focus application by index"""
        names = list(ctx.lists["user.running_application"].values())
        if index > -1 and index < len(names):
            actions.user.focus_name(names[index])

    def focus_help_toggle():
        """Shows/hides all running applications"""
        if gui.showing:
            actions.user.focus_hide()
        else:
            actions.mode.enable("user.focus")
            gui.show()

    def focus_hide():
        """Hides list of running applications"""
        actions.mode.disable("user.focus")
        gui.hide()

    def focus_app(app: ui.App):
        """Focus app and wait until finished"""
        app.focus()
        t1 = time.monotonic()
        while ui.active_app() != app:
            if time.monotonic() - t1 > 1:
                raise RuntimeError(f"Can't focus app: {app.name}")
            actions.sleep("50ms")

    def focus_window(window: ui.Window):
        """Focus window and wait until finished"""
        window.focus()

        t1 = time.monotonic()
        while ui.active_window() != window:
            if time.monotonic() - t1 > 1:
                raise RuntimeError(f"Can't focus window '{window.title}'")
            actions.sleep("50ms")

    def get_app(name: str) -> ui.App:
        """Get application by name"""
        all_apps = ui.apps(background=False)

        # First try to get application by default name
        apps = list(filter(lambda app: app.name == name, all_apps))

        # Second try to get application by alternative name
        if not apps:
            alt_name = parse_name(name)
            apps = list(filter(lambda app: app.name == alt_name, all_apps))

        # No application found for either name
        if not apps:
            raise RuntimeError(f"App '{name}' not running")

        # Multiple hits on this application. Filter out applications with invalid active window
        if len(apps) > 1:
            apps2 = list(filter(lambda app: is_valid_window(app.active_window), apps))
            if apps2:
                return apps2[0]

        # Finally just pick the first application
        if apps:
            return apps[0]


def is_valid_window(window: ui.Window) -> bool:
    return (
        not window.hidden
        and window.title != ""
        and window.rect.width > window.screen.dpi
        and window.rect.height > window.screen.dpi
    )


@imgui.open(numbered=True)
def gui(gui: imgui.GUI):
    gui.header("Focus")
    gui.line(bold=True)
    for name in ctx.lists["self.running_application"]:
        gui.text(name)
    gui.spacer()
    if gui.button("Hide"):
        actions.user.focus_hide()


def on_ready():
    actions.user.watch_csv_as_dict("app_name_overrides.csv", update_overrides)
    ui.register("app_launch", lambda _: update_running())
    ui.register("app_close", lambda _: update_running())


app.register("ready", on_ready)
