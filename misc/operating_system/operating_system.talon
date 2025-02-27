open settings:              app.preferences()

^system shutdown$:          user.system_shutdown()
^system restart$:           user.system_restart()
^system hibernate$:
    user.talon_sleep()
    user.repeat_command_block()
    user.system_hibernate()
^system lock$:              key(super-l)

open {user.launch_command}:
    user.exec(launch_command)

open path {user.path}:
    user.file_manager_open(path)

open browser {user.webpage}:
    user.browser_open(webpage)
