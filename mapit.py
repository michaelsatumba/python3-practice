import webbrowser, sys, pyperclip
print('hello where are you going?')

if len(sys.argv) > 1:
   address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
