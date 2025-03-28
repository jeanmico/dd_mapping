import re  # regular expressions
with open('/mnt/c/Users/jeanmico/projects/misc/dunks/data/addresses_raw.txt') as infile:
    raw = infile.read().splitlines()

print(len(raw))

a = raw[0]
print(a)
a1 = re.sub(r'MA ([0-9]{5})', r'MA,\1', a )
print(a1)

raw1 = [re.sub(r'MA ([0-9]{5})', r'MA,\1', i) for i in raw]  # comma between state and zip
print(raw1[0:10])

raw2 = [re.sub(r'( [a-zA-z]+, *MA)' ,r',\1' , i) for i in raw1]  # comma between street and town
a2 = re.sub(r'( [a-zA-z]+, *MA)' ,r',\1' , a1)
print(a2)
#with open('/mnt/c/Users/jeanmico/projects/misc/dunks/data/addresses_processed.txt', 'w') as outfile:
#    outfile.write('\n'.join(str(i) for i in my_adds))