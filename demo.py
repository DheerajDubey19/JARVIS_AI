import webbrowser as wb

chromePath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
# search = takecommand()
# wb.register('chrome', None,wb.BackgroundBrowser(chromePath))
wb.get(chromePath).open_new_tab("facebook")
# print(search)
