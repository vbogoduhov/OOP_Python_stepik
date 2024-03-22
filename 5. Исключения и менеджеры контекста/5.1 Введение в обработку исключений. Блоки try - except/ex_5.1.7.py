# lst_in = input().split()
# s = "1 -5.6 2 abc 0 False 22.5 hello world"
s = "8 11 abcd -7.5 2.0 -5"
lst_in = s.split()


def check_text_on_integer(text):
    try:
        val = int(text)
        return True
    except:
        return False


res = sum(map(int, filter(check_text_on_integer, lst_in)))
print(res)
