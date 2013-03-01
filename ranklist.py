import requests
import simplejson as json

def get_ranklist():
	f = open("trap.txt", "r")
	ranklist = []
	for line in f:
		tokens = line.split(' ')
		tokens[1] = tokens[1].rstrip()
		r = requests.get('http://uhunt.felix-halim.net/api/ranklist/'+ tokens[1] +'/0/0')
		data = json.loads(r.text)
		d = data[0]
		ranklist.append((d['name'], d['username'], d['ac'], d['nos']))

	return sorted(ranklist, key=lambda member : member[2], reverse=True)

if __name__ == '__main__':
	f = open("ranklist.txt", "w")
	ranklist = get_ranklist()
	for item in ranklist:
		f.write('%s %s %d %d\n' % (item))