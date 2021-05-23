import re
#a = re.match(pattern, string, optional flag)
mystr = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, Javascript or PHP."

a = re.match("You", mystr)
a.group()