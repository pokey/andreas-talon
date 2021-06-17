from talon import Context, actions, Module, app

ctx = Context()
mod = Module()

mod.apps.slack = """
tag: browser
and title: /Slack/
"""

ctx.matches = r"""
app: slack
"""

@ctx.action_class("edit")
class user_actions:
    def line_insert_down():
        actions.key("end ctrl-enter")
