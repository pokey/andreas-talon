# Switch to dictation mode and insert a phrase
dictate [<phrase>]$:        user.dictation_mode(phrase or "")

# Switch to swedish dictation
swedish$:                   user.swedish_mode()

# Switch to mixed mode and insert a phrase
mixed mode [<phrase>]$:     user.mixed_mode(phrase or "")

# Just guard so you can always try to break out of dictation mode and it won't do anything weird
command mode:               skip()
