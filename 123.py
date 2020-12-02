ik = input('Insert isikukood')
if int(len(ik)) != 11:
    print('vale lenght')
for char in ik:
    if not (char.isdigit()):
        print('vale digit')
        break
if ik[:1] in ('1', '3', '5'):
    print("Mees")
elif ik[:1] in ('2', '4', '6'):
    print("Naine")
else:
    print("Vale isikukood")
# comment
