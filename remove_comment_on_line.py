file = input("File: ")
data = open(file, 'rb').read().split(b'\n')
new_data = []

for i in data:
	try:
		if "#" == i.decode('utf-8')[0]:
			continue
	except IndexError:
		pass
	if not i.strip():
		continue
	new_data.append(i)

data = b"\n".join(new_data)
open("recom-" + str(file), 'wb').write(data)
print("Done!")