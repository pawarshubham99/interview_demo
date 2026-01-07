# aaaaa
# aa

s1 = "aaaaa"
s2 = "aa"


def overlaping_string(s1, s2):
    n = len(s1)
    m = len(s2)
    count = 0
    for i in range(n):
        if s1[i:i+m] == s2:
            count +=1
    return (s1, s2, count)


overlaping_string("aaaaa" , "aa" )
