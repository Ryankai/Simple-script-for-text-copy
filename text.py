import pyperclip as pp


while True:
    t = pp.waitForNewPaste()
    print('New item copied to clipboard!')
    t = t.replace("\r\n", " ")

    pp.copy(t)


