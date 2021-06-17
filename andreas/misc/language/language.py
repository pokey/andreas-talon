from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

extension_lang_map = {
    ".asm": "assembly",
    ".bat": "batch",
    ".c": "c",
    ".cmake": "cmake",
    ".cpp": "cplusplus",
    ".cs": "csharp",
    ".gdb": "gdb",
    ".go": "go",
    ".h": "c",
    ".hpp": "cplusplus",
    ".java": "java",
    ".js": "javascript",
    ".jsx": "javascript",
    ".json": "json",
    ".lua": "lua",
    ".md": "markdown",
    ".pl": "perl",
    ".ps1": "powershell",
    ".py": "python",
    ".r": "r",
    ".rb": "ruby",
    ".s": "assembly",
    ".sh": "bash",
    ".snippets": "snippets",
    ".talon": "talon",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".vba": "vba",
    ".vim": "vimscript",
    ".vimrc": "vimscript",
    ".html": "html"
}

@ctx.action_class("code")
class code_actions:
    def language():
        file_extension = actions.win.file_ext()
        if file_extension and file_extension in extension_lang_map:
            return extension_lang_map[file_extension]
        return ""

mod.mode("auto_lang")
# create a mode for each defined language
for __, lang in extension_lang_map.items():
    mod.mode(lang)

@mod.action_class
class Actions:
    def code_set_language_mode(language: str):
        """Sets the active language mode, and disables extension matching"""
        actions.user.code_clear_language_mode()
        actions.mode.disable("user.auto_lang")
        actions.mode.enable("user.{}".format(language))
        app.notify("Enabled {} mode".format(language))

    def code_clear_language_mode():
        """Clears the active language mode, and re-enables code.language: extension matching"""
        actions.mode.enable("user.auto_lang")
        for __, lang in extension_lang_map.items():
            actions.mode.disable("user.{}".format(lang))

def on_ready():
    actions.mode.enable("user.auto_lang")

app.register("ready", on_ready)