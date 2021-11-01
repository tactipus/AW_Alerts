import re

aw_keywords = re.compile("#AdvanceWars+")
text = "All right, new #AdvanceWars is coming out in April!"

x = re.findall(aw_keywords, text)
print(x)
