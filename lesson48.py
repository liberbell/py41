import string

with open("design/email_template.txt", "r") as f:
    t = string.Template(f.read())

content = t.substitute(name="Eric", contents="How are you")
print(content)