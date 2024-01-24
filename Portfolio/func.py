def make_path (*names):
    result = ""
    for name in names:
        result += name + "/"
    return result

make_path('tbc')