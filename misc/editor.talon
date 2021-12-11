# ----- Navigation -----
page up:                  edit.page_up()
page down:                edit.page_down()

go top:
    user.stop_app()
    edit.file_start()
go bottom:
    user.stop_app()
    edit.file_end()

head:                     edit.line_start()
tail:                     edit.line_end()
middle:                   user.line_middle()

up [<number_small>]:      user.up(number_small or 1)
down [<number_small>]:    user.down(number_small or 1)
left [<number_small>]:    user.left(number_small or 1)
right [<number_small>]:   user.right(number_small or 1)

lefter:                   edit.word_left()
righter:                  edit.word_right()

slap:                     edit.line_insert_down()
slapper:                  user.line_insert_down_twice()

indent:                   edit.indent_more()
dedent:                   edit.indent_less()

# ----- Selection -----
take all:                 edit.select_all()
take none:                edit.select_none()

extend top:               edit.extend_file_start()
extend bottom:            edit.extend_file_end()
extend head:              edit.extend_line_start()
extend tail:              edit.extend_line_end()

extend up:                edit.extend_up()
extend down:              edit.extend_down()
extend left:              edit.extend_left()
extend right:             edit.extend_right()

extend lefter:            edit.extend_word_left()
extend righter:           edit.extend_word_right()

# ----- Delete, undo, redo -----
undo:                     edit.undo()
redo:                     edit.redo()

dell:                     edit.delete()
drill:                    user.delete_right()

# ----- Cut, copy, paste -----
cut this:                 edit.cut()
copy this:                edit.copy()
paste it:                 edit.paste()
paste special:            edit.paste_match_style()

# ----- Word -----
take word:                edit.select_word()
cut word:                 user.cut_word()
copy word:                user.copy_word()
paste to word:            user.paste_word()
(chuck | clear) word:     edit.delete_word()

remove:                   user.delete_word_left()
wipe:                     user.delete_word_right()

# ----- Misc -----
drag up:                  edit.line_swap_up()
drag down:                edit.line_swap_down()
disk:                     edit.save()