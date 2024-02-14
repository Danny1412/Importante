import re

texto = "The quick brown fox jump over lazy dog"

x = re.search("^The.*dog$", texto)

if x:
    print("SI")
else:
    print("NO")