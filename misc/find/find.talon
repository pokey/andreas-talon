tag: user.find
-

scout for clip:             edit.find(clip.text())
scout [<user.text>]$:       edit.find(text or "")

scout all for clip:         user.find_everywhere(clip.text())
scout all [<user.text>]$:   user.find_everywhere(text or "")

replace [<user.text>]$:     user.find_replace(text or "")
replace all [<user.text>]$: user.find_replace_everywhere(text or "")

scout case:                 user.find_toggle_match_by_case()
scout word:                 user.find_toggle_match_by_word()
scout expression:           user.find_toggle_match_by_regex()
replace case:               user.find_replace_toggle_preserve_case()

scout last:                 edit.find_previous()
scout next:                 edit.find_next()

scout hide:
    edit.find("")
    sleep(100ms)
    key(escape)

replace confirm:            user.find_replace_confirm()
replace confirm all:        user.find_replace_confirm_all()

scout file for clip:        user.find_file(clip.text())
scout file [<user.text>] [<user.extension>]$:
    text = text or ""
    extension = extension or ""
    user.find_file(text + extension)

pop <user.text>$:
    edit.find(text)
    key(enter)

pop file <user.text> [<user.extension>]$:
    extension = extension or ""
    user.find_file(text + extension)
    sleep(300ms)
    key(enter)
