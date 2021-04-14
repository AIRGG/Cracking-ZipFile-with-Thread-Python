import random, string
mypass = "abcdefg"
maxrand = 5000
with open("wordlist.txt", "w") as f:
	luckyNumber = random.randint(1000, maxrand-1)
	for x in range(maxrand):
		f.write(''.join(random.sample(string.ascii_letters, random.randint(5,10)))+"\n")
		if x == luckyNumber:
			f.write(mypass+"\n")