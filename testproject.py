from requests import get
r = get('https://api.github.com/events').json()
keys = []
alert = 'What you wanna find?'
for i in r:
    for key in i.keys():
        if key not in keys:
            keys.append(key)

print(f'Select one key from:\n{keys}\n{alert}')

find = ''
while find not in keys:
    find = input()
    print(f'Sorry, not defined argument\n{keys}\n{alert}')
else:
    for i in r:
        print(i.get(find))
                