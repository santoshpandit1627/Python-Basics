import re
#a = re.match(pattern, string, optional flag)
mystr = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, Javascript or PHP."

a = re.match("You", mystr)
a.group()

import re
arp = "22.22.22.1   0   b4:19:5a:ff:c8:45   VLAN#222       L"
a = re.search(r"(.+?) +(\d) +(.+?) \s{2,} (\w)*", arp)
a.group(1)