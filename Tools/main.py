def input_int(string, bad_text="Не число"):
    ans = input(string)
    if ans.isdigit():
        return int(ans)
    else:
        print(bad_text)
        return input_int(string)


def input_variant(lst, string):
    print(string)
    for i, el in enumerate(lst):
        print(f"{i + 1} - {el}")
    i = input_int("Ваш выбор: ") - 1
    if 0 <= i <= len(lst) - 1:
        return lst[i]
    else:
        print('Некорректный вариант!')
        return input_variant(lst, string)
