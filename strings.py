#collectrion of characters
b='python life'
a="python life"
v='''python life'''
print(type(a),type(b),type(v))
#upper
me="vamsikrishna"
print(me.upper())
#lower
me="VAMSI KRISHNA"
print(me.lower())
#endswith,starts with
print(me.endswith("KRISHNA"))
print(me.startswith("VAMSI"))
#REPLACE
print(me.replace("VAMSI","SAI"))
#INDEX,FIND
print(me.index("VAMSI"))
print(me.find("VAMSI"))
#REMOVE SUFFIX
print(me.removesuffix("KRISHNA"))
print(me.removeprefix("VAMSI"))
#COUNT
print(me.count("V"))
#SPLIT -is used to convert string to list
print(me.split())
#strip
me="   vamsikrishna    "
print(len(me))
v=me.strip()
print(len(v))
# l strip
v=me.lstrip()
print(len(v))
#r srtip
v=me.rstrip()
print(len(v))
