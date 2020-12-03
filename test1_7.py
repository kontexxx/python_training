c = input('slovo')
if c != c[::-1]: # -1 здесь шаг строки: от конца к началу
    print("It's not palindrome")
else:
    print("It's palindrome")
#как с пробелами не осилил