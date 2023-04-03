# Exer-15-Launching-a-Web Browser

import webbrowser

webbrowser.open("http://www.python.org")

###

# Open the page in a new browser window
webbrowser.open_new("http://www.python.org")

# Open the page in a new browser tab
webbrowser.open_new_tab("http://www.python.org")

###

# Open a page in a specific browser
c = webbrowser.get("safari")
c.open("http://www.python.org")
c.open_new_tab("http://docs.python.org")
