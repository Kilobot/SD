def rvr(str):
    if len(str)==0:
        return ''
    else:
        return rvr(str[1:])+str[0]
str="pots&pans"

print(rvr(str))