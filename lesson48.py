import string

s = """\
Hi $name.
$contents
Hava a good day.
"""

t = string.Template(s)
content = t.substitute(name="Eric", contents="How are you")
print(content)