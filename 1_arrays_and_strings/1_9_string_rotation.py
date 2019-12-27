# 1.9 String Rotation:Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

# Solution : check if s1 is found in s2+s2

def check_rotation(s1,s2):
    s2 = s2 + s2
    return s2.find(s1) >= 0

print(check_rotation(s1 = "waterbottle", s2 = "erbottlewat"))