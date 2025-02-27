not app: vscode
-

# ----- Word -----
take token:                 edit.select_word()
cut token:                  user.cut_word()
copy token:                 user.copy_word()
paste to token:             user.paste_word()
(chuck | clear) token:      edit.delete_word()

# Line
pre line:                   edit.line_start()
post line:                  edit.line_end()
clone line:                 edit.line_clone()
drink line:                 edit.line_insert_up()
pour line:                  edit.line_insert_down()

# Head / tail
take head:                  user.select_line_start()
take tail:                  user.select_line_end()
cut head:                   user.cut_line_start()
cut tail:                   user.cut_line_end()
copy head:                  user.copy_line_start()
copy tail:                  user.copy_line_end()
(chuck | clear) head:       user.delete_line_start()
(chuck | clear) tail:       user.delete_line_end()

# Paragraph
pre block:                  edit.paragraph_start()
post block:                 edit.paragraph_end()
take block:                 edit.select_paragraph()
cut block:                  user.cut_paragraph()
copy block:                 user.copy_paragraph()
paste to block:             user.paste_paragraph()
(chuck | clear) block:      edit.delete_paragraph()

# File / document
pre file:                   edit.file_start()
post file:                  edit.file_end()
take file:                  edit.select_all()
cut file:                   user.cut_all()
copy file:                  user.copy_all()
paste to file:              user.paste_all()
(chuck | clear) file:       user.delete_all()

# Navigate to specified text/symbol: go right paren
{user.navigation_action} {user.navigation_direction} to <user.any_alphanumeric_key>:
    user.navigation(navigation_action, navigation_direction, any_alphanumeric_key)

# Reformat
<user.formatters> format this:
    user.reformat_selection(formatters)
<user.formatters> format token:
    edit.select_word()
    user.reformat_selection(formatters)
<user.formatters> format line:
    edit.select_line()
    user.reformat_selection(formatters)

# Homophones
phones this:                user.homophones_cycle_selected()
phones token:
    edit.select_word()
    user.homophones_cycle_selected()

# Wrappers
{user.delimiter_pair_wrap} wrap this:
    user.delimiters_pair_wrap_selection(delimiter_pair_wrap)
{user.delimiter_pair_wrap} wrap token:
    edit.select_word()
    user.delimiters_pair_wrap_selection(delimiter_pair_wrap)
{user.delimiter_pair_wrap} wrap line:
    edit.select_line()
    user.delimiters_pair_wrap_selection(delimiter_pair_wrap)
