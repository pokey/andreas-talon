tag: browser
-
tag(): user.zoom
tag(): user.tabs

^(address bar | go address | go url)$:   browser.focus_address()
^go home$:                               browser.go_home()
^go forward$:                            browser.go_forward()
^go (back | backward)$:                  browser.go_back()

^go private$:                            browser.open_private_window()

^copy address$:
	browser.focus_address()
	edit.copy()

^bookmark show$:                         browser.bookmarks()
^bookmark bar$:                          browser.bookmarks_bar()
^bookmark it$:                           browser.bookmark()
^bookmark tabs$:                         browser.bookmark_tabs()

^(refresh | reload) page$:               browser.reload()
^(refresh | reload) page hard$:          browser.reload_hard()

^show downloads$:                        browser.show_downloads()
^show extensions$:                       browser.show_extensions()
^show history$:                          browser.show_history()
^show cache$:                            browser.show_clear_cache()

^dev tools$:                             browser.toggle_dev_tools()