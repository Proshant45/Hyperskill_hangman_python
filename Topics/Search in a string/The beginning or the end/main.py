x = input()
st = x.find("old")
ed = x.rfind("old")

if st>ed:
    print(st)
else:
    print(ed)
