mode: user.game
tag: user.game_commands
-

settings():
    user.foot_switch_timeout = 0

^command mode$:             user.game_mode_disable()

^game mode$:                skip()
